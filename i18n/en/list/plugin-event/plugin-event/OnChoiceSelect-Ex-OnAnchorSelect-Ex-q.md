# OnChoiceSelect(Ex)/OnAnchorSelect(Ex)/events with arbitrary names specified in `\q` or similar

**カテゴリ:** PLUGIN Event

A plugin-side hook for SHIORI Events that occur when a choice or anchor is selected.<br />
If the script sent by a plugin to a ghost, or the script returned by a ghost in response to an event notified by a plugin, contains a choice- or anchor-related Sakura Script tag, then for that occurrence only, the same event notified to SHIORI when the choice or anchor is selected is also forwarded to the plugin.

- **Reference\***: Reference for the choice- or anchor-related SHIORI Event that occurred.

**対応:** SSP
