# seriko.paint_transparent_region_black,number

**カテゴリ:** descript.txt

Controls the display of regions that have the image's transparency color (the color at the top left of the image) but are not transparent according to their opacity values.<br />
If 0, the image's original color (the transparency color) is displayed at the specified opacity.<br />
If 1, the region is filled with black instead of the image's color and then displayed at the specified opacity.<br />
For example, if 0 is specified and an image has an entirely white pna, the image is displayed as-is without a transparency color.

This can also be specified in the ghost's descript.txt. The shell's setting takes precedence if present; otherwise, the ghost's value is used.

**既定値:** Unspecified (equivalent to 1 for images using pna for opacity, and 0 for [images using their own alpha channel for opacity](seriko.use_self_alpha.md))

**対応:** SSP
