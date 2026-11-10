# OnMouseUp

**カテゴリ:** Mouse events

Occurs when the left or right mouse button is released.

- **Reference0**: Mouse cursor x coordinate (local coordinates)
- **Reference1**: Mouse cursor y coordinate (local coordinates)
- **Reference2**: Always 0.
- **Reference3**: 0 for the main character, 1 for the partner. SSP/CROW also support 2 and higher.
- **Reference4**: Hit-test identifier.
- **Reference5**: 0 for a left click, 1 for a right click, 2 for a middle click (compatibility behavior: migration to OnMouseClickEx is recommended).
- **Reference6**: Input from a touchscreen in a multitouch-capable environment (※ not a touchpad) is touch, from a pen tablet is pen, from the eraser side of a pen tablet is eraser, and from a mouse or similar device is mouse

**対応:** SSP / Ninix
