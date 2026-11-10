# kero.recommendsites

**カテゴリ:** Ghost information

The partner's recommendations list.<br />
The value is<br />
item name 1\[byte value 1\]url1\[byte value 1\]banner image path 1\[byte value 1\]talk script on selection 1\[byte value 2\]item name 2\[byte value 1\]...<br />
and is returned in this format.<br />
However, SHIORI may perform this conversion internally, so refer to the documentation for each SHIORI for details.<br />
The talk script portion is not a plain string but Sakura Script.<br />
Instead of a URL, a description beginning with script: in the URL portion executes that script (including [`\![raise]`](../../sakura-script/event/bang-raise-r0-r1-r2.md), for example).

**対応:** Materia / SSP / CROW / Ninix
