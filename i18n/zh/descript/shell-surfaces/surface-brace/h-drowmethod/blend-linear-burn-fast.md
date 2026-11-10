# blend-linear-burn-fast

**カテゴリ:** surface brace \> Drawing method

*New layer* is composited over the image using linear burn, according to the opacity of the *base layer*.<br />
Its behavior is the same as overlay-fast and its outline does not change, but linear burn blending is applied to the current surface instead of overwriting it.<br />
This can also be used with dressup and element.<br />
The word "fast" in the name is due to historical circumstances; processing is not faster.<br />
It is recommended to set [`seriko.use_self_alpha,full`](../../../shell/descript-txt/seriko.use_self_alpha.md) in the shell's descript.txt.

**対応:** SSP 2.8.40
