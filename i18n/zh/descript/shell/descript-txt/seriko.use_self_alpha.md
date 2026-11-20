# seriko.use_self_alpha,值

**カテゴリ:** descript.txt

指定 1 或 true 时，对有透明度的图像（带 alpha 通道的 PNG）以及有 .pna 的图像，使用 alpha 通道作为透明度。若 alpha 通道和 .pna 均不存在，则沿用以图像左上角颜色为键色的传统行为。<br />
指定 full 时，除上述行为外，还将所有没有 alpha 通道的图像视为不透明（不对左上角的键色进行透明处理）。

也可写在 ghost 侧的 descript.txt 中。如果 shell 侧已指定，则优先使用 shell 侧的值；否则使用 ghost 侧的值。

**既定値:** 0

**対応:** SSP
