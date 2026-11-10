# asis

**カテゴリ:** surface brace \> drawing method

Similar to [overlay](overlay.md), but overlays the *new layer* while ignoring its transparency (transparent colors and, if pna or [seriko.use_self_alpha](../../../shell/descript-txt/seriko.use_self_alpha.md) is set, the image's own alpha channel).<br />
Can also be used for dressups and elements.<br />
The display is undefined when a surface composited from elements is composited using the asis method as an animation part of another surface. On Windows, however, transparent areas will normally be displayed in black (#000000), regardless of the image's original transparent color.

**対応:** SSP
