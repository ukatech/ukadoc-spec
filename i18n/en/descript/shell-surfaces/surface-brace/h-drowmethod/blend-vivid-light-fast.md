# blend-vivid-light-fast

**カテゴリ:** surface brace \> Drawing methods

Overlay the *new layer* using vivid light blending according to the opacity of the *base layer*.<br />
Its behavior is the same as overlay-fast: the outline does not change, but vivid light blending is applied to the current surface instead of overwriting it.<br />
This can also be used with dressup and element.<br />
The “fast” in the name is historical; processing is not faster.<br />
It is recommended to set [`seriko.use_self_alpha,full`](../../../shell/descript-txt/seriko.use_self_alpha.md) in the shell's descript.txt.

**対応:** SSP 2.8.40
