# OnGamepadAxisMove

**カテゴリ:** Gamepad event

Occurs when the value of a gamepad analog stick or trigger changes significantly from the time it was last reported.<br />
Events do not occur for minor fluctuations. Values near the center of a stick or in a trigger's dead zone are automatically rounded to 0.<br />
When a stick or trigger returns to the center position (neutral), the event always occurs regardless of the amount of change.<br />
The event is broadcast simultaneously to all running ghosts.<br />
Axis events may occur frequently while operating a stick, so consider rate limiting on the ghost side when performing heavy processing.

- **Reference0**: [Pad index](caption_gamepad_padindex.md).
- **Reference1**: [Axis name](caption_gamepad_axis.md).
- **Reference2**: Raw value (integer). The range depends on the baseware implementation.
- **Reference3**: Normalized value (decimal). Sticks range from -1.0 to 1.0, and triggers range from 0.0 to 1.0. This is usually the value to use.

**対応:** SSP 2.7.54
