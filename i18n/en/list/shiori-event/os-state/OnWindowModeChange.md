# OnWindowModeChange

**カテゴリ:** OS state event

Occurs when SSP's window mode changes. *\[NOTIFY at startup/other GET\]*<br />
Window mode displays ghosts inside a window (container) provided by SSP, rather than on the desktop. The inside of the container serves as the screen for the ghost.<br />
Because the screen size for the ghost changes when the mode changes, [OnDisplayChange](OnDisplayChange.md) also occurs after this event.<br />
The current mode can also be retrieved using [baseware.windowmode](../../propertysystem/property-system/baseware.windowmode.md).

- **Reference0**: init (notification at startup) or update (a change after startup)
- **Reference1**: Current mode.<br />
  normal: Normal mode (displays ghosts on the desktop)<br />
  shared: Window mode; all ghosts share a single container<br />
  perghost: Window mode; each ghost has its own container
- **Reference2**: Previous mode. The possible values are the same as for Reference1. Empty if Reference0 is init.

**対応:** SSP 2.8.93
