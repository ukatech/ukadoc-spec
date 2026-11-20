# seriko.paint_transparent_region_black,数值

**カテゴリ:** descript.txt

设置颜色为图像透明色（图像左上角的颜色），但按透明度值判断并非透明的区域的显示方式。<br />
为 0 时，以指定的透明度显示图像原本的颜色（透明色）。<br />
为 1 时，先用黑色代替图像颜色填充，再以指定的透明度显示。<br />
例如，指定 0 并为图像准备全白的 pna 时，图像将按原样显示，没有透明色。

也可写在 ghost 侧的 descript.txt 中。如果 shell 侧已指定，则优先使用 shell 侧的值；否则使用 ghost 侧的值。

**既定値:** 未指定（使用 pna 作为透明度的图像按 1 处理，[使用图像自身 alpha 通道作为透明度的图像](seriko.use_self_alpha.md)按 0 处理）

**対応:** SSP
