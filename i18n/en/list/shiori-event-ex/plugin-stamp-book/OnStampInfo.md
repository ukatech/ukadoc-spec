# OnStampInfo

**カテゴリ:** Plugin “Stamp Book”

Event that notifies the recipient of information about stamps.<br />
Occurs when a ghost starts, when the plugin is loaded or unloaded, and whenever OnStampInfoCall is sent.

- **Reference0**: Total number of stamps.
- **Reference1**: Whether this ghost has a stamp: 1 if it does, or 0 if it does not.<br />
  This value is less reliable when multiple ghosts are running, so to check it reliably, it is recommended to actively raise this event using OnStampInfoCall.
- **Reference2**: Path to the plugin.
- **Reference3**: Information for all stamps. Each stamp has the ghost name, stamp image file name, stamp title, stamp comment, and time the stamp was added, separated by byte value 1. The stamp entries are separated by byte value 2.
- **Reference4**: 1 if this plugin is running, or 0 otherwise.
