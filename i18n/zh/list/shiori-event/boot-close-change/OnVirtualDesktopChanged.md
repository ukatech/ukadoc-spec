# OnVirtualDesktopChanged

**カテゴリ:** Startup, shutdown, and switching events

Occurs when the virtual desktop is switched.<br />
Currently effective only on Windows 10.<br />
**This is an experimental feature, so its specification may change in the future**.

- **Reference0**: current：The current virtual desktop and the desktop displaying the ghost are the same<br />
  hidden：The virtual desktop has been switched, and the ghost is hidden<br />
  minimize：The window is minimized, and it is unclear which virtual desktop it belongs to
- **Reference1**: Current virtual desktop ID.

**対応:** SSP
