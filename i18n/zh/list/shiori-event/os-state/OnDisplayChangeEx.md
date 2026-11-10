# OnDisplayChangeEx

**カテゴリ:** OS state event

Occurs when the screen resolution/color depth changes. Supports multiple monitors. *\[NOTIFY at startup/GET otherwise\]*

- **Reference0**: init (startup notification) or update (update after startup)
- **Reference1～**: left, top, right, bottom, bit depth, whether this is the primary monitor (0/1), taskbar position (left,top,right,bottom,unknown), coordinates separating the taskbar and work area<br />
  Example: 0,0,1600,900,32,1,bottom,1560<br />
  In [window mode](OnWindowModeChange.md), there is only one entry, treating the container's client area as a single screen (example: 0,0,1280,720,32,1,unknown,0). It does not occur when the physical monitor changes; it occurs when the container is resized or window mode is switched.

**対応:** SSP 2.4.09/taskbar is 2.6.35
