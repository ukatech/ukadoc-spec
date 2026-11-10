# OnDressupChanged

**カテゴリ:** Startup, shutdown, and switching events

This event occurs when dressup is switched.<br />
It may be notified multiple times. In that case, the last OnDressupChanged is *\[GET\]*, and the others are *\[NOTIFY\]*.<br />
Also see [OnNotifyDressupInfo](../notify/OnNotifyDressupInfo.md), which occurs after this event.

**This notification is skipped when the number of dressup flag changes is large (currently 100 elements). Use OnNotifyDressupInfo to receive large numbers of changes.**

- **Reference0**: ID of the character targeted for dressup.
- **Reference1**: Name of the part.
- **Reference2**: 1 when enabled, 0 when disabled.
- **Reference3**: Category name of the part.
- **Reference4**: script when executed from a script, user when executed from a menu \[2.5.90～\]

**対応:** SSP / Ninix
