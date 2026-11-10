# currentghost.seriko.sticky-window

**カテゴリ:** Property System

The current setting state of [`\![set,sticky-window,～]`](../../sakura-script/surface/bang-set-sticky-window-ID-ID.md).<br />
Scope IDs within a group are comma-separated, and groups are separated by semicolons.<br />
For example, if scopes 0 and 1 are attached to each other, and scopes 2 and 3 are attached to each other, the value is `0,1;2,3`.<br />
If there are no settings, the value is empty.<br />
*\[SET enabled\]*

When writing, the current settings are **completely replaced** using the same format. Note that this differs from Sakura Script tags, which add groups.<br />
Writing an empty string clears all attachment settings.<br />
Groups with fewer than two elements, and groups containing a scope ID already used in another group, are ignored.

**対応:** SSP 2.8.78
