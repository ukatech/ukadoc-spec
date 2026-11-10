# animation\*.option,shared-index

**カテゴリ:** surface块

跨越`\s`标签切换基底 surface 时，从中途继续执行相同 ID 的动画。<br />
具体来说，假设执行`\s`前动画已执行到pattern4，那么执行`\s`后也会从pattern4重新开始。<br />
`\s`切换源和切换目标两侧都必须指定此项，只在其中一侧指定会导致动画重置。<br />
此外，如果在切换目标的动画中找不到pattern ID，也会重置。

**既定値:** 无特殊行为

**対応:** SSP 2.6.02
