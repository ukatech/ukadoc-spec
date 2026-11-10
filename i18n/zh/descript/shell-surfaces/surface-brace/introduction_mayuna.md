# Dressup (MAYUNA)

## Overview

A shell in Ukagaka has a mechanism called dressup. It is used to show or hide parts such as clothing, or switch between their types, within a single shell.

Dressup in Ukagaka shells is considered a type of animation.<br />
However, unlike other animations, it does not play frame by frame. When the animation starts, all frames (patterns) and the base surface are composited immediately and are then treated as a still image (therefore, the wait parameter in pattern definitions is ignored).<br />
This property—where the drawing behaves as though it has become one with the base surface—is well suited to representing things such as clothing.

The start and end of dressup animations are mainly controlled by switching them through the dressup menu in the owner draw menu. In SSP, they can also be controlled by the ghost using the Sakura Script [`\![bind]`](../../../list/sakura-script/surface/bang-bind.md) tag.<br />
The owner draw menu settings are made in [descript.txt](../../shell/index.md), not in surfaces.txt; see that page.

The specifications for the series of animations in surfaces.txt are called MAYUNA.

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

For example, a dressup definition in surfaces.txt can look like the above.

The example defines two dressups, “Clothing 1” and “Clothing 2,” for surface0.

As with ordinary animation definitions, interval and pattern definitions are required. Specifying bind in the interval definition indicates that the animation is a dressup definition.

For an animation, a pattern definition is made for each frame. For dressup, however, the specification is a still image, so the necessary parts are composited rather than individual frames. If, as in the example, a dressup consists of only one part, it needs only one pattern line. Also, because each part is composited immediately in dressup, the wait parameter is ignored.

The drawing methods for pattern definitions are described below.

## Available drawing methods

In MATERIA (the original Ukagaka), four methods provided for dressup were available: “bind,” “add,” “reduce,” and “insert.” Of these, bind is the old specification, and add is its upward-compatible equivalent.

In SSP, some of the methods provided as ordinary animation drawing methods can also be used for dressup.

For details about drawing methods and other options available for dressup, see the [Drawing methods](h-drowmethod/introduction_drawmethod.md) section.

## bind in interval combinations

In SSP, interval combinations can be specified, as mentioned in the [Animation intervals](h-animationinterval/introduction_animationinterval.md) section.

If bind is included in a combination, the animation loses the still-image property it would normally have with bind alone (the wait parameter in pattern definitions is no longer ignored). However, the animation's lifetime does not change. For example, with a combination such as bind+runonce, the display at the point when all patterns have finished drawing continues until the base surface or dressup state changes.

Therefore, with an interval combination that includes bind, the animation should not be ended on the last line of the pattern definition; instead, composite the drawing that should remain as a still image.

## Nested dressup definitions (SSP only)

If an animation frame references a surface that has an animation defined for it, those animations are normally ignored.

In SSP, however, animations whose interval is bind (that is, dressups) are applied rather than ignored.

This makes it possible to define animations that respond to dressup on the animation frame side, for animations whose structure is affected by dressup.

Nested dressups are also possible, but circular references are ignored.
