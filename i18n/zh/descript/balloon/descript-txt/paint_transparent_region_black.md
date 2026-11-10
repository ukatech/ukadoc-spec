# paint_transparent_region_black,value

**カテゴリ:** descript.txt

Controls the display of regions that have the image's transparency color (the color at the top-left of the image) but are not transparent according to the transparency value.<br />
If set to 0, the original image color (transparency color) is displayed with the specified transparency.<br />
If set to 1, the region is filled with black instead of the image color, then displayed with the specified transparency.<br />
For example, if 0 is specified and an entirely white pna is prepared, the image is displayed as-is, with no transparency color.<br />
This setting applies only to the entire balloon and cannot be overridden.

**既定値:** Not specified (acts like 1 for images that use pna for transparency, and like 0 for [images that use the image's own alpha channel for transparency](use_self_alpha.md))

**対応:** SSP
