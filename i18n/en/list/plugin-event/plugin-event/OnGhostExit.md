# OnGhostExit

**カテゴリ:** PLUGIN Event

Occurs when a ghost exits. *\[NOTIFY\]*

- **Reference0**: The HWNDs of the character windows for the exited ghost, after `\0`, separated by byte value 1.<br />
  May be 0 if the windows have not been created, for example.
- **Reference1**: Name of the exited ghost.
- **Reference2**: Current shell name of the exited ghost.
- **Reference3**: ID of the exited ghost (the same as the one sent by Owned SSTP).
- **Reference4**: Full path of the exited ghost.

**対応:** SSP
