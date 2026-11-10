# OnMouseClickEx

**カテゴリ:** Mouse event

Occurs when a mouse button other than the left or right button is clicked and released, if OnMouseUpEx does not respond.

- **Reference0**: The x coordinate of the mouse cursor (local coordinates)
- **Reference1**: The y coordinate of the mouse cursor (local coordinates)
- **Reference2**: Always 0.
- **Reference3**: 0 for the main character, 1 for the partner. SSP/CROW may also use 2 or higher.
- **Reference4**: The hit-test identifier.
- **Reference5**: middle for a wheel click (or the middle button on a three-button mouse), xbutton1 for extended button 1 (usually assigned to “Back”), and xbutton2 for extended button 2 (usually assigned to “Forward”).
- **Reference6**: For input from a touchscreen in a multitouch-capable environment (not a touchpad), touch; from a pen tablet, pen; from the eraser side of a pen tablet, eraser; and from a mouse or similar device, mouse.

**対応:** SSP / Ninix
