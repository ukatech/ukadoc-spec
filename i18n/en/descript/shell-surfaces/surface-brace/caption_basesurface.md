# Base Surface

## Base Surface

The image representing the basic state of each surface, before animations are composited, is called the base surface.

Animations are normally drawn above the base surface (closer to the viewer).

## The Base Surface's Components

A surface's base surface is defined by the surface\*.png corresponding to its ID and by the [element definition](element-star.md) in the surface brace corresponding to that ID.

For a surface with a surface\*.png, that image is the base surface for surface\*. However, if element0 is also defined, the contents of surface\*.png are discarded and replaced by the element0 definition (this behavior exists for compatibility).

If definitions for element1 and later are present, they are composited in sequence on top of the previous elements, and the final composite is treated as the base surface.
