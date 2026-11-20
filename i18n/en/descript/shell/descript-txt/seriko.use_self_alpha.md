# seriko.use_self_alpha,value

**カテゴリ:** descript.txt

If 1 or true is specified, images with transparency (PNG with an alpha channel) and images with a .pna use the alpha channel for opacity. If neither an alpha channel nor a .pna exists, the conventional behavior is used, with the color at the top left of the image as the key color.<br />
If full is specified, in addition to the above, all images without an alpha channel are treated as opaque (the top-left key color is not made transparent).

This can also be specified in the ghost's descript.txt. The shell's setting takes precedence if present; otherwise, the ghost's value is used.

**既定値:** 0

**対応:** SSP
