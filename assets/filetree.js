// site-look-manual-files: ファイル構成の木（+- の行のある言語の印の無いコードブロック）のファイル名を span で包む（字は変えない）
(() => {
  const ROW = /^[\s　]*\+-/;
  const NAME = /[^\s（]+/y;
  const OR = / または /y;
  const FILE = /\.[^.()]+$/;

  // 木の行 line の中のファイル名の [始め, 終わり] の並び。名前は +- の後ろの空白と全角の（ までで、/ と「 または 」で 2 つ目が続く
  const files = (line) => {
    const row = ROW.exec(line);
    if (!row) return [];
    const out = [];
    let i = row[0].length;
    for (;;) {
      NAME.lastIndex = i;
      const m = NAME.exec(line);
      if (!m) return out;
      let s = i;
      for (const part of m[0].split('/')) {
        if (FILE.test(part)) out.push([s, s + part.length]);
        s += part.length + 1;
      }
      i = NAME.lastIndex;
      OR.lastIndex = i;
      if (!OR.test(line)) return out;
      i = OR.lastIndex;
    }
  };

  for (const code of document.querySelectorAll('pre > code:not([class*="language-"])')) {
    const t = code.textContent;
    if (!/^[\s　]*\+-/m.test(t)) continue;
    if (code.children.length) { console.warn('filetree: 要素の入った木には色を付けない', location.pathname); continue; }
    const nodes = [];
    let last = 0, at = 0;
    for (const line of t.split('\n')) {
      for (const [s, e] of files(line)) {
        const span = document.createElement('span');
        span.className = 'filetree-file';
        span.textContent = line.slice(s, e);
        nodes.push(t.slice(last, at + s), span);
        last = at + e;
      }
      at += line.length + 1;
    }
    code.replaceChildren(...nodes, t.slice(last));
    if (code.textContent !== t) { code.textContent = t; console.warn('filetree: 字が変わるので包まずに戻した', location.pathname); }
  }
})();
