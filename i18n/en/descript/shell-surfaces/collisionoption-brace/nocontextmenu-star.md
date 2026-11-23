# nocontextmenu\*,collision name

**カテゴリ:** collisionoption brace

Prevents the mouse right-click context menu (the baseware menu) from appearing when the right button is pressed over the specified collision.<br />
The \* part is a number that must be unique among nocontextmenu definitions in the same scope.<br />
The collision name is the name set in the collision definition. It is case-insensitive.

Do not overuse this feature, as it restricts user operations. Use the cursor brace to specify a cursor that tells users the operation is unavailable.

- Whether the menu appears is determined by the collision at the position where the right button was pressed.
- This applies only to mouse right-clicks. The keyboard menu key, Shift+F10, and the task tray menu work as usual.
- Right-button OnMouseDown, OnMouseUp, OnMouseClick, and mouse gestures occur as usual.

**既定値:** Not specified (show the context menu)

**対応:** SSP 2.9.38
