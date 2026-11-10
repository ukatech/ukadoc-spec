# OnGhostBoot

**カテゴリ:** PLUGIN Event

Occurs when a ghost starts.

- **Reference0**: The HWNDs of the character windows for the started ghost, after `\0`, separated by byte value 1.<br />
  May be 0 if the windows have not been created, for example.
- **Reference1**: Name of the started ghost.
- **Reference2**: Current shell name of the started ghost.
- **Reference3**: ID of the started ghost (the same as the one sent by Owned SSTP).
- **Reference4**: Full path of the started ghost.

**対応:** SSP
