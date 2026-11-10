# OnMouseGesture

**カテゴリ:** Mouse event

Occurs when the mouse is right-dragged or the wheel is dragged.<br />
Also, from SSP 2.3.53 onward, in a touch-panel environment, if SHIORI returns nothing (204 No Content is returned) for an OnMouseGesture whose Reference5 is up or down, [OnMouseWheel](OnMouseWheel.md) occurs as a fallback event. See the OnMouseWheel section for details.

- **Reference0**: 0 for the main character, 1 for the partner. SSP/CROW may also use 2 and higher.
- **Reference1**: The xy coordinates of the mouse cursor (separated by byte value 1)
- **Reference2**: The hit-test region identifier.
- **Reference3**: The xy coordinates of the mouse cursor when the right-drag started (separated by byte value 1)
- **Reference4**: The hit-test region identifier where the right-drag started.
- **Reference5**: Gesture direction.<br />
  left_up (upper left) up (up) right_up (upper right)<br />
  left (left) right (right)<br />
  left_down (lower left) down (down) right_down (lower right)<br />
  circle.cw (clockwise) circle.ccw (counterclockwise)<br />
  end (right button released)
- **Reference6**: Gesture movement angle.<br />
  Measured counterclockwise from 0 degrees to the right.

**対応:** SSP
