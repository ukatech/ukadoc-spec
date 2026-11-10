# char\*.recommendsites

**カテゴリ:** ghost 資訊

`\p[*]`側的推薦清單。<br />
值<br />
以以下格式傳回：<br />
項目名稱1\[位元組值1\]url1\[位元組值1\]橫幅圖片路徑1\[位元組值1\]選取時的對話腳本1\[位元組值2\]項目名稱2\[位元組值1\]...<br />
但SHIORI可能會在內部轉換成此格式，詳情請參閱各SHIORI的說明。<br />
對話腳本部分不是單純的文字，而是Sakura Script。<br />
url部分可改為以script:開頭的描述，此時會執行該腳本（也可以使用[`\![raise]`](../../sakura-script/event/bang-raise-r0-r1-r2.md)等）。

**対応:** SSP
