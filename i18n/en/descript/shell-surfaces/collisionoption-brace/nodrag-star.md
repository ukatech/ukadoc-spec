# nodrag\*,collision region name

**カテゴリ:** collisionoption brace

Prevents a window drag from starting when the left button is pressed over the specified collision region.<br />
The \* is a number that must be unique among nodrag definitions in the same scope.<br />
The collision region name is the name set in the collision definition. It is case-insensitive.

Do not overuse this option, as it restricts user operations. Use the cursor brace to specify a cursor that tells the user the operation is unavailable.

- Whether a window drag starts is determined by the collision region where the left button was pressed. This does not change while the button is held, and a window drag will not start even if the cursor leaves the collision region.
- OnMouseMove occurs normally while the button is held (including outside the window; Reference4 is empty at positions without a collision region). The ghost can implement controls such as knobs and sliders.
- OnMouseDragStart and OnMouseDragEnd do not occur.
- Since no window drag starts, OnMouseUp occurs when the button is released.
- If the cursor moves beyond the distance from the press position that is recognized as a window drag (a Windows system setting), OnMouseClick does not occur even if OnMouseUp was not handled. This is the same behavior as for a window drag.

**既定値:** Not specified (a window drag starts)

**対応:** SSP 2.9.38
