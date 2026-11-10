# OnMouseGesture

**カテゴリ:** Mouse events

Occurs when the mouse is right-dragged or the wheel is dragged.<br />
Also, from SSP2.3.53 onward, in a touchscreen environment, if SHIORI returns nothing (204 No Content is returned) for an OnMouseGesture whose Reference5 is up or down, [OnMouseWheel](OnMouseWheel.md) occurs as a fallback event. See the OnMouseWheel section for details.

- **Reference0**: 0 for the main character, 1 for the partner. SSP/CROW also support 2 and higher.
- **Reference1**: Mouse cursor xy coordinates (separated by byte values)
- **Reference2**: Hit-test identifier.
- **Reference3**: Mouse cursor xy coordinates where the right-drag started (separated by byte values)
- **Reference4**: Hit-test identifier where the right-drag started.
- **Reference5**: Gesture direction.<br />
  left_up (upper left) up (up) right_up (upper right)<br />
  left (left) right (right)<br />
  left_down (lower left) down (down) right_down (lower right)<br />
  circle.cw (clockwise) circle.ccw (counterclockwise)<br />
  end (right button released)
- **Reference6**: Gesture movement angle.<br />
  0 degrees to the right, increasing counterclockwise up to 360 degrees.

**対応:** SSP
