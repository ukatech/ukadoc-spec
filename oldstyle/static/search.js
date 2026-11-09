/* サイト内検索。search-index.js（ビルド時に作る。大きいので、使うときに読み込む）の UKADOC_INDEX を、
   空白で区切った語の AND で部分一致検索する。旧版にあった外部の Google 検索の代わり。
   使われ方は 3 つ（全部この 1 ファイル）
   - 検索頁（search.html）: 入力欄の下に、ヒットした全項目を並べる
   - 枠の頁（上の帯 header#navigation に form.internal-search のある頁）: 上の帯の入力欄（.search-field）の下にドロップダウンを出す
   - 仕様書側（list / spec の頁）: 右上（翻訳ボタンの左横）に入力欄を固定で置き、その下にドロップダウンを出す
   打ち込みが止まってから DEBOUNCE ミリ秒たつと検索する。↑↓で選び、Enter で開く（選んでいなければ検索頁へ）。Esc で閉じる */
(function () {
  'use strict';

  var DEBOUNCE = 250;      // 打ち込みが止まってから検索するまでの待ち（ミリ秒）
  var MAX_ITEMS = 8;       // ドロップダウンに並べる件数
  var MAX_PAGE = 100;      // 検索頁に並べる件数

  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function norm(s) { return s.toLowerCase(); }
  function searchUrl(q) { return 'search.html' + (q ? '?q=' + encodeURIComponent(q) : ''); }

  /* ---------------------------------------------------------------- 索引と検索 */

  var docs = null;
  var waiting = null;      // 索引の読み込み中に溜まった呼び出し

  function ensureIndex(cb) {
    if (docs) { cb(); return; }
    if (waiting) { waiting.push(cb); return; }
    waiting = [cb];
    function done(list) {
      docs = (list || []).map(function (e) {
        return { page: e[0], title: e[1], url: e[2], text: e[3], nt: norm(e[1]), nx: norm(e[3]) };
      });
      var calls = waiting;
      waiting = null;
      calls.forEach(function (f) { f(); });
    }
    if (window.UKADOC_INDEX) { done(window.UKADOC_INDEX); return; }
    var s = document.createElement('script');
    s.src = 'search-index.js';
    s.onload = function () { done(window.UKADOC_INDEX); };
    s.onerror = function () { done([]); };
    document.head.appendChild(s);
  }

  function snippet(d, terms, len) {
    var pos = -1;
    terms.forEach(function (t) { var p = d.nx.indexOf(t); if (p >= 0 && (pos < 0 || p < pos)) pos = p; });
    var start = Math.max(0, pos - 30);
    var html = esc(d.text.slice(start, start + len));
    terms.forEach(function (t) {
      if (!t) return;
      var re = new RegExp(esc(t).replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'gi');
      html = html.replace(re, function (m) { return '<mark>' + m + '</mark>'; });
    });
    return (start > 0 ? '…' : '') + html + (start + len < d.text.length ? '…' : '');
  }

  function find(q) {
    var terms = norm(q).split(/\s+/).filter(Boolean);
    var hits = [];
    if (!terms.length) return { terms: terms, hits: hits };
    docs.forEach(function (d) {
      var score = 0;
      for (var i = 0; i < terms.length; i++) {
        var inTitle = d.nt.indexOf(terms[i]) >= 0, inText = d.nx.indexOf(terms[i]) >= 0;
        if (!inTitle && !inText) return;
        score += inTitle ? (d.nt === terms[i] ? 100 : 10) : 1;
      }
      hits.push({ d: d, score: score });
    });
    hits.sort(function (a, b) { return b.score - a.score; });
    return { terms: terms, hits: hits };
  }

  /* ---------------------------------------------------------------- 検索頁（search.html） */

  function resultsPage() {
    var input = document.getElementById('search-q');
    var out = document.getElementById('search-results');
    var form = document.getElementById('search-form');
    if (!input || !out || !form) return;

    function run(q) {
      ensureIndex(function () {
        var r = find(q);
        if (!r.terms.length) { out.innerHTML = ''; return; }
        var shown = r.hits.slice(0, MAX_PAGE);
        var html = '<p>' + r.hits.length + ' 件' + (r.hits.length > shown.length ? '（上位 ' + shown.length + ' 件を表示）' : '') + '</p><ul class="search-hits">';
        shown.forEach(function (h) {
          html += '<li><a href="' + esc(h.d.url) + '">' + esc(h.d.title) + '</a> <span class="search-page">' + esc(h.d.page) + '</span><br>' + snippet(h.d, r.terms, 140) + '</li>';
        });
        out.innerHTML = html + '</ul>';
      });
    }

    var m = /[?&]q=([^&]*)/.exec(location.search);
    if (m) { input.value = decodeURIComponent(m[1].replace(/\+/g, ' ')); run(input.value); }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      run(input.value);
      history.replaceState(null, '', '?q=' + encodeURIComponent(input.value));
    });
  }

  /* ---------------------------------------------------------------- ドロップダウン（枠の頁・仕様書側で使う） */

  function Dropdown(mount, place) {
    var self = this;
    var el = document.createElement('div');
    el.className = 'ukadoc-search__dropdown';
    el.id = 'ukadoc-search-dropdown';
    el.setAttribute('role', 'listbox');
    el.setAttribute('translate', 'no');
    el.hidden = true;
    // 項目を押してもフォーカス（入力欄）を動かさない。動くと、入力欄の blur で閉じて、押した項目に届かない
    el.addEventListener('mousedown', function (e) { e.preventDefault(); });
    el.addEventListener('mouseover', function (e) {
      var a = e.target.closest('a[data-i]');
      if (a) self.setActive(+a.dataset.i);
    });
    mount(el);

    self.el = el;
    self.q = '';
    self.active = -1;
    self.count = 0;          // 選べるものの数（ヒットした項目 + 末尾の「すべての結果」）
    self.timer = null;
    self.onchange = null;    // 開閉が変わったとき（aria-expanded の更新用）

    self.items = function () { return el.querySelectorAll('a[data-i]'); };

    self.setActive = function (i) {
      self.active = i;
      Array.prototype.forEach.call(self.items(), function (a) {
        var on = +a.dataset.i === i;
        a.classList.toggle('is-active', on);
        a.setAttribute('aria-selected', String(on));
        if (on) a.scrollIntoView({ block: 'nearest' });
      });
    };

    self.hide = function () {
      clearTimeout(self.timer);
      self.q = '';
      self.active = -1;
      if (!el.hidden) { el.hidden = true; if (self.onchange) self.onchange(false); }
    };

    function render() {
      var r = find(self.q);
      var shown = r.hits.slice(0, MAX_ITEMS);
      var html = '';
      shown.forEach(function (h, i) {
        html += '<a class="ukadoc-search__item" role="option" data-i="' + i + '" href="' + esc(h.d.url) + '"><span class="ukadoc-search__title">' + esc(h.d.title) +
          '</span> <span class="ukadoc-search__page">' + esc(h.d.page) + '</span><span class="ukadoc-search__snippet">' + snippet(h.d, r.terms, 90) + '</span></a>';
      });
      if (!shown.length) html += '<p class="ukadoc-search__empty">見つからなかった。</p>';
      html += '<a class="ukadoc-search__all" role="option" data-i="' + shown.length + '" href="' + esc(searchUrl(self.q)) + '">' +
        (shown.length ? 'すべての結果を見る（' + r.hits.length + ' 件）' : '検索頁で探す') + '</a>';
      el.innerHTML = html;
      self.count = shown.length + 1;
      self.active = -1;
      place(el);
      if (el.hidden) { el.hidden = false; if (self.onchange) self.onchange(true); }
    }

    // 打ち込みが止まってから検索する。空なら閉じる
    self.query = function (q) {
      clearTimeout(self.timer);
      q = q.trim();
      if (!q) { self.hide(); return; }
      self.timer = setTimeout(function () {
        ensureIndex(function () {
          if (q === self.q) return;
          self.q = q;
          render();
        });
      }, DEBOUNCE);
    };

    self.move = function (delta) {
      if (el.hidden) return;
      self.setActive(Math.max(-1, Math.min(self.count - 1, self.active + delta)));
    };

    // Enter: 選んでいる項目があればそこへ、なければ検索頁へ
    self.enter = function (q) {
      var a = self.active >= 0 && !el.hidden ? el.querySelector('a[data-i="' + self.active + '"]') : null;
      location.href = a ? a.getAttribute('href') : searchUrl(q.trim());
    };
  }

  // 入力欄のキー操作を Dropdown に結びつける共通の処理。send(type, extra) が各方式の受け渡し
  function bindInput(input, send) {
    var composing = false;
    function fire() { send('input', { q: input.value }); }
    input.addEventListener('compositionstart', function () { composing = true; });
    input.addEventListener('compositionend', function () { composing = false; fire(); });
    input.addEventListener('input', function () { if (!composing) fire(); });
    input.addEventListener('focus', function () { if (input.value.trim()) fire(); });
    input.addEventListener('blur', function () { send('close'); });
    input.addEventListener('keydown', function (e) {
      if (e.isComposing) return;
      if (e.key === 'ArrowDown' || e.key === 'ArrowUp') { e.preventDefault(); send('move', { delta: e.key === 'ArrowDown' ? 1 : -1 }); }
      else if (e.key === 'Enter') { e.preventDefault(); send('enter', { q: input.value }); }
      else if (e.key === 'Escape') { send('close'); }
    });
  }

  function handle(dd, type, d) {
    if (type === 'input') dd.query(d.q || '');
    else if (type === 'move') dd.move(d.delta);
    else if (type === 'enter') dd.enter(d.q || '');
    else if (type === 'close') dd.hide();
  }

  // 枠の頁: 上の帯の入力欄（.search-field）の真下にドロップダウンを出す
  function inlineMode(input) {
    var field = input.parentNode;
    var form = input.form;
    input.setAttribute('role', 'combobox');
    input.setAttribute('aria-autocomplete', 'list');
    input.setAttribute('aria-expanded', 'false');
    input.setAttribute('aria-controls', 'ukadoc-search-dropdown');
    input.setAttribute('autocomplete', 'off');
    var dd = new Dropdown(function (el) { field.appendChild(el); }, function () {});
    dd.onchange = function (open) { input.setAttribute('aria-expanded', String(open)); };
    bindInput(input, function (type, d) { handle(dd, type, d || {}); });
    form.addEventListener('submit', function (e) { e.preventDefault(); dd.enter(input.value); });
    document.addEventListener('mousedown', function (e) { if (!field.contains(e.target)) dd.hide(); });
  }

  // 仕様書側: 右上（翻訳ボタンの左横）に入力欄を固定で置く
  function floatMode() {
    var wrap = document.createElement('div');
    wrap.className = 'ukadoc-search';
    wrap.setAttribute('translate', 'no');
    var input = document.createElement('input');
    input.type = 'text';
    input.className = 'ukadoc-search__input';
    input.placeholder = 'ukadoc内検索';
    input.title = 'ukadoc内検索';
    input.setAttribute('aria-label', 'ukadoc内検索');
    input.setAttribute('role', 'combobox');
    input.setAttribute('aria-autocomplete', 'list');
    input.setAttribute('aria-expanded', 'false');
    input.setAttribute('aria-controls', 'ukadoc-search-dropdown');
    input.setAttribute('autocomplete', 'off');
    wrap.appendChild(input);
    var icon = document.createElement('span');
    icon.className = 'ukadoc-search__icon';
    icon.setAttribute('aria-hidden', 'true');
    icon.textContent = '🔍';
    wrap.appendChild(icon);
    var dd = new Dropdown(function (el) { wrap.appendChild(el); }, function () {});
    dd.onchange = function (open) { input.setAttribute('aria-expanded', String(open)); };
    bindInput(input, function (type, d) { handle(dd, type, d || {}); });
    document.addEventListener('mousedown', function (e) { if (!wrap.contains(e.target)) dd.hide(); });
    document.body.appendChild(wrap);
  }

  /* ---------------------------------------------------------------- 起動 */

  var navInput = document.querySelector('form.internal-search input[name="q"]');
  resultsPage();
  if (navInput) inlineMode(navInput);
  else floatMode();
})();
