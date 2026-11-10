# OnWindowModeChange

**カテゴリ:** OS state event

Occurs when the SSP window mode changes. *\[NOTIFY at startup/other GET\]*<br />
Window mode displays ghosts inside a window (container) provided by SSP, rather than on the desktop. The inside of the container serves as the screen for the ghost.<br />
Since the screen size for the ghost changes when the mode switches, [OnDisplayChange](OnDisplayChange.md) also occurs after this event.<br />
The current mode can also be obtained from [baseware.windowmode](../../propertysystem/property-system/baseware.windowmode.md).

- **Reference0**: init (notification at startup) or update (change after startup)
- **Reference1**: Current mode.<br />
  normal: Normal mode (displays ghosts on the desktop)<br />
  shared: Window mode. All ghosts share one container<br />
  perghost: Window mode. Uses one container per ghost
- **Reference2**: Previous mode. The possible values are the same as for Reference1. Empty if Reference0 is init.

**対応:** SSP 2.8.93
