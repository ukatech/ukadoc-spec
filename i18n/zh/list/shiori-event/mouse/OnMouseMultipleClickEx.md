# OnMouseMultipleClickEx

**カテゴリ:** Mouse event

Occurs when a button other than the left or right button is clicked three or more times in succession.<br />
※ If SHIORI does not respond to this event, processing returns to the usual OnMouseClickEx and OnMouseDoubleClickEx sequence.

- **Reference0**: Mouse cursor x-coordinate (local coordinates)
- **Reference1**: Mouse cursor y-coordinate (local coordinates)
- **Reference2**: Always 0.
- **Reference3**: 0 for the main character, 1 for the partner; 2 and higher thereafter
- **Reference4**: Hit-test region identifier.
- **Reference5**: Wheel click (or the middle button on a three-button mouse) is middle; extended button 1 (usually assigned to “Back”) is xbutton1; extended button 2 (usually assigned to “Forward”) is xbutton2.
- **Reference6**: For input from a touch panel in a multitouch-capable environment (※ touchpads are not supported), touch; from a pen tablet, pen; from the eraser end of a pen tablet, eraser; and from a mouse or similar device, mouse
- **Reference7**: Number of consecutive clicks

**対応:** SSP
