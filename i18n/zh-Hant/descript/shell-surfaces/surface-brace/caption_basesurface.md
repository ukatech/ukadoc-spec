# Base surface

## Base surface

The image representing the basic state of each surface, before animations are composited, is called the base surface.

Animations are normally drawn above the base surface (toward the front of the screen).

## Base surface contents

The base surface of a surface is defined by the surface\*.png corresponding to its ID and by [element definitions](element-star.md) in the surface braces corresponding to that ID.

For a surface with a surface\*.png, that image is the base surface of surface\*. However, if element0 is also defined, the contents of surface\*.png are discarded and replaced with the contents defined by element0 (this specification ensures compatibility).

If there are definitions for element1 and later, they are composited in sequence, layered on top of one another, and the final composite is treated as the base surface.
