# OnMouseDown

**カテゴリ:** Mouse event

Occurs when the left or right mouse button is pressed.

- **Reference0**: The x coordinate of the mouse cursor (local coordinates)
- **Reference1**: The y coordinate of the mouse cursor (local coordinates)
- **Reference2**: Always 0.
- **Reference3**: 0 for the main character, 1 for the partner. SSP/CROW may also use 2 or higher.
- **Reference4**: The hit-test identifier.
- **Reference5**: 0 for a left click, 1 for a right click, and 2 for a middle click (compatibility behavior; migration to OnMouseClickEx is recommended).
- **Reference6**: For input from a touchscreen in a multitouch-capable environment (not a touchpad), touch; from a pen tablet, pen; from the eraser side of a pen tablet, eraser; and from a mouse or similar device, mouse.

**対応:** SSP / Ninix
