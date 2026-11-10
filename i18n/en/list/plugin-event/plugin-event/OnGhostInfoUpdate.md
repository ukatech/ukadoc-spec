# OnGhostInfoUpdate

**カテゴリ:** PLUGIN Event

Occurs when ghost information changes.<br />
May also occur at load time. *\[NOTIFY\]*

- **Reference0**: The HWNDs of the character windows for the ghost whose information changed, after `\0`, separated by byte value 1.<br />
  May be 0 if the windows have not been created, for example.
- **Reference1**: Name of the ghost whose information changed.
- **Reference2**: Current shell name of the ghost whose information changed.
- **Reference3**: ID of the ghost whose information changed (the same as the one sent by Owned SSTP).
- **Reference4**: Full path of the ghost whose information changed.

**対応:** SSP
