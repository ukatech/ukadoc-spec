/* 翻訳ボタン。ブラウザ組み込みの Translator API（Chrome 138 以降のデスクトップ版など）で、
   表示中のページの本文を日本語から英語・中国語（繁体・簡体）へ訳す。
   - API が無いブラウザではボタンを出さない
   - 訳すのは日本語を含むテキストノードだけ。コード（code / pre / kbd）と translate="no" の中は訳さない
   - 画面に近づいた所から順に訳す（まとめ頁は長いため）。訳した文は覚えておき、同じ文は再訳しない
   - 選んだ言語は localStorage に覚え、次の頁を開いたとき、モデルが取得済みなら自動で訳す
   機械翻訳なので、読める程度の品質。仕様の判断には原文を見ること */
(function () {
  'use strict';
  if (typeof Translator === 'undefined') return;

  var SOURCE = 'ja';
  var LANGS = [
    { code: 'en', label: 'English' },
    { code: 'zh-Hant', label: '繁體中文' },
    { code: 'zh', label: '简体中文' }
  ];
  var STORE_KEY = 'ukadoc-translate-lang';
  var ROOTS = '.md-content, .md-sidebar';
  var SKIP = 'pre, code, kbd, script, style, svg, [translate="no"], .headerlink, .ukadoc-translate';
  var JAPANESE = /[぀-ヿ㐀-鿿ｦ-ﾟ]/;

  var state = { lang: null, gen: 0, translator: null, observer: null };
  var originals = new WeakMap();   // テキストノード -> 原文
  var pending = new Map();         // 親の要素 -> その中の未訳のテキストノード
  var cache = {};                  // 言語コード -> { 原文: 訳文 }
  var els = {};

  function load() { try { return localStorage.getItem(STORE_KEY); } catch (e) { return null; } }
  function save(v) {
    try { if (v) localStorage.setItem(STORE_KEY, v); else localStorage.removeItem(STORE_KEY); } catch (e) { /* 覚えられなくても動く */ }
  }

  function setStatus(text) { els.status.textContent = text || ''; }

  function setActive(code) {
    els.button.classList.toggle('ukadoc-translate__button--on', !!code);
    Array.prototype.forEach.call(els.menu.querySelectorAll('button[data-lang]'), function (b) {
      b.setAttribute('aria-pressed', String(b.dataset.lang === (code || '')));
    });
  }

  function collect(root) {
    var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        if (!JAPANESE.test(n.nodeValue)) return NodeFilter.FILTER_REJECT;
        var p = n.parentElement;
        return p && !p.closest(SKIP) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT;
      }
    });
    var n;
    while ((n = walker.nextNode())) {
      if (originals.has(n)) continue;
      var p = n.parentElement;
      if (!pending.has(p)) pending.set(p, []);
      pending.get(p).push(n);
      state.observer.observe(p);
    }
  }

  async function translateText(translator, lang, text) {
    var c = cache[lang] || (cache[lang] = {});
    var key = text.trim();
    if (!(key in c)) c[key] = await translator.translate(key);
    var lead = text.match(/^\s*/)[0];
    var trail = text.match(/\s*$/)[0];
    return lead + c[key] + trail;
  }

  async function translateElement(el, gen) {
    var nodes = pending.get(el);
    if (!nodes) return;
    pending.delete(el);
    for (var i = 0; i < nodes.length; i++) {
      if (gen !== state.gen) return;
      var node = nodes[i];
      if (!node.isConnected || originals.has(node)) continue;
      var original = node.nodeValue;
      try {
        var out = await translateText(state.translator, state.lang, original);
        if (gen !== state.gen) return;
        originals.set(node, original);
        node.nodeValue = out;
      } catch (e) {
        /* 1 か所の失敗で全体を止めない */
      }
    }
  }

  var queue = Promise.resolve();
  function enqueue(el, gen) {
    queue = queue.then(function () { return translateElement(el, gen); });
  }

  function restore() {
    state.gen++;
    if (state.observer) { state.observer.disconnect(); state.observer = null; }
    pending.clear();
    var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    var n;
    while ((n = walker.nextNode())) {
      if (originals.has(n)) { n.nodeValue = originals.get(n); originals.delete(n); }
    }
    state.lang = null;
    state.translator = null;
    document.documentElement.lang = state.htmlLang;
    document.documentElement.removeAttribute('data-translated');
  }

  async function start(code, interactive) {
    var lang = LANGS.filter(function (l) { return l.code === code; })[0];
    if (!lang) return;
    if (state.lang) { restore(); setActive(null); }
    var gen = ++state.gen;
    var opts = { sourceLanguage: SOURCE, targetLanguage: code };
    var avail;
    try { avail = await Translator.availability(opts); } catch (e) { avail = 'unavailable'; }
    if (avail === 'unavailable') {
      setStatus('This language is not available in this browser / このブラウザでは使えません');
      return;
    }
    // 取得が要るモデルは、利用者の操作（クリック）の中でないと作れない。自動のときは取得済みの場合だけ進める
    if (!interactive && avail !== 'available') return;
    try {
      setStatus(avail === 'available' ? 'Translating… / 翻訳中…' : 'Downloading model… / モデルを取得中…');
      state.translator = await Translator.create({
        sourceLanguage: SOURCE,
        targetLanguage: code,
        monitor: function (m) {
          m.addEventListener('downloadprogress', function (e) {
            setStatus('Downloading model… / モデルを取得中… ' + Math.round(e.loaded * 100) + '%');
          });
        }
      });
    } catch (e) {
      setStatus('Failed to start translation / 翻訳を始められませんでした');
      return;
    }
    if (gen !== state.gen) return;
    state.lang = code;
    save(code);
    setActive(code);
    setStatus('Machine translation (' + lang.label + ') / 機械翻訳');
    document.documentElement.lang = code;
    document.documentElement.setAttribute('data-translated', code);
    state.observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        state.observer.unobserve(en.target);
        enqueue(en.target, gen);
      });
    }, { rootMargin: '800px 0px' });
    Array.prototype.forEach.call(document.querySelectorAll(ROOTS), collect);
  }

  function showOriginal() {
    if (state.lang) restore();
    save(null);
    setActive(null);
    setStatus('');
  }

  function build() {
    state.htmlLang = document.documentElement.lang;

    var wrap = document.createElement('div');
    wrap.className = 'md-header__option ukadoc-translate';
    wrap.setAttribute('translate', 'no');

    var button = document.createElement('button');
    button.type = 'button';
    button.className = 'md-header__button md-icon ukadoc-translate__button';
    button.title = 'Translate / 翻訳';
    button.setAttribute('aria-label', 'Translate / 翻訳');
    button.setAttribute('aria-haspopup', 'true');
    button.setAttribute('aria-expanded', 'false');
    button.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12.87 15.07l-2.54-2.51.03-.03A17.5 17.5 0 0 0 14.07 6H17V4h-7V2H8v2H1v2h11.17C11.5 7.92 10.44 9.75 9 11.35 8.07 10.32 7.3 9.19 6.69 8h-2c.73 1.63 1.73 3.17 2.98 4.56l-5.09 5.02L4 19l5-5 3.11 3.11zM18.5 10h-2L12 22h2l1.12-3h4.75L21 22h2zm-2.62 7 1.62-4.33L19.12 17z"/></svg>';

    var menu = document.createElement('div');
    menu.className = 'ukadoc-translate__menu';
    menu.hidden = true;
    var list = document.createElement('ul');
    LANGS.forEach(function (l) {
      var li = document.createElement('li');
      var b = document.createElement('button');
      b.type = 'button';
      b.dataset.lang = l.code;
      b.textContent = l.label;
      b.setAttribute('aria-pressed', 'false');
      li.appendChild(b);
      list.appendChild(li);
    });
    var li = document.createElement('li');
    var orig = document.createElement('button');
    orig.type = 'button';
    orig.dataset.lang = '';
    orig.textContent = '日本語（原文 / Original）';
    orig.setAttribute('aria-pressed', 'true');
    li.appendChild(orig);
    list.appendChild(li);
    var status = document.createElement('p');
    status.className = 'ukadoc-translate__status';
    status.setAttribute('role', 'status');
    menu.appendChild(list);
    menu.appendChild(status);

    wrap.appendChild(button);
    wrap.appendChild(menu);
    els = { wrap: wrap, button: button, menu: menu, status: status };

    function toggle(open) {
      menu.hidden = !open;
      button.setAttribute('aria-expanded', String(open));
    }
    button.addEventListener('click', function () { toggle(menu.hidden); });
    document.addEventListener('click', function (e) { if (!wrap.contains(e.target)) toggle(false); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') toggle(false); });
    menu.addEventListener('click', function (e) {
      var b = e.target.closest('button[data-lang]');
      if (!b) return;
      if (b.dataset.lang) start(b.dataset.lang, true); else showOriginal();
    });

    var header = document.querySelector('.md-header__inner');
    if (!header) return false;
    var search = header.querySelector('label[for="__search"]');
    header.insertBefore(wrap, search || null);
    return true;
  }

  if (!build()) return;
  var saved = load();
  if (saved) start(saved, false);
})();
