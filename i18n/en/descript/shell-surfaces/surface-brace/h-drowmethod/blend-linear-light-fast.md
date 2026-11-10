# blend-linear-light-fast

**カテゴリ:** Surface Brace \> Drawing Method

Stack the *new layer* using linear light compositing, based on the opacity of the *base layer*.<br />
Its behavior is the same as overlay-fast and does not change the outline, but it applies linear light compositing to the current surface instead of overwriting it.<br />
Can also be used with dressup and element.<br />
The word "fast" in the name is due to historical circumstances; processing is not faster.<br />
It is recommended to set [`seriko.use_self_alpha,full`](../../../shell/descript-txt/seriko.use_self_alpha.md) in the shell's descript.txt.

**対応:** SSP 2.8.40
