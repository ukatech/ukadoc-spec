// site-look-sakura-script-highlight: さくらスクリプトの記述例のタグと環境変数を span で包み、誤りを示す（字は変えない）
(() => {
  const NUMBERED = { s: /[0-9]/, p: /[0-9]/, b: /[0-9]/, w: /[1-9]/ };
  const ENV = /%(?:\*|m\?|[A-Za-z_][A-Za-z0-9_]*)/y;
  const WHY = {
    args: '閉じる ] が無い（引数の " が閉じていないときも）',
    enclosure: '閉じる囲みの印が無い',
    backslash: '\\ の後にタグの名前が無い（\\ を字として見せるなら \\\\ と書く）',
  };

  // t[i] の [ に対になる ] の次の位置（閉じなければ -1）。\] と、引数の頭からの "…"（"" は " 1 字）の中の ] では終えない
  const argsEnd = (t, i) => {
    for (let j = i + 1, head = true; j < t.length; ) {
      if (head && t[j] === '"') {
        for (j++; j < t.length && !(t[j] === '"' && t[j + 1] !== '"'); j += t[j] === '"' ? 2 : 1);
        if (j >= t.length) return -1;
        j++;
        head = false;
        continue;
      }
      if (t[j] === ']') return j + 1;
      head = t[j] === ',';
      j += t[j] === '\\' && t[j + 1] === ']' ? 2 : 1;
    }
    return -1;
  };

  // [種類, 始め, 終わり, わけ] の並び。誤りはブロックの終わりまでとし、そこで読むのをやめる（救済しない）
  const tokens = (t) => {
    const out = [];
    const fail = (i, why) => (out.push(['error', i, t.length, why]), out);
    for (let i = 0; i < t.length; ) {
      if (t[i] === '\\') {
        if (t[i + 1] === '\\' || t[i + 1] === '%') { i += 2; continue; }
        let k = i + 1;
        while (t[k] === '_') k++;
        if (k >= t.length || t[k] === '\n' || t[k] === '\r') return fail(i, WHY.backslash);
        let e = k + (t.codePointAt(k) > 0xffff ? 2 : 1);
        const name = t.slice(i + 1, e);
        if (name === '_?' || name === '_!') {
          const close = t.indexOf('\\' + name, e);
          if (close < 0) return fail(i, WHY.enclosure);
          out.push(['tag', i, e], ['tag', close, close + 3]);
          i = close + 3;
          continue;
        }
        if (NUMBERED[name]?.test(t[e] ?? '')) e++;
        else if (t[e] === '[' && (e = argsEnd(t, e)) < 0) return fail(i, WHY.args);
        out.push(['tag', i, e]);
        i = e;
      } else if (t[i] === '%') {
        let e = -1;
        if (t.startsWith('%property[', i)) {
          if ((e = argsEnd(t, i + 9)) < 0) return fail(i, WHY.args);
        } else {
          ENV.lastIndex = i;
          if (ENV.exec(t)) e = ENV.lastIndex;
        }
        if (e < 0) { i++; continue; }
        out.push(['env', i, e]);
        i = e;
      } else i++;
    }
    return out;
  };

  // 警告に添える場所（記述例の前の見出しの id）
  const where = (code) => {
    for (let el = code.closest('pre'); el; el = el.previousElementSibling) {
      if (/^H[1-6]$/.test(el.tagName) && el.id) return `${location.pathname}#${el.id}`;
    }
    return location.pathname;
  };

  for (const code of document.querySelectorAll('code.language-sakurascript, code.language-ss')) {
    code.classList.add('language-sakurascript');
    if (code.children.length) { console.warn('sakurascript: 要素の入ったブロックには色を付けない', where(code)); continue; }
    const t = code.textContent;
    const nodes = [];
    let last = 0;
    for (const [kind, s, e, why] of tokens(t)) {
      const span = document.createElement('span');
      span.className = `sakurascript-${kind}`;
      span.textContent = t.slice(s, e);
      if (why) {
        span.title = why;
        console.warn(`sakurascript: ${why}`, where(code), t.slice(s, s + 40));
      }
      nodes.push(t.slice(last, s), span);
      last = e;
    }
    code.replaceChildren(...nodes, t.slice(last));
    if (code.textContent !== t) { code.textContent = t; console.warn('sakurascript: 字が変わるので包まずに戻した', where(code)); }
  }
})();
