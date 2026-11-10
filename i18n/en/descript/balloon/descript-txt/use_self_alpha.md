# use_self_alpha,value

**カテゴリ:** descript.txt

If 1 or true is specified, surfaces with transparent images (PNG files with an alpha channel) or .pna files use the alpha channel as transparency. If neither an alpha channel nor a .pna file is present, the conventional behavior is used: the color at the top-left of the image is treated as the key color.<br />
If full is specified, all surfaces without an alpha channel are also treated as opaque, in addition to the above (the top-left key color is not made transparent).<br />
Note that input-box balloons cannot be made translucent unless use_input_alpha is also set to 1.<br />
This setting applies to the entire balloon and cannot be overridden.

**既定値:** 0

**対応:** SSP
