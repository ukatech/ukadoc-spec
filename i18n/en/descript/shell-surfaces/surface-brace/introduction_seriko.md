# Animation (SERIKO)

## Overview

Ukagaka shells have animation functionality. This creates video-like effects by continuously drawing frames, which are still images.

Animations are configured for each surface. The images used for each frame of an animation are also surfaces. If a surface referenced as a frame has its own animation definition, that definition is normally ignored (however, SSP alone has a mechanism called multiple dressup. See the [Dressup](introduction_mayuna.md) section).

For each surface, you need to define when the animation itself starts, which surfaces to use for each frame, and how and at what intervals to draw them.

The specifications for animations in surfaces.txt are collectively called SERIKO.

## Basic syntax and examples

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

For example, animation definitions in surfaces.txt can look like the above.

The example defines two animations for surface0: “blinking” and “moving the mouth in time with speech.”

Every animation definition includes an interval definition and pattern definitions. There may also be option definitions and, in SSP, animation-specific touch region definitions. These are optional, but an interval definition is required and must appear at the start of each animation definition. At least one pattern definition is also required.

An [interval definition](animation-star-.interval.md) specifies when an animation plays. The example above uses three values: “rarely,” “talk,” and “never.” For details, see the [Animation Interval](h-animationinterval/introduction_animationinterval.md) section. In brief, the “blinking” animation plays occasionally, while the “moving the mouth in time with speech” animation plays every time the character speaks two characters.

A [pattern definition](animation-star-.pattern-star.md) specifies each “frame” of an animation. It sets the drawing method for that frame (see the [Drawing Methods](h-drowmethod/introduction_drawmethod.md) section), the wait time before it is displayed, and how far to offset it when drawing relative to the frame below it. Provide as many pattern definitions as the frames require. The number represented by \* in pattern\* is a sequential number starting at 0.

## Relationships Between Animations

Every animation is assigned an ID (see the animation\*.interval section for specific instructions).

IDs must be unique within a single surface, and animations with the same ID on different surfaces are expected to have the same meaning. For example, suppose there are surface0, where the character is facing forward, and surface1, where the character is facing sideways, and both have an animation for “blinking.” The images used for the frames that actually depict the blink should differ because the character’s pose differs, but both surfaces should still assign the animation the same ID. This association between ID and meaning is especially essential for the [dressup](introduction_mayuna.md) feature described below.

In general, all distinct animations are independent and start and end asynchronously.<br />
For example, an animation that blinks and one that moves the mouth in sync with speech should start and end without regard to whether the other is moving; indeed, they behave this way as long as they are defined as animations with different IDs.

On the other hand, mechanisms are also provided for using an animation itself as a trigger to run another animation, through special drawing methods for running other animations, such as start and alternativestart.<br />
It is also possible to run exclusive animations by specifying the exclusive option.
