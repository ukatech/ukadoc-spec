# blend-add-fast

**カテゴリ:** surface brace \> drawing method

Overlays the *new layer* using additive blending according to the opacity of the *base layer*.<br />
Like overlay-fast, its behavior does not change the outline, but it performs additive blending on the current surface instead of overwriting it.<br />
Can also be used for dressups and elements.<br />
The "fast" in the name is historical and does not mean that processing is faster.<br />
It is recommended to set [`seriko.use_self_alpha,full`](../../../shell/descript-txt/seriko.use_self_alpha.md) in the shell's descript.txt.

**対応:** SSP 2.8.36
