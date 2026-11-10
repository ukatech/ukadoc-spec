# currentghost.seriko.zorder

**カテゴリ:** Property system

The current setting of [`\![set,zorder,～]`](../../sakura-script/surface/bang-set-zorder-ID-ID.md).<br />
Elements within a group are comma-separated, and groups are separated by semicolons. Elements are listed from front to back.<br />
In explicit element mode, the value is returned in abbreviated form as `s` (surface) or `b` (balloon), followed by a scope ID, such as `s0,b0,s1;s2,b2`.<br />
In the traditional mode, which specifies only scope IDs, only numbers are returned, such as `0,1;2,3`.<br />
The value is empty if no settings are defined.<br />
*\[SET supported\]*

When writing, the current settings are **completely replaced** using the same format. Note that this differs from Sakura Script tags, which add groups.<br />
Writing an empty string clears all Z-order settings.<br />
Writing back a read value as-is reproduces the original state.<br />
Groups with fewer than two elements are ignored. Explicit element mode and traditional mode are mutually exclusive, so **the two modes cannot be mixed**, as in `s0,b0;2,3`.

**対応:** SSP 2.8.78
