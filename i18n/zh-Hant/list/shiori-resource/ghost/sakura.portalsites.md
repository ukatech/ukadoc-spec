# sakura.portalsites

**カテゴリ:** ghost 資訊

本體側的入口清單。<br />
值會以<br />
項目名稱1\[位元組值1\]url1\[位元組值1\]橫幅圖片路徑1\[位元組值1\]選取時的對話腳本1\[位元組值2\]項目名稱2\[位元組值1\]...<br />
的格式回傳。<br />
不過，SHIORI 可能會在內部轉換成此格式，詳情請參閱各 SHIORI 的說明。<br />
對話腳本部分不是單純的字串，而是 Sakura Script。<br />
在 url 部分以 script: 開頭的描述取代 url，即可執行該腳本（也可使用[`\![raise]`](../../sakura-script/event/bang-raise-r0-r1-r2.md)等）。

**対応:** Materia / SSP / CROW / Ninix
