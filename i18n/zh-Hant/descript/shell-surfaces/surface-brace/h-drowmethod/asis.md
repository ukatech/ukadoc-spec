# asis

**カテゴリ:** surface brace \> 繪製方法

類似[overlay](overlay.md)，但會忽略*新圖層*的透明設定（透明色，以及設定了 pna 或[seriko.use_self_alpha](../../../shell/descript-txt/seriko.use_self_alpha.md)時的圖像本身 alpha 通道），並將圖層疊加。<br />
也可用於 dressup 或 element。<br />
另外，將以 element 合成的 surface 作為其他 surface 的動畫元件，並使用 asis 方法合成時，其顯示結果未定義；但在 Windows 上，透明區域一般會顯示為黑色（#000000），與圖像原本的透明色無關。

**対応:** SSP
