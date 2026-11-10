# Drawing methods

## Overview

The methods for compositing and drawing each frame (part) in [animation pattern definitions](../animation-star-.pattern-star.md) and [element definitions](../element-star.md).

Rather than compositing images, various methods serve roles such as replacing the [base surface](../caption_basesurface.md) (base), moving the base surface (move), and inserting or executing other animations (insert, start, stop, alternativestart, alternativestop).

## Handling of drawing methods in dressup

In dressup definitions, methods that do not composite images (move, insert, start, stop, alternativestart, alternativestop) are disabled (treated as overlay). However, base is effective only when used in the very first pattern, making it possible to replace the base surface only while that dressup is ON.

The dressup methods add and bind are implemented as synonyms for overlay. In dressup, specifying any of these three methods has the same effect.

## Handling of drawing methods in element definitions

In element definitions, methods that do not composite images (base, move, insert, start, stop, alternativestart, alternativestop) are disabled (treated as overlay).

The other dressup methods, add and bind, are also disabled (but in the current SSP implementation, disabled values are interpreted as overlay, so the result is drawing as specified).

This is self-evident, but most drawing methods specified for the first element (element0, or later elements if surface\*.png does not exist) are equivalent to base. However, the fact that the transparent color is displayed as-is with the asis method remains effective.

Note that when a surface composited from elements is used as an animation part, the result of the element composition is treated as a single image. However, this implementation was introduced in SSP2.3.53; note that it was undefined before that.

## Differences and commonalities in compositing methods across elements, animations, and dressup

The meaning of compositing methods differs between elements, animations, and dressup.

Element definitions are intended to produce a single still image to serve as the base surface. In an element definition, each successive composite is applied to the result of the previous composites, producing a single still image as the final result.

Dressup definitions, like element definitions, are a mechanism for producing a still image, so the process for resolving drawing methods is quite similar to that of element definitions. In a dressup pattern definition, the first pattern is composited onto the base surface, and each subsequent composite is applied to the result of the previous composites, producing a single still image as the final result. Therefore, dressup behaves as if it were integrated with the base surface.

In contrast, regular animations that are not dressup are a video-like representation, so their process differs greatly from the previous two. Each animation pattern definition defines one frame of the animation, and each is independent. Each pattern definition composites the base surface with a new image to create a new frame, so the composite result from the previous pattern definition (previous frame) does not affect the next frame. Drawing new frames one after another in this way produces a video-like representation.

However, in all cases, compositing methods share the function of combining two images, the “original image” and the “new image.” Therefore, for convenience, in the explanations of drawing methods, ukadoc calls the *“original image”* the *base layer*, and the latter, the *“new image,”* the *new layer*.

Put another way, each animation pattern definition creates a frame by compositing a new layer onto the base surface as the base layer. In contrast, dressup and element composition produce a single still image as the result of repeatedly compositing a new layer onto the result of the previous composites as the base layer.

## Drawing methods and transparent colors

The top-left pixel of an image is treated as its transparent color, and areas of the same color are transparent when displayed. This also applies to surfaces used in pattern definitions and images used in element definitions.

The RGB values of the transparent colors in the images composited at this point do not need to be identical.

Each drawing method has its own characteristics in how it handles transparent colors; see the relevant sections.

## Offsets and overlap between the base layer and new layer

The behavior when a new layer is composited outside the base layer (due to image size or position) is left to the baseware implementation.

In MATERIA, parts that extend beyond the base layer are simply not displayed.

In CROW, compositing in a way that extends beyond the base layer results in incorrect drawing.

SSP allows a new layer to be composited so that it extends beyond the base layer. In this case, *fully transparent areas are added to the base layer just enough to prevent the new layer from extending beyond it*.

Conversely, areas outside the new layer are *empty areas that are different from fully transparent areas*, and compositing *does nothing, leaving the contents of the base layer unchanged*. This is an important premise to understand, especially for the replace and reduce methods, where fully transparent areas of the new layer affect the composite result.
