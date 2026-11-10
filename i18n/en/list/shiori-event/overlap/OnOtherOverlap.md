# OnOtherOverlap

**カテゴリ:** Offscreen and overlap events

Occurs when the windows of any running characters' (surfaces') overlap, including other characters. The global version of OnOverlap.<br />
Notifications are sent whenever the overlap state changes, so with some effort you can also detect when the windows no longer overlap.<br />
Note that information about your own window is also included.

- **Reference0**: Sakura name/ID-Sakura name/ID \[`\1`\] Sakura name/ID-Sakura name/ID \[`\1`\] Sakura name/ID-Sakura name/ID ...<br />
  \[`\1`\] is the byte value 1<br />
  Example: Emily/0-Mari/1 \[`\1`\] Mari/0-Director-tan/1
- **Reference1**: In the same format as Reference0, indicates the state before the change (that is, the Reference0 from the previous event).

**対応:** SSP / Ninix
