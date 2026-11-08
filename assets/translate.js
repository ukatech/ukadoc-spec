/* 翻訳ボタン。ブラウザ組み込みの Translator API（Chrome 138 以降のデスクトップ版など）で、
   表示中のページの本文を日本語から英語・中国語（繁体・簡体）へ訳す。
   - API が無いブラウザではボタンを出さない
   - 訳すのは日本語を含む文だけ。コード（code / pre / kbd）と translate="no" の中は訳さない
   - 文はブロック（p / li / td など）の中の連なりを単位に、まとめて訳す。リンク・太字・コードスパンが文の途中にあっても、
     文が断片に切れない。コードスパンなど訳さないものは <x1/> のような印に、リンク・太字は <a2>…</a2> のような印の対に置き換えて訳し、
     訳したあとで元の要素に戻す。印が訳文で崩れたときは、その文だけテキストごとの訳（断片訳）に切り替える
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

  // 文の途中に置ける要素。これ以外（p / li / td / br など）は文の切れ目になる
  var INLINE_TAGS = {
    A: 1, ABBR: 1, B: 1, BDI: 1, BDO: 1, CITE: 1, CODE: 1, DATA: 1, DEL: 1, DFN: 1, EM: 1, I: 1, IMG: 1, INS: 1, KBD: 1,
    MARK: 1, Q: 1, S: 1, SAMP: 1, SMALL: 1, SPAN: 1, STRONG: 1, SUB: 1, SUP: 1, TIME: 1, U: 1, VAR: 1, WBR: 1
  };
  // 中にこれがある要素は、文の途中に置けない（文の切れ目を含むため）
  var BREAKERS = 'address, article, aside, blockquote, br, details, dialog, div, dl, fieldset, figure, footer, form, h1, h2, h3, h4, h5, h6, header, hr, li, main, nav, ol, p, pre, section, table, ul, summary';
  // 印が訳文で崩れる状況が続いたら（成功が一度もなく、これだけ失敗したら）、以後は断片訳だけにする
  var MARKER_GIVE_UP = 6;

  var state = { lang: null, gen: 0, translator: null, observer: null, markerOk: 0, markerBad: 0 };
  var records = [];                // 訳した場所の控え。原文へ戻すのに使う
  var pending = new Set();         // 未訳のブロック要素
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

  function toArray(list) { return Array.prototype.slice.call(list); }

  /* ---- 文の単位を切り出す ---- */

  // 文の途中に置けるノードか（テキスト、または切れ目を含まない inline 要素）
  function isInlineNode(n) {
    if (n.nodeType === 3) return true;
    if (n.nodeType !== 1) return false;
    return !!INLINE_TAGS[n.tagName] && !n.querySelector(BREAKERS);
  }

  // 訳さずにそのまま残す要素か（コードなど、または日本語を含まない）
  function isOpaque(el) {
    return el.matches(SKIP) || !JAPANESE.test(el.textContent);
  }

  // 子の並びを、文の切れ目（p / li / br など）で区切った連なりにする
  function buildRuns(el) {
    var runs = [];
    var cur = [];
    toArray(el.childNodes).forEach(function (n) {
      if (isInlineNode(n)) {
        cur.push(n);
      } else {
        if (cur.length) runs.push(cur);
        cur = [];
      }
    });
    if (cur.length) runs.push(cur);
    return runs;
  }

  // 連なりの両端の、空白だけのテキストと、訳さない要素（見出しの ¶ リンクなど）を外す
  function trimRun(run) {
    function skippable(n) { return n.nodeType === 3 ? !/\S/.test(n.nodeValue) : isOpaque(n); }
    var a = 0;
    var b = run.length;
    while (a < b && skippable(run[a])) a++;
    while (b > a && skippable(run[b - 1])) b--;
    return run.slice(a, b);
  }

  // そのブロックの直下に、訳すものがあるか
  function hasOwnRun(el) {
    var found = false;
    toArray(el.childNodes).forEach(function (n) {
      if (found || !isInlineNode(n)) return;
      if (n.nodeType === 3 ? JAPANESE.test(n.nodeValue) : !isOpaque(n)) found = true;
    });
    return found;
  }

  function collect(root) {
    var all = [root].concat(toArray(root.querySelectorAll('*')));
    all.forEach(function (el) {
      if (isInlineNode(el) || el.closest(SKIP) || !hasOwnRun(el)) return;
      pending.add(el);
      state.observer.observe(el);
    });
  }

  /* ---- 印への置き換えと、元の要素への復元 ---- */

  // ノードの並びを、印つきの文字列にする。訳さない要素は <xN/>、訳す要素は <aN>…</aN>。
  // ctx.map は 印の番号 -> 元の要素、ctx.hasMark は印を使ったか
  function serialize(nodes, ctx) {
    var s = '';
    nodes.forEach(function (n) {
      if (n.nodeType === 3) { s += n.nodeValue; return; }
      if (n.nodeType !== 1) return;
      var id = ++ctx.n;
      ctx.map[id] = n;
      ctx.hasMark = true;
      if (isOpaque(n)) {
        s += '<x' + id + '/>';
      } else {
        s += '<a' + id + '>' + serialize(toArray(n.childNodes), ctx) + '</a' + id + '>';
      }
    });
    return s;
  }

  // 訳文の印を元の要素に戻して、ノードの並びにする。印が欠けた・重なった・入れ子が崩れたときは null
  function rebuild(out, ctx) {
    var re = /<\s*(\/?)\s*([xXaA])\s*(\d+)\s*(\/?)\s*>/g;
    var root = document.createDocumentFragment();
    var stack = [root];
    var ids = [0];
    var seenX = {};
    var seenOpen = {};
    var seenClose = {};
    var last = 0;
    var m;

    function top() { return stack[stack.length - 1]; }
    function pushText(t) { if (t) top().appendChild(document.createTextNode(t)); }

    while ((m = re.exec(out))) {
      pushText(out.slice(last, m.index));
      last = re.lastIndex;
      var closing = m[1] === '/';
      var kind = m[2].toLowerCase();
      var id = parseInt(m[3], 10);
      var src = ctx.map[id];
      if (!src) return null;
      if (kind === 'x') {
        if (closing || seenX[id] || !isOpaque(src)) return null;
        seenX[id] = true;
        top().appendChild(src.cloneNode(true));
      } else if (!closing) {
        if (m[4] === '/' || seenOpen[id] || isOpaque(src)) return null;
        seenOpen[id] = true;
        var c = src.cloneNode(false);
        top().appendChild(c);
        stack.push(c);
        ids.push(id);
      } else {
        if (stack.length < 2 || ids[ids.length - 1] !== id) return null;
        seenClose[id] = true;
        stack.pop();
        ids.pop();
      }
    }
    pushText(out.slice(last));
    if (stack.length !== 1 || !root.firstChild) return null;

    for (var key in ctx.map) {
      if (!Object.prototype.hasOwnProperty.call(ctx.map, key)) continue;
      if (isOpaque(ctx.map[key])) { if (!seenX[key]) return null; }
      else if (!seenOpen[key] || !seenClose[key]) return null;
    }
    return toArray(root.childNodes);
  }

  /* ---- 訳す ---- */

  async function translateText(translator, lang, text) {
    var c = cache[lang] || (cache[lang] = {});
    var key = text.trim();
    if (!(key in c)) c[key] = await translator.translate(key);
    var lead = text.match(/^\s*/)[0];
    var trail = text.match(/\s*$/)[0];
    return lead + c[key] + trail;
  }

  function textNodesOf(nodes) {
    var out = [];
    function walk(n) {
      if (n.nodeType === 3) {
        if (JAPANESE.test(n.nodeValue)) out.push(n);
      } else if (n.nodeType === 1 && !n.matches(SKIP)) {
        toArray(n.childNodes).forEach(walk);
      }
    }
    nodes.forEach(walk);
    return out;
  }

  // 断片訳。テキストノードごとに別々に訳す（印が使えないときの代わり）
  async function translateFragments(nodes, gen) {
    var texts = textNodesOf(nodes);
    for (var i = 0; i < texts.length; i++) {
      if (gen !== state.gen) return;
      var node = texts[i];
      if (!node.isConnected) continue;
      var original = node.nodeValue;
      try {
        var out = await translateText(state.translator, state.lang, original);
        if (gen !== state.gen) return;
        records.push({ kind: 't', node: node, original: original });
        node.nodeValue = out;
      } catch (e) {
        /* 1 か所の失敗で全体を止めない */
      }
    }
  }

  // 連なり 1 つを訳す
  async function translateRun(run, gen) {
    var nodes = trimRun(run);
    if (!nodes.length) return;

    // 外側が 1 つの要素だけのとき（li の中のリンク、リンクの中の span など）は、印にせず中へ入る
    if (nodes.length === 1 && nodes[0].nodeType === 1) {
      await translateBlock(nodes[0], gen);
      return;
    }

    var ctx = { map: {}, n: 0, hasMark: false };
    var src = serialize(nodes, ctx);
    if (!JAPANESE.test(src)) return;
    if (nodes.some(function (n) { return !n.isConnected; })) return;

    // 印が無い（テキストだけの）連なりは、1 つの文としてそのまま訳せる
    if (!ctx.hasMark) {
      var texts = nodes.filter(function (n) { return n.nodeType === 3; });
      try {
        var out = await translateText(state.translator, state.lang, src);
        if (gen !== state.gen) return;
        texts.forEach(function (n, i) {
          records.push({ kind: 't', node: n, original: n.nodeValue });
          n.nodeValue = i === 0 ? out : '';
        });
      } catch (e) { /* 1 か所の失敗で全体を止めない */ }
      return;
    }

    if (state.markerOk > 0 || state.markerBad < MARKER_GIVE_UP) {
      try {
        var translated = await translateText(state.translator, state.lang, src);
        if (gen !== state.gen) return;
        var built = rebuild(translated, ctx);
        if (built) {
          state.markerOk++;
          var first = nodes[0];
          var parent = first.parentNode;
          if (!parent || nodes.some(function (n) { return n.parentNode !== parent; })) return;
          built.forEach(function (n) { parent.insertBefore(n, first); });
          nodes.forEach(function (n) { parent.removeChild(n); });
          records.push({ kind: 'r', originals: nodes, inserted: built });
          return;
        }
        state.markerBad++;
      } catch (e) {
        /* 訳せなかったときは、断片訳へ */
      }
    }
    await translateFragments(nodes, gen);
  }

  // ブロック 1 つの直下の文を、順に訳す
  async function translateBlock(el, gen) {
    var runs = buildRuns(el);
    for (var i = 0; i < runs.length; i++) {
      if (gen !== state.gen) return;
      await translateRun(runs[i], gen);
    }
  }

  async function translateElement(el, gen) {
    if (!pending.has(el)) return;
    pending.delete(el);
    if (!el.isConnected) return;
    await translateBlock(el, gen);
  }

  var queue = Promise.resolve();
  function enqueue(el, gen) {
    queue = queue.then(function () { return translateElement(el, gen); });
  }

  function restore() {
    state.gen++;
    if (state.observer) { state.observer.disconnect(); state.observer = null; }
    pending.clear();
    for (var i = records.length - 1; i >= 0; i--) {
      var r = records[i];
      if (r.kind === 't') {
        r.node.nodeValue = r.original;
      } else {
        var first = r.inserted[0];
        var parent = first && first.parentNode;
        if (!parent) continue;
        r.originals.forEach(function (o) { parent.insertBefore(o, first); });
        r.inserted.forEach(function (n) { if (n.parentNode) n.parentNode.removeChild(n); });
      }
    }
    records = [];
    state.lang = null;
    state.translator = null;
    state.markerOk = 0;
    state.markerBad = 0;
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
