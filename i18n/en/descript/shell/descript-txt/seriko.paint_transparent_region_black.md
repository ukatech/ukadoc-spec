# seriko.paint_transparent_region_black,numeric value

**カテゴリ:** descript.txt

Sets how to display regions whose color matches the image's transparent color (the color at the top left of the image), but which are not transparent according to the transparency value.<br />
If set to 0, the image's original color (the transparent color) is displayed with the specified transparency.<br />
If set to 1, the region is filled with black instead of the image color, then displayed with the specified transparency.<br />
For example, if you set this to 0 and provide an image with a full-white pna, the image is displayed as-is, without a transparent color.

**既定値:** Not specified (behaves as 1 for images that use pna for transparency, and as 0 for [images that use the image's own alpha channel for transparency](seriko.use_self_alpha.md))

**対応:** SSP
