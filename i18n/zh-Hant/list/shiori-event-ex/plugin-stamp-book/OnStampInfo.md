# OnStampInfo

**カテゴリ:** Plugin "Stamp Book"

An event that reports information about stamps.<br />
Triggered at ghost startup, when the plugin is loaded or unloaded, and whenever OnStampInfoCall is sent.

- **Reference0**: Total number of stamps.
- **Reference1**: Whether a stamp from this ghost exists: 1 if so, 0 otherwise.<br />
  This may be unreliable when multiple ghosts are running, so to determine this with certainty, it is recommended to trigger this event explicitly using OnStampInfoCall.
- **Reference2**: Plugin path.
- **Reference3**: All stamp information. The ghost name, stamp image filename, stamp title, stamp comment, and time the stamp was added are separated by byte value 1; each stamp's set of values is separated by byte value 2.
- **Reference4**: 1 if this plugin is running, 0 otherwise.
