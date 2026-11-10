# Animation interval

## Overview

Specifies the cycle and timing (trigger) at which an animation runs, as specified in [animation\*.interval](../animation-star-.interval.md).

## Combining specifications (SSP extension)

With SSP, multiple animation interval specifications can be combined by listing them separated by "+". Since this feature was originally designed for use with bind, be cautious when using it without bind, even if it appears to work.

Examples of combined specifications follow.

- **bind+always**: An animation that runs continuously while that dressup is ON.
- **bind+runonce**: An animation that runs once when switching to the surface where that dressup is defined, or when that dressup is turned ON while that surface is displayed.
- **bind+random,frequency**: An animation that occurs with a probability of 1/frequency per second while that dressup is ON.
- **bind+periodic,interval**: An animation that occurs every (interval) seconds while that dressup is ON.
- **bind+runonce+random,5**: An animation that runs once when switching to the surface where that dressup is defined, or when that dressup is turned ON while that surface is displayed, then plays with a probability of 1 in 5 per second while that dressup is ON.

When other specifications are added to bind using "+", bind interval properties such as "ignoring the pattern definition's weight parameter and combining with the base surface as a still image" no longer apply.

Also, for specifications that require a parameter, such as random, periodic, and talk, write the parameter at the end, including when combining specifications.

The following is *incorrect*.

```
animation0.interval,random,5+bind
```

The following is *correct*.

```
animation1.interval,bind+random,5
```

Interval specifications that have parameters cannot be combined with each other.
