# paint_transparent_region_black,numeric value

**カテゴリ:** descript.txt

Controls the display of areas that use the image's transparent color (the color in the top-left pixel) but are not transparent according to the transparency values.<br />
If set to 0, the image's original color (the transparent color) is displayed at the specified transparency.<br />
If set to 1, the area is filled with black instead of the image color, then displayed at the specified transparency.<br />
For example, an image with a completely white pna will be displayed as-is, without a transparent color, if this is set to 0.<br />
This setting applies to the entire balloon and cannot be overridden.

**既定値:** Unspecified (behaves as 1 for images that use pna as transparency, and as 0 for [images that use the image's own alpha channel as transparency](use_self_alpha.md))

**対応:** SSP
