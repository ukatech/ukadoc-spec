# seriko.use_self_alpha,value

**カテゴリ:** descript.txt

If set to 1 or true, images with transparency (PNG files with an alpha channel) and images with a .pna file use the alpha channel as the transparency value. If neither an alpha channel nor a .pna file is present, the traditional behavior of using the color at the top left of the image as the key color applies.<br />
If set to full, in addition to the above, all images without an alpha channel are treated as fully opaque (the key color at the top left is not made transparent).

**既定値:** 0

**対応:** SSP
