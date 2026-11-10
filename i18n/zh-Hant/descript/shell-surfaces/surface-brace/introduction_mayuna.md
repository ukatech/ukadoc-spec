# Dressup (MAYUNA)

## Overview

A shell in 伺か (Ukagaka) has a mechanism called dressup. It allows parts such as clothing to be shown or hidden, or their types to be switched, within a single shell.

Dressup in a 伺か (Ukagaka) shell is treated as a type of animation.<br />
However, unlike other animations, it is not played frame by frame. Instead, all frames (patterns) and the base surface are composited immediately when the animation starts, and are then treated as a still image (so the wait parameter in pattern definitions is ignored).<br />
This behavior, where the drawing acts as though it were integrated with the base surface, is well suited to representing things such as clothing.

The start and end of dressup animations are mainly controlled by toggling them in the dressup menu of the owner-draw menu. In SSP, the ghost can also control them using the Sakura Script [`\![bind]`](../../../list/sakura-script/surface/bang-bind.md) tag.<br />
The owner-draw menu settings are configured in [descript.txt](../../shell/index.md), not in surfaces.txt; see that page.

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

For example, dressup can be defined in surfaces.txt as shown above.

The example defines two dressups, “Clothing 1” and “Clothing 2,” for surface0.

As with ordinary animation definitions, interval and pattern definitions are required. Specifying bind in the interval definition indicates that the animation is a dressup definition.

For an animation, a pattern definition is provided for each frame. For dressup, however, the image is static, so only as many parts as needed are composited rather than frames. If the dressup consists of just one part, as in the example, it needs only one pattern line. In addition, because each part is composited immediately for dressup, the wait parameter is ignored.

The drawing methods for pattern definitions are described below.

## Available drawing methods

In MATERIA (the original 伺か), four methods were available for dressup: “bind,” “add,” “reduce,” and “insert.” Of these, bind is the old specification, and add is its superset.

In SSP, some of the methods provided as ordinary animation drawing methods can also be used for dressup.

For details about drawing methods and other features available for dressup, see the [Drawing methods](h-drowmethod/introduction_drawmethod.md) section.

## bind in combined interval specifications

As described in the [Animation intervals](h-animationinterval/introduction_animationinterval.md) section, SSP allows interval specifications to be combined.

When an animation includes bind in a combined specification, it loses the static-image behavior it would have with bind alone (the wait parameter in pattern definitions is no longer ignored). However, the animation's lifetime does not change. For example, with a combination such as bind+runonce, the display at the point when all patterns have finished drawing continues to be shown until the base surface changes or the dressup state changes.

Therefore, when using a combined interval specification that includes bind, do not end the animation on the last line of the pattern definition; instead, composite the drawing that should remain as a still image.

## Nested dressup definitions (SSP only)

Normally, if the surface referenced by an animation frame has an animation defined for it, that animation is ignored.

In SSP, however, animations whose interval is bind (that is, dressups) are not ignored and are applied.

This makes it possible to define animations on the animation-frame side that respond to dressup, for animations structured to be affected by dressup.

Nested dressup is also possible, but circular references are ignored.
