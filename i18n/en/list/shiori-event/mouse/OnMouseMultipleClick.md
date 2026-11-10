# OnMouseMultipleClick

**カテゴリ:** Mouse events

Occurs when clicked three or more times in succession.<br />
※ If SHIORI does not respond to this event, processing returns to the usual OnMouseClick and OnMouseDoubleClick sequence.

- **Reference0**: Mouse cursor x coordinate (local coordinates)
- **Reference1**: Mouse cursor y coordinate (local coordinates)
- **Reference2**: Always 0.
- **Reference3**: 0 for the main character, 1 for the partner, 2 and higher thereafter
- **Reference4**: Hit-test identifier.
- **Reference5**: 0 for a left click, 1 for a right click
- **Reference6**: Input from a touchscreen in a multitouch-capable environment (※ not a touchpad) is touch, from a pen tablet is pen, from the eraser side of a pen tablet is eraser, and from a mouse or similar device is mouse
- **Reference7**: Number of consecutive clicks

**対応:** SSP
