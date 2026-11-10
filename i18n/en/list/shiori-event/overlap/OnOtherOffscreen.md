# OnOtherOffscreen

**カテゴリ:** Offscreen and overlap events

Occurs when any character's (surface's) window, including other characters, gets caught on or moves outside the monitor (work area). Offscreen. The global version of OnOffscreen.<br />
Notifications are sent whenever the offscreen state changes, so with some effort you can also detect when a window is no longer offscreen.<br />
Note that information about your own window is also included.

- **Reference0**: Sakura name/ID \[`\1`\] Sakura name/ID \[`\1`\] Sakura name/ID ...<br />
  \[`\1`\] is the byte value 1<br />
  Example: Emily/1 \[`\1`\] Director-tan/0
- **Reference1**: In the same format as Reference0, indicates the state before the change (that is, the Reference0 from the previous event).

**対応:** SSP / Ninix
