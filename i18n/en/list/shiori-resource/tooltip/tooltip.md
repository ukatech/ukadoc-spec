# tooltip

**カテゴリ:** Tooltip events

Retrieves the tooltip text for the shell.<br />
Notifies when the mouse cursor is over a shell surface.<br />
If [shell-side settings](../../../descript/shell-surfaces/tooltip-brace/entry.md) are present, they take precedence.

- **Reference0**: Mouse cursor x-coordinate (local coordinates)
- **Reference1**: Mouse cursor y-coordinate (local coordinates)
- **Reference2**: Always 0.
- **Reference3**: 0 for the base character, 1 for the companion. SSP/CROW may also use 2 or higher.
- **Reference4**: Hit-test region identifier.
- **Reference5**: Always 0.

**対応:** SSP
