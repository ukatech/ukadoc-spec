# blend-linear-light-fast

**カテゴリ:** surface 括號 \> 繪圖方法

依據*基底圖層*的不透明度，以線性光源合成方式疊加*新圖層*。<br />
其行為與 overlay-fast 相同，外形不變，但會對目前的 surface 執行線性光源合成，而非覆寫。<br />
也可用於 dressup 與 element。<br />
名稱中的「fast」源自歷史因素，並不代表處理速度較快。<br />
建議在 shell 的 descript.txt 中設定[`seriko.use_self_alpha,full`](../../../shell/descript-txt/seriko.use_self_alpha.md)。

**対応:** SSP 2.8.40
