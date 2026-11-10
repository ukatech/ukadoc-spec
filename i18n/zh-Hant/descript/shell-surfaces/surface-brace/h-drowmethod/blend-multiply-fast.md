# blend-multiply-fast

**カテゴリ:** surface brace \> Drawing method

Overlay the *new layer* using multiply compositing, according to the opacity of the *base layer*.<br />
Its behavior is the same as overlay-fast and its outline does not change, but it applies multiply compositing to the current surface instead of overwriting it.<br />
Can also be used with dressup and element.<br />
The word "fast" in the name is historical; processing is not actually faster.<br />
It is recommended to set [`seriko.use_self_alpha,full`](../../../shell/descript-txt/seriko.use_self_alpha.md) in the shell's descript.txt.

**対応:** SSP 2.8.36
