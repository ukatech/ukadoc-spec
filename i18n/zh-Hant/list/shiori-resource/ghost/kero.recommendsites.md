# kero.recommendsites

**カテゴリ:** ghost 資訊

搭檔側的推薦清單。<br />
值<br />
以項目名稱1\[位元組值1\]url1\[位元組值1\]橫幅圖片路徑1\[位元組值1\]選取時的對話腳本1\[位元組值2\]項目名稱2\[位元組值1\]...<br />
這種格式回傳。<br />
但有時SHIORI會在內部轉換為此格式，詳細資訊請參閱各SHIORI的說明。<br />
對話腳本部分不是單純的字串，而是Sakura Script。<br />
url部分可以改為以script:開頭的描述，藉此執行該腳本（也可使用[`\![raise]`](../../sakura-script/event/bang-raise-r0-r1-r2.md)等）。

**対応:** Materia / SSP / CROW / Ninix
