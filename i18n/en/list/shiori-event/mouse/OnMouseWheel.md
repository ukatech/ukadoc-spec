# OnMouseWheel

**カテゴリ:** Mouse events

Occurs when the mouse wheel rotates.<br />
From SSP2.3.53 onward, in a touchscreen environment, OnMouseWheel also occurs as a fallback event if SHIORI returns nothing (204 No Content is returned) for an [OnMouseGesture](OnMouseGesture.md) whose Reference5 is up or down. In that case, the value of Reference2 is converted from the movement amount and up/down direction of the original OnMouseGesture (positive for up, negative for down).

- **Reference0**: Mouse cursor x coordinate (local coordinates)
- **Reference1**: Mouse cursor y coordinate (local coordinates)
- **Reference2**: Mouse wheel rotation amount and direction.
- **Reference3**: 0 for the main character, 1 for the partner. SSP/CROW also support 2 and higher.
- **Reference4**: Hit-test identifier.
- **Reference5**: ※ SSP/NINIX only　Always 0.
- **Reference6**: ※ SSP/NINIX only　Input from a touchscreen in a multitouch-capable environment (※ not a touchpad) is touch, from a pen tablet is pen, from the eraser side of a pen tablet is eraser, and from a mouse or similar device is mouse

**対応:** Materia / SSP / CROW / Ninix
