# blend-screen-fast

**カテゴリ:** surface區塊 \> 繪製方法

依照*基底圖層*的不透明度，以螢幕混合方式疊加*新圖層*。<br />
行為與overlay-fast相同，外形不會改變，但不會覆寫，而是對目前的surface進行螢幕混合處理。<br />
也可用於dressup與element。<br />
名稱中的「fast」是歷史因素所致，並不代表處理速度較快。<br />
建議在shell的descript.txt中設定[`seriko.use_self_alpha,full`](../../../shell/descript-txt/seriko.use_self_alpha.md)。

**対応:** SSP 2.8.36
