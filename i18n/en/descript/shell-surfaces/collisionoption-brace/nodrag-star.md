# nodrag\*,collision name

**カテゴリ:** collisionoption brace

Prevents window dragging from starting when the left button is pressed over the specified collision.<br />
The \* part is a number that must be unique among nodrag definitions in the same scope.<br />
The collision name is the name set in the collision definition. It is case-insensitive.

Do not overuse this feature, as it restricts user operations. Use the cursor brace to specify a cursor that tells users the operation is unavailable.

- Whether window dragging starts is determined by the collision at the position where the left button was pressed. This does not change while the button is held, and dragging does not start even if the cursor leaves the collision.
- OnMouseMove occurs as usual while the button is held (including when the cursor leaves the window; Reference4 is empty at positions with no collision). This allows the ghost to implement controls such as knobs and sliders.
- OnMouseDragStart and OnMouseDragEnd do not occur.
- Since window dragging does not start, OnMouseUp occurs when the button is released.
- If the cursor moves beyond the distance from the press position that triggers a drag (a Windows system setting), OnMouseClick does not occur, even if there is no response to OnMouseUp. This is the same behavior as during window dragging.

**既定値:** Not specified (window dragging starts)

**対応:** SSP 2.9.38
