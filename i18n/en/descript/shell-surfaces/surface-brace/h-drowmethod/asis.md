# asis

**カテゴリ:** surface brace \> Drawing method

Similar to [overlay](overlay.md), but overlays the *new layer* while ignoring its transparency (the transparent color and, if pna or [seriko.use_self_alpha](../../../shell/descript-txt/seriko.use_self_alpha.md) is set, the image's own alpha channel).<br />
Can also be used with dressups and elements.<br />
The display result is undefined when an element-composited surface is combined as an animation part of another surface using the asis method. On Windows, however, transparent areas will normally appear black (#000000), regardless of the image's original transparent color.

**対応:** SSP
