# animation\*.option,shared-index

**カテゴリ:** surface brace

切換 `\s` 標籤的 base surface 時，讓相同 ID 的動畫從切換前的進度繼續執行。<br />
具體而言，假設執行 `\s` 前動畫已執行至 pattern4，執行 `\s` 後也會從 pattern4 重新開始。<br />
必須在 `\s` 切換來源和切換目的地兩者都指定；若只在其中一方指定，動畫就會重設。<br />
此外，若在切換目的地的動畫中找不到 pattern ID，也會重設。

**既定値:** 無動作

**対応:** SSP 2.6.02
