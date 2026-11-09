/* サイト内検索。search-index.js（ビルド時に作る）の UKADOC_INDEX を、空白で区切った語の AND で部分一致検索する。
   旧版にあった外部の Google 検索の代わり */
(function () {
  'use strict';
  var input = document.getElementById('search-q');
  var out = document.getElementById('search-results');
  var form = document.getElementById('search-form');
  if (!input || !out || !window.UKADOC_INDEX) return;

  function esc(s) { return s.replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function norm(s) { return s.toLowerCase(); }

  var docs = window.UKADOC_INDEX.map(function (e) {
    return { page: e[0], title: e[1], url: e[2], text: e[3], nt: norm(e[1]), nx: norm(e[3]) };
  });

  function snippet(d, terms) {
    var pos = -1;
    terms.forEach(function (t) { var p = d.nx.indexOf(t); if (p >= 0 && (pos < 0 || p < pos)) pos = p; });
    var start = Math.max(0, pos - 30);
    var s = d.text.slice(start, start + 140);
    var html = esc(s);
    terms.forEach(function (t) {
      if (!t) return;
      var re = new RegExp(esc(t).replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'gi');
      html = html.replace(re, function (m) { return '<mark>' + m + '</mark>'; });
    });
    return (start > 0 ? '…' : '') + html + (start + 140 < d.text.length ? '…' : '');
  }

  function run(q) {
    var terms = norm(q).split(/\s+/).filter(Boolean);
    if (!terms.length) { out.innerHTML = ''; return; }
    var hits = [];
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
    var shown = hits.slice(0, 100);
    var html = '<p>' + hits.length + ' 件' + (hits.length > shown.length ? '（上位 ' + shown.length + ' 件を表示）' : '') + '</p><ul class="search-hits">';
    shown.forEach(function (h) {
      html += '<li><a href="' + esc(h.d.url) + '" target="_top">' + esc(h.d.title) + '</a> <span class="search-page">' + esc(h.d.page) + '</span><br>' + snippet(h.d, terms) + '</li>';
    });
    out.innerHTML = html + '</ul>';
  }

  var m = /[?&]q=([^&]*)/.exec(location.search);
  if (m) { input.value = decodeURIComponent(m[1].replace(/\+/g, ' ')); run(input.value); }
  form.addEventListener('submit', function (e) { e.preventDefault(); run(input.value); history.replaceState(null, '', '?q=' + encodeURIComponent(input.value)); });
})();
