# currentghost.seriko.zorder

**カテゴリ:** Property system

The current state of the [`\![set,zorder,～]`](../../sakura-script/surface/bang-set-zorder-ID-ID.md) settings.<br />
Elements within a group are separated by commas, and groups are separated by semicolons. Elements are listed from front to back.<br />
In explicit element mode, the value is returned as abbreviations consisting of `s` (surface) or `b` (balloon) plus the scope ID, as in `s0,b0,s1;s2,b2`.<br />
In the conventional mode, which specifies only scope IDs, only numbers are returned, as in `0,1;2,3`.<br />
In `front` and `back` mode, the front and back parts are separated by a semicolon, as in `front,0,1;back,3`. If only one is specified, only that part is returned.<br />
If no settings exist, there is no value.<br />
*\[SET enabled\]*

When written, a value in the same format **completely replaces the current settings**. Note that this differs from the Sakura Script tag, which adds groups.<br />
Writing an empty string clears all Z-order settings.<br />
Writing back a value as read restores the original state.<br />
Groups with fewer than two elements are ignored (`front` and `back` may have only one). Explicit element mode and conventional mode are mutually exclusive, so **the two modes cannot be mixed** as in `s0,b0;2,3`. `front` and `back` cannot be mixed with other modes either; if mixed, the later specification takes precedence.

**対応:** SSP 2.8.78/2.9.35 (front,back syntax)
