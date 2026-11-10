# currentghost.seriko.sticky-window

**カテゴリ:** Property system

The current setting of [`\![set,sticky-window,～]`](../../sakura-script/surface/bang-set-sticky-window-ID-ID.md).<br />
Scope IDs in a group are comma-separated, and groups are separated by semicolons.<br />
For example, if scopes 0 and 1 are joined together, and scopes 2 and 3 are joined together, the value is `0,1;2,3`.<br />
The value is empty if no settings are defined.<br />
*\[SET supported\]*

When writing, the current settings are **completely replaced** using the same format. Note that this differs from Sakura Script tags, which add groups.<br />
Writing an empty string clears all join settings.<br />
Groups with fewer than two elements, and groups containing a scope ID already used in another group, are ignored.

**対応:** SSP 2.8.78
