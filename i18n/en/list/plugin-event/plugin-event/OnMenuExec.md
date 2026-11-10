# OnMenuExec

**カテゴリ:** PLUGIN Event

Occurs when a plugin is run from the owner-draw menu.<br />
Some kind of reaction is recommended.

- **Reference0**: HWNDs of each character window after `\0` of the ghost that called the plugin, delimited by byte value 1.<br />
  May contain 0, such as when the window has not been created.
- **Reference1**: Name of the ghost that called the plugin.
- **Reference2**: Name of the current shell of the ghost that called the plugin.
- **Reference3**: ID of the ghost that called the plugin (same as the one sent by Owned SSTP).
- **Reference4**: Full path of the ghost that called the plugin.

**対応:** SSP
