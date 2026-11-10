# char\*.recommendsites

**カテゴリ:** Ghost information

The recommendation list for `\p[*]`.<br />
The value is<br />
returned in the following format:<br />
Item name 1\[byte value 1\]URL 1\[byte value 1\]banner image path 1\[byte value 1\]talk script on selection 1\[byte value 2\]item name 2\[byte value 1\]...<br />
However, SHIORI may perform the conversion to this format internally; see the documentation for each SHIORI for details.<br />
The talk script part is Sakura Script, not plain text.<br />
Instead of a URL, a value beginning with script: in the URL part executes that script (including [`\![raise]`](../../sakura-script/event/bang-raise-r0-r1-r2.md)).

**対応:** SSP
