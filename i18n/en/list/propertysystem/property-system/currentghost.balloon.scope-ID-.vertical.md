# currentghost.balloon.scope(ID).vertical

**カテゴリ:** Property system

Whether the current balloon uses [vertical writing](../../../descript/balloon/descript-txt/vertical.md). 1 for vertical writing, 0 for horizontal writing.<br />
[validwidth](currentghost.balloon.scope-ID-.validwidth.md) and [validheight](currentghost.balloon.scope-ID-.validheight.md) represent dimensions in the “on-screen orientation” indicated by their names, even with vertical writing: for vertical writing, validwidth is the “width available in the direction the columns advance,” and validheight is the “length of one column.” [lines](currentghost.balloon.scope-ID-.lines.md) indicates the “number of lines that fit” (or columns for vertical writing) in either orientation.<br />
To calculate how many characters fit in one line (or column), check validheight for vertical writing and validwidth for horizontal writing. Use this property to determine which one to check.<br />
※Specification changed in SSP 2.8.83. In 2.8.80, validwidth and validheight for vertical writing represented dimensions based on the “direction in which characters advance.”

**対応:** SSP 2.8.80
