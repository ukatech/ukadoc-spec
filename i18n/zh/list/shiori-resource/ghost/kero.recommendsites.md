# kero.recommendsites

**カテゴリ:** Ghost information

The partner's recommendations list.<br />
The value is<br />
Item name 1\[byte value 1\]url1\[byte value 1\]banner image path 1\[byte value 1\]talk script on selection 1\[byte value 2\]item name 2\[byte value 1\]...<br />
It is returned in this format.<br />
However, SHIORI may perform this conversion internally, so refer to the documentation for each SHIORI for details.<br />
The talk script portion is Sakura Script, not a plain string.<br />
If the url portion contains a description beginning with script: instead of a url, that script is executed (for example, [`\![raise]`](../../sakura-script/event/bang-raise-r0-r1-r2.md) is also possible).

**対応:** Materia / SSP / CROW / Ninix
