# shiori.escape_unknown,0/1

**カテゴリ:** descript.txt

與 SHIORI 通訊時，若有無法轉換為指定字元編碼的 Unicode 字元，便使用特殊跳脫方式，盡可能避免完全無法辨識為文字的情況。<br />
具體而言，會將無法轉換的字串改寫成?escape!unicode\[0xABCD\]之類的特殊形式後傳給 SHIORI；若 SHIORI 以相同形式傳回，則會適當地重新轉換。

**既定値:** 0（false）

**対応:** SSP 2.6.89
