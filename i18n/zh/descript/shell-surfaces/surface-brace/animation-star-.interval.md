# animation\*.interval,间隔

**カテゴリ:** surface块

定义动画开始的时机（周期）。<br />
间隔请参见下文的[动画间隔](h-animationinterval/index.md)。仅SSP支持用+分隔并列，从而组合指定。<br />
\*部分（animationID）为任意数字。在该scope（`\0`、`\1`、...）的所有surface中，相同ID的动画应具有相同含义（例如“眨眼”“口型同步”“同一服装的dressup”）。<br />
interval定义表示该ID动画定义整体的起点，必须始终写在这一系列animation定义的开头。<br />
动画的叠加方式与ID顺序之间的关系请参见[animation-sort](../descript-brace/animation-sort.md)。<br />
[旧定义](caption_seriko-redefine.md)：\*interval,间隔

**既定値:** 无效果

**対応:** Materia / SSP / CROW
