# sakura.portalsites

**カテゴリ:** Ghost information

The portal list on the main character's side.<br />
The value<br />
is returned in the following format:<br />
Item name 1\[byte value 1\]URL 1\[byte value 1\]banner image path 1\[byte value 1\]talk script on selection 1\[byte value 2\]item name 2\[byte value 1\]...<br />
However, SHIORI may perform the conversion to this format internally. See the documentation for each SHIORI for details.<br />
The talk script portion is not plain text, but Sakura Script.<br />
If the URL portion contains a description beginning with script: instead of a URL, that script is executed (for example, [`\![raise]`](../../sakura-script/event/bang-raise-r0-r1-r2.md) is also possible).

**対応:** Materia / SSP / CROW / Ninix
