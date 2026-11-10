# Base surface

## Base surface

The image in each surface's basic state, before animations are composited, is called the base surface.

Animations are normally drawn above the base surface (closer to the viewer).

## The base surface itself

The base surface of a surface is defined by the surface\*.png corresponding to its ID and by [element definitions](element-star.md) in the surface brace for that ID.

For a surface with a surface\*.png, that image is its base surface. However, if element0 is also defined, the contents of surface\*.png are discarded and replaced by the element0 definition (this behavior is for compatibility).

If there are definitions for element1 and higher, they are composited sequentially on top, and the final composited result is treated as the base surface.
