# currentghost.seriko.zorder

**カテゴリ:** Property System

The current setting state of [`\![set,zorder,～]`](../../sakura-script/surface/bang-set-zorder-ID-ID.md).<br />
Elements within a group are comma-separated, and groups are separated by semicolons. Elements are listed from front to back.<br />
In explicit element specification mode, values are returned in abbreviated form as `s` (surface) or `b` (balloon) followed by a scope ID, such as `s0,b0,s1;s2,b2`.<br />
In the legacy mode, which specifies only scope IDs, only numbers are returned, such as `0,1;2,3`.<br />
If there are no settings, the value is empty.<br />
*\[SET enabled\]*

When writing, the current settings are **completely replaced** using the same format. Note that this differs from Sakura Script tags, which add groups.<br />
Writing an empty string clears all Z-order settings.<br />
Writing back the value as read reproduces the original state.<br />
Groups with fewer than two elements are ignored. Also, because explicit specification mode and legacy mode are mutually exclusive, **the two modes cannot be mixed**, as in `s0,b0;2,3`.

**対応:** SSP 2.8.78
