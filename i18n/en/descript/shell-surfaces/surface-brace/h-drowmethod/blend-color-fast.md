# blend-color-fast

**カテゴリ:** surface brace \> drawing method

Overlay the *new layer* using Color blending, according to the opacity of the *base layer*.<br />
Its behavior is the same as overlay-fast, and the outline remains unchanged, but instead of overwriting, it applies Color blending to the current surface.<br />
It can also be used with dressup and element.<br />
The "fast" in the name is historical; it does not mean that processing is faster.<br />
It is recommended to set [`seriko.use_self_alpha,full`](../../../shell/descript-txt/seriko.use_self_alpha.md) in the shell's descript.txt.

**対応:** SSP 2.8.39
