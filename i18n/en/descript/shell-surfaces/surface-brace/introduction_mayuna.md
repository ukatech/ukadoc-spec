# Dressup (MAYUNA)

## Overview

Ukagaka shells have a mechanism called dressup. It allows parts such as outfits to be shown or hidden, or their types to be switched, within a single shell.

Dressup in Ukagaka shells is treated as a type of animation.<br />
However, unlike other animations, it is not played frame by frame. At the start of the animation, all frames (patterns) and the base surface are composited immediately, after which they are treated as a still image. (Therefore, the wait parameter in pattern definitions is ignored.)<br />
This property, where “the drawing behaves as if it were integrated with the base surface,” is well suited to representing things such as clothing.

The start and end of dressup animations are controlled mainly by switching them through the dressup menu in the owner draw menu. In SSP, control from the ghost is also possible using the Sakura Script [`\![bind]`](../../../list/sakura-script/surface/bang-bind.md) tag.<br />
The owner draw menu settings are configured in [descript.txt](../../shell/index.md), not surfaces.txt; see that page.

The specifications for a series of animations in surfaces.txt are called MAYUNA.

## Basic syntax and examples

```
surface0
{
// 服1の定義　アニメーションIDは0
animation0.interval,bind
animation0.pattern0,add,500,0,50,100

// 服2の定義　アニメーションIDは1
animation1.interval,bind
animation1.pattern0,add,501,0,50,100
}

//--- 以下着せ替えパーツ定義 ---
// 服1
surface500
{
element0,overlay,dress1.png,0,0
}

// 服2
surface501
{
element0,overlay,dress2.png,0,0
}
```

For example, dressup definitions in surfaces.txt can look like the above.

The example defines two dressups, “Outfit 1” and “Outfit 2,” for surface0.

As with ordinary animation definitions, interval and pattern definitions are required. Specifying bind in the interval definition indicates that the animation is a dressup definition.

In an animation, pattern definitions are made for each frame. For dressup, however, the specification is a still image, so the required number of parts are composited rather than frames. If the dressup consists of just one part, as in the example, there is only one pattern line. Also, because each part is composited immediately for dressup, the wait parameter is ignored.

The drawing methods for pattern definitions are described below.

## Available drawing methods

In MATERIA (the original Ukagaka), four methods were provided for dressup: “bind,” “add,” “reduce,” and “insert.” Of these, bind is the old specification, and add is its upward-compatible successor.

In SSP, some of the methods provided as ordinary animation drawing methods can also be used for dressup.

For details on the drawing methods and other features available for dressup, see the [Drawing methods](h-drowmethod/introduction_drawmethod.md) section.

## bind in combined interval specifications

In SSP, interval combinations can be specified, as described in the [Animation intervals](h-animationinterval/introduction_animationinterval.md) section.

When bind is included in a combination, the animation loses the still-image property it normally has when bind is used alone (the wait parameter in pattern definitions is no longer ignored). However, the animation's lifetime does not change. For example, with a combination such as bind+runonce, the display after all patterns have been drawn continues until the base surface changes or the dressup state changes.

Therefore, with interval combinations that include bind, the final line of the pattern definition should not end the animation; instead, it should composite the drawing that is to remain as a still image.

## Nested dressup definitions (SSP only)

If an animation frame references a surface that has an animation defined for it, that animation is normally ignored.

In SSP, however, only animations whose interval is bind (that is, dressups) are not ignored and are applied.

This makes it possible to define animations whose structure is affected by dressup, with definitions in the animation frames that respond to the dressup.

Dressups can also be nested, but circular references are ignored.
