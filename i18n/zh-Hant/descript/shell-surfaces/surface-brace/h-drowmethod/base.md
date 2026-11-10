# base

**カテゴリ:** surface brace \> 繪製方法

使用*新圖層*完全取代[底圖 surface](../caption_basesurface.md)。collision 也會更新為該影格 surface 中定義的內容。<br />
疊加此方法的 pattern，即可透過重新繪製整個 surface 來實現動畫（也就是類似翻頁動畫的效果）。<br />
在指定此繪製方法的 pattern 定義中，XY 座標會被忽略。<br />
在 dressup 和 element 中，base 方法只能用於第一個項目（element0、pattern0）。其他項目會改讀為 overlay。

**対応:** Materia / SSP / CROW
