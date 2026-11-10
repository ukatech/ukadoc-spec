# blend-add-fast

**カテゴリ:** surface brace \> Drawing method

Overlays the *new layer* using additive blending, according to the opacity of the *base layer*.<br />
Its behavior is the same as overlay-fast, and its outline does not change, but it performs additive blending on the current surface instead of overwriting it.<br />
Can also be used with dressups and elements.<br />
The word "fast" in the name is historical; the processing is not faster.<br />
It is recommended to set [`seriko.use_self_alpha,full`](../../../shell/descript-txt/seriko.use_self_alpha.md) in the shell's descript.txt.

**対応:** SSP 2.8.36
