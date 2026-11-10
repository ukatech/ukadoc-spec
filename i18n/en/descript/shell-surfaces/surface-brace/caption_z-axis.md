# Stacking order of each element

## Higher and lower layers

The side closer to the front of the screen is referred to as the higher layer, and the side farther back as the lower layer.

## Stacking order of each part

For elements and dressups (animations whose interval is bind), the one with the smaller elementID or patternID is lower, and the one with the larger ID is higher.

## Stacking order of the base surface and each animation

The base surface is generally placed at the bottom of all compositing. However, animations that specify SSP's [background option](animation-star-.option-2.md) are composited below (behind) the base surface.

The stacking order among animations, including dressups, is normally descending by animation ID, with the larger ID higher (placed closer to the front of the screen). In SSP, however, this can be changed to ascending order by defining [animation-sort](../descript-brace/animation-sort.md) in the descript brace.

## Stacking order of hit tests (collision)

For a given surface, the collision definition that appears first in surfaces.txt is generally higher. In SSP, however, the order can also be set to ascending or descending by collisionID by defining [collision-sort](../descript-brace/collision-sort.md) in the descript brace.

SSP can also define hit tests that are active only when a specific animation is displayed, using [animation\*.collision](animation-star-.collision-star.md). In this case, after taking the stacking order of each animation into account, the hit tests for each animation and the base surface are evaluated in the usual order.

For example, with animation-sort set to descend, the order from higher to lower is:

1. Higher hit tests of regular animations with larger IDs
2. Lower hit tests of regular animations with larger IDs
3. Higher hit tests of regular animations with smaller IDs
4. Lower hit tests of regular animations with smaller IDs
5. Higher hit tests of the base surface
6. Lower hit tests of the base surface
7. Higher hit tests of animations with the background option and larger IDs
8. Lower hit tests of animations with the background option and larger IDs
9. Higher hit tests of animations with the background option and smaller IDs
10. Lower hit tests of animations with the background option and smaller IDs

(Animations here also include dressups.)
