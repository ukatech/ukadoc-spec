# OnVirtualDesktopChanged

**カテゴリ:** Startup, shutdown, and switching events

Fires when the virtual desktop is switched.<br />
Currently only works on Windows 10.<br />
**This is an experimental feature, so its specification may change in the future**.

- **Reference0**: current: same as the current virtual desktop and the desktop displaying the ghost<br />
  hidden: the virtual desktop was switched and the ghost is hidden<br />
  minimize: the window is minimized, and it is not possible to determine which virtual desktop it belongs to
- **Reference1**: ID of the current virtual desktop.

**対応:** SSP
