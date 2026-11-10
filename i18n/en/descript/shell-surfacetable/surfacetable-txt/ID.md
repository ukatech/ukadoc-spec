# surface ID,name

**カテゴリ:** surfacetable.txt

Assigns an identifying name to a surface ID.<br />
Usually written inside a group.<br />
The first entry written in a group is treated as that group's default surface (for example, 0 for scope,0 and 10 for scope,1).<br />
The name "\_\_parts" indicates that the surface is primarily used as a part, such as in animations or dressup (it is treated as having no name in SSP's Surface Test).<br />
Omitting the name explicitly marks it as undefined. In SSP's Surface Test, only [specific surfaces](../../shell-surfaces/surface-brace/caption_standarddef.md) are assigned default values even when unspecified, so use this to clear the setting for such surfaces.

**既定値:** No behavior / In SSP's Surface Test, only certain surfaces have [default surface definitions](../../shell-surfaces/surface-brace/caption_standarddef.md).

**対応:** SSP
