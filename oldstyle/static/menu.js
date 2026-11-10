/* 狭い画面（720px 以下）では、左のメニュー（list / spec の頁は、上の目次の表と左のナビゲーション）を、
   左上のボタンで開閉する引き出し（ドロワー）にする。
   - 引き出しになるのは #ukadoc-drawer（枠の頁は nav.sidebar、list / spec の頁は build.py の drawer() の包み）
   - この script は head で同期に読み込み、<html> に js-drawer を付ける。CSS は js-drawer があるときだけメニューを畳む
     （JavaScript が動かなければ、メニューは従来どおり本文の上に出る）
   - 開いているときは <html> に drawer-open。背景の暗幕・Esc・メニューの中のリンクで閉じる。広い画面に戻ると閉じる */
(function () {
  'use strict';

  var root = document.documentElement;
  root.classList.add('js-drawer');

  var LABELS = {
    ja: ['メニューを開く', 'メニューを閉じる'],
    en: ['Open menu', 'Close menu'],
    'zh-Hant': ['開啟選單', '關閉選單'],
    zh: ['打开菜单', '关闭菜单']
  };
  var ICON_OPEN = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true"><path d="M3 6h18v2H3zm0 5h18v2H3zm0 5h18v2H3z"/></svg>';
  var ICON_CLOSE = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" aria-hidden="true"><path d="M19 6.41 17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z"/></svg>';
  var narrow = window.matchMedia('(max-width: 720px)');

  function init() {
    var drawer = document.getElementById('ukadoc-drawer');
    if (!drawer) return;
    var labels = LABELS[root.lang] || LABELS.ja;

    var button = document.createElement('button');
    button.type = 'button';
    button.className = 'ukadoc-drawer-toggle';
    button.setAttribute('aria-controls', 'ukadoc-drawer');
    button.setAttribute('translate', 'no');
    document.body.appendChild(button);

    var backdrop = document.createElement('div');
    backdrop.className = 'ukadoc-drawer-backdrop';
    document.body.appendChild(backdrop);

    drawer.setAttribute('tabindex', '-1');

    function render(open) {
      button.innerHTML = open ? ICON_CLOSE : ICON_OPEN;
      button.title = labels[open ? 1 : 0];
      button.setAttribute('aria-label', labels[open ? 1 : 0]);
      button.setAttribute('aria-expanded', String(open));
    }

    function setOpen(open, restoreFocus) {
      if (open === root.classList.contains('drawer-open')) return;
      root.classList.toggle('drawer-open', open);
      render(open);
      if (open) {
        drawer.scrollTop = 0;
        drawer.focus({ preventScroll: true });
      } else if (restoreFocus) {
        button.focus({ preventScroll: true });
      }
    }

    render(false);
    button.addEventListener('click', function () {
      setOpen(!root.classList.contains('drawer-open'), false);
    });
    backdrop.addEventListener('click', function () { setOpen(false, true); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && root.classList.contains('drawer-open')) setOpen(false, true);
    });
    // 同じ頁の中の見出しへのリンクでも、選んだら閉じて本文を見せる
    drawer.addEventListener('click', function (e) {
      if (narrow.matches && e.target.closest && e.target.closest('a[href]')) setOpen(false, false);
    });
    var onChange = function () { if (!narrow.matches) setOpen(false, false); };
    if (narrow.addEventListener) narrow.addEventListener('change', onChange);
    else if (narrow.addListener) narrow.addListener(onChange);
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
