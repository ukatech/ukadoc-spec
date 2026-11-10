# 动画（SERIKO）

## 概要

伺か（Ukagaka）的 shell 具有动画功能。通过连续绘制静止图像帧来实现类似视频的表现。

动画针对各个 surface 进行设置。动画各帧使用的图像也同样是其他 surface。此时，即使被引用为帧的 surface 还定义了动画，通常也会忽略该动画（但仅限 SSP，存在一种称为多重 dressup 的机制。参见[dressup](introduction_mayuna.md)一节）。

在各个 surface 的设置中，需要定义动画本身何时开始，以及每帧使用哪个 surface、以何种方式和时间间隔绘制等内容。

另外，surfaces.txt 中有关动画的一系列规范称为 SERIKO。

## 基本格式与示例

```
surface0
{
// 瞬き
animation0.interval,rarely
animation0.pattern0,overlay,101,700,200,100
animation0.pattern1,overlay,102,700,200,100
animation0.pattern2,overlay,101,700,200,100
animation0.pattern3,overlay,-1,700,0,0

// トークに合わせて口を動かす
animation10.interval,talk,2
animation10.pattern0,overlay,200,700,200,120
animation10.pattern1,overlay,201,700,200,120
animation10.pattern2,overlay,202,700,200,120
animation10.pattern3,overlay,-1,700,0,0
}
```

例如，surfaces.txt 中的动画定义如下。

上例为 surface0 定义了「眨眼」和「配合对话活动嘴部」这两个动画。

所有动画定义都包含 interval 定义和 pattern 定义。此外还有选项定义，以及 SSP 中专用的动画触摸判定定义；但这些都可以省略，而 interval 定义不能省略，并且必须出现在一系列动画定义的开头。pattern 定义也至少需要有一个。

[interval 定义](animation-star-.interval.md)用于设置动画何时播放。上例中出现了「rarely」「talk」「never」三种指定。详情请参见[动画间隔一节](h-animationinterval/introduction_animationinterval.md)，大意是「眨眼」动画会偶尔播放，而「配合对话活动嘴部」动画会在角色每说两个字符时播放。

[pattern 定义](animation-star-.pattern-star.md)用于设置动画的各个「帧」。其中设置帧的绘制方法（参见[绘制方法](h-drowmethod/introduction_drawmethod.md)一节）、显示前的等待时间，以及相对于下方帧绘制时的偏移量。按需要准备相应数量的 pattern 定义即可。pattern\*中的\*是从0开始的连续编号。

## 各动画之间的关系

所有动画都具有 ID（具体指定方式请参见animation\*.interval一节）。

同一个 surface 内不允许有重复的 ID，而不同 surface 上具有相同 ID 的动画则应表示相同的含义。例如，假设有角色面朝正面的 surface0 和面朝侧面的 surface1，并且两者都设置了「眨眼」动画。此时，由于角色姿势不同，实际用于表现眨眼的帧图像理应不同，但两个 surface 仍应使用相同的动画 ID。特别是在下文所述的[dressup](introduction_mayuna.md)中，必须将 ID 与含义关联起来。

原则上，所有不同的动画彼此独立，并且异步开始和结束。<br />
例如，眨眼动画和配合对话活动嘴部的动画，应当互不在意对方是否正在运行而开始和结束；只要它们被定义为 ID 不同的动画，实际也会如此运行。

另一方面，也提供了一种机制，可以通过 start 或 alternativestart 等用于执行其他动画的特殊绘制方法，将动画本身作为触发器来执行其他动画。<br />
此外，还可以通过指定 exclusive 选项来执行互斥动画。
