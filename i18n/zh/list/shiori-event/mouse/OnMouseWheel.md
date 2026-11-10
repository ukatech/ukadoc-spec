# OnMouseWheel

**カテゴリ:** Mouse event

Occurs when the mouse wheel is rotated.<br />
Since SSP2.3.53, on touch-panel environments, if SHIORI returns nothing (204 No Content) for an [OnMouseGesture](OnMouseGesture.md) event whose Reference5 is up or down, OnMouseWheel is also triggered as a fallback event. In that case, the numeric value of Reference2 is converted based on the original OnMouseGesture movement amount and the up or down direction (positive for up, negative for down).

- **Reference0**: x coordinate of the mouse cursor (local coordinates)
- **Reference1**: y coordinate of the mouse cursor (local coordinates)
- **Reference2**: Mouse wheel rotation amount and direction.
- **Reference3**: 0 for the main character, 1 for the partner. SSP/CROW may also use 2 and above.
- **Reference4**: Hit-test identifier.
- **Reference5**: ※SSP/NINIX only　Always 0.
- **Reference6**: ※SSP/NINIX only　Input from a touch panel in a multi-touch-compatible environment (※touchpads are not supported) is reported as touch, input from a pen tablet as pen, input from the eraser side of a pen tablet as eraser, and input from a mouse or similar device as mouse

**対応:** Materia / SSP / CROW / Ninix
