# Animation interval

## Overview

Specifies the cycle and timing (trigger) at which an animation runs, as specified in [animation\*.interval](../animation-star-.interval.md).

## Combining specifications (SSP extension)

In SSP, multiple animation interval specifications can be combined by listing them separated by "+". This specification was originally intended to be used with bind, so use caution when specifying it without bind, even if it appears to work.

Examples of combinations follow.

- **bind+always**: An animation that runs continuously while the dressup is ON.
- **bind+runonce**: An animation that runs once when the surface on which the dressup is defined is switched to while the dressup is ON, or when the dressup is turned ON while that surface is displayed.
- **bind+random,frequency**: An animation that occurs with a probability of 1/frequency per second while the dressup is ON.
- **bind+periodic,interval**: An animation that occurs every (interval) seconds while the dressup is ON.
- **bind+runonce+random,5**: An animation that runs once when the surface on which the dressup is defined is switched to while the dressup is ON, or when the dressup is turned ON while that surface is displayed, and thereafter plays with a probability of 1/5 per second.

When another specification is added to bind using "+", the bind interval loses its original property of ignoring the weight parameter in the pattern definition and merging with the base surface as a still image.

For specifications that require parameters, such as random, periodic, and talk, write the parameter at the end, even when combining specifications.

The following is *incorrect*.

```
animation0.interval,random,5+bind
```

The following is *correct*.

```
animation1.interval,bind+random,5
```

Intervals that have parameters cannot be combined with one another.
