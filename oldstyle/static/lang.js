/* 言語切替（全頁の右上。検索窓 search.js の右横）。
   - 日本語版（ルート）と、翻訳版（en/ zh-Hant/ zh/）は、頁のファイル名が同じ。メニューは、いま見ている頁の別言語版へ移るだけ
   - 切替先にできる言語は、頁の <meta name="ukadoc-langs" content="ja,en,..."> による（ビルドが i18n/ にある言語を書く）。日本語だけなら何も出さない
   - 翻訳版の頁には、機械翻訳である旨と、日本語の原文へのリンクの帯を、頁の頭に出す
   翻訳は LLM による機械翻訳（scripts/translate.py）。読めればよい水準で、仕様の判断には原文を見ること */
(function () {
  'use strict';

  var LANGS = [
    { code: 'ja', label: '日本語' },
    { code: 'en', label: 'English' },
    { code: 'zh-Hant', label: '繁體中文' },
    { code: 'zh', label: '简体中文' }
  ];
  var NOTICE = {
    en: { text: 'This page is a machine translation. For specification decisions, refer to the Japanese original.', link: 'View the Japanese original' },
    'zh-Hant': { text: '本頁為機器翻譯。涉及規格的判斷，請以日文原文為準。', link: '查看日文原文' },
    zh: { text: '本页为机器翻译。涉及规范的判断，请以日文原文为准。', link: '查看日文原文' }
  };

  var meta = document.querySelector('meta[name="ukadoc-langs"]');
  var available = meta ? meta.getAttribute('content').split(',') : ['ja'];
  var cur = document.documentElement.lang || 'ja';
  if (available.length < 2) return;

  // いまの頁のファイル名（ディレクトリの頁は空）。翻訳版は 1 つ下の階層にあるので、日本語版は ../、ほかの翻訳版は ../<言語>/ になる
  var file = location.pathname.slice(location.pathname.lastIndexOf('/') + 1);
  function hrefOf(code) {
    return (cur === 'ja' ? '' : '../') + (code === 'ja' ? '' : code + '/') + file + location.search + location.hash;
  }

  function buildNotice() {
    var n = NOTICE[cur];
    if (!n) return;
    var bar = document.createElement('div');
    bar.className = 'ukadoc-mt-notice';
    bar.setAttribute('role', 'note');
    var a = document.createElement('a');
    a.href = hrefOf('ja');
    a.textContent = n.link;
    bar.appendChild(document.createTextNode(n.text + ' '));
    bar.appendChild(a);
    document.body.insertBefore(bar, document.body.firstChild);
  }

  function buildMenu() {
    var wrap = document.createElement('div');
    wrap.className = 'ukadoc-translate';
    wrap.setAttribute('translate', 'no');

    var button = document.createElement('button');
    button.type = 'button';
    button.className = 'ukadoc-translate__button' + (cur !== 'ja' ? ' ukadoc-translate__button--on' : '');
    button.title = 'Language / 言語';
    button.setAttribute('aria-label', 'Language / 言語');
    button.setAttribute('aria-haspopup', 'true');
    button.setAttribute('aria-expanded', 'false');
    button.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12.87 15.07l-2.54-2.51.03-.03A17.5 17.5 0 0 0 14.07 6H17V4h-7V2H8v2H1v2h11.17C11.5 7.92 10.44 9.75 9 11.35 8.07 10.32 7.3 9.19 6.69 8h-2c.73 1.63 1.73 3.17 2.98 4.56l-5.09 5.02L4 19l5-5 3.11 3.11zM18.5 10h-2L12 22h2l1.12-3h4.75L21 22h2zm-2.62 7 1.62-4.33L19.12 17z"/></svg>';

    var menu = document.createElement('div');
    menu.className = 'ukadoc-translate__menu';
    menu.hidden = true;
    var list = document.createElement('ul');
    LANGS.forEach(function (l) {
      if (available.indexOf(l.code) < 0) return;
      var li = document.createElement('li');
      var b = document.createElement('button');
      b.type = 'button';
      b.dataset.lang = l.code;
      b.lang = l.code;
      b.textContent = l.label;
      b.setAttribute('aria-pressed', String(l.code === cur));
      li.appendChild(b);
      list.appendChild(li);
    });
    menu.appendChild(list);
    if (cur !== 'ja') {
      var status = document.createElement('p');
      status.className = 'ukadoc-translate__status';
      status.textContent = 'Machine translation / 機械翻訳';
      menu.appendChild(status);
    }
    wrap.appendChild(button);
    wrap.appendChild(menu);

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
      if (b.dataset.lang === cur) { toggle(false); return; }
      location.href = hrefOf(b.dataset.lang);
    });
    document.body.appendChild(wrap);
  }

  buildMenu();
  buildNotice();
})();
