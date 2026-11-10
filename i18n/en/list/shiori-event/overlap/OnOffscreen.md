# OnOffscreen

**カテゴリ:** Offscreen and overlap events

Occurs when a character's (surface's) window gets caught on or moves outside the monitor (work area). Offscreen.<br />
Notifications are sent whenever the offscreen state changes, so with some effort you can also detect when it is no longer offscreen.

- **Reference0**: ID \[`\1`\] ID \[`\1`\] ID ...<br />
  \[`\1`\] is the byte value 1<br />
  Example: 1 \[`\1`\] 2 indicates that windows 1 and 2 are offscreen.
- **Reference1**: In the same format as Reference0, indicates the state before the change (that is, the Reference0 from the previous event).

**対応:** SSP / Ninix
