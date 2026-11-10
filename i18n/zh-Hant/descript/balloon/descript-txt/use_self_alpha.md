# use_self_alpha,值

**カテゴリ:** descript.txt

指定1或true時，具有透明度的影像（含 alpha channel 的 PNG）以及有 .pna 的 surface，會參照 alpha channel 並將其用作透明度。若兩者皆不存在，則會沿用原有行為，將影像左上角的顏色視為色鍵。<br />
指定full時，除了上述行為外，也會將所有沒有 alpha channel 的 surface 視為不透明（不使用左上角色鍵透明效果）。<br />
請注意，輸入框類型的 balloon 必須同時將 use_input_alpha 設為1，才能半透明化。<br />
此設定只能套用至整個 balloon，不能覆寫。

**既定値:** 0

**対応:** SSP
