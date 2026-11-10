# OnOverlap

**カテゴリ:** Offscreen and overlap events

Occurs when a character's (surface's) window overlaps another window.<br />
Notifications are sent whenever the overlap state changes, so with some effort you can also detect when the windows no longer overlap.

- **Reference0**: ID-ID \[`\1`\] ID-ID \[`\1`\] ID-ID ...<br />
  \[`\1`\] is the byte value 1<br />
  Example: 0-1 \[`\1`\] 0-2 indicates that window 0 overlaps window 1 and window 0 overlaps window 2.
- **Reference1**: In the same format as Reference0, indicates the state before the change (that is, the Reference0 from the previous event).

**対応:** SSP / Ninix
