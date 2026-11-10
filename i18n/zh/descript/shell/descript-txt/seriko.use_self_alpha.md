# seriko.use_self_alpha,值

**カテゴリ:** descript.txt

指定 1 或 true 时，对于带有透明度的图像（带 alpha 通道的 PNG）以及带有 .pna 的图像，会参考 alpha 通道并将其用作透明度。如果既没有 alpha 通道也没有 .pna，则沿用传统行为，以图像左上角的颜色作为键色。<br />
指定 full 时，除此之外还会将所有不带 alpha 通道的图像视为不透明（不使用左上角键色透明效果）。

**既定値:** 0

**対応:** SSP
