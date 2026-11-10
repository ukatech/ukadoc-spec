# OnGamepadAxisMove

**カテゴリ:** Gamepad event

Occurs when the value of a gamepad analog stick or trigger changes significantly from the value at the previous notification.<br />
The event does not occur for minor fluctuations. Values near the stick center and within the trigger's dead zone are automatically rounded to 0.<br />
The event always occurs when a stick or trigger returns to its center (neutral) position, regardless of the amount of change.<br />
The event is broadcast to all running ghosts simultaneously.<br />
Axis events may occur frequently while a stick is being operated, so consider rate-limiting on the ghost side when performing expensive processing.

- **Reference0**: [Pad index](caption_gamepad_padindex.md).
- **Reference1**: [Axis name](caption_gamepad_axis.md).
- **Reference2**: Raw value (integer). The range depends on the baseware implementation.
- **Reference3**: Normalized value (decimal). Sticks range from -1.0 to 1.0, and triggers from 0.0 to 1.0. Use this value in most cases.

**対応:** SSP 2.7.54
