# OnDisplayHandover

**カテゴリ:** OS state event

Occurs when a window is moved across screens. *\[NOTIFY/other GET\]*

- **Reference0**: init (when position initialization is complete) or update (an update after initialization).<br />
  init is notified when the window position is determined after startup; this is not necessarily before OnBoot.
- **Reference1**: 0 for the main ghost, 1 for the partner. SSP/CROW may also use 2 or higher.
- **Reference2**: Before moving: left, top, right, bottom, bit depth, whether it is the primary monitor (0/1). Empty during init.<br />
  Example: 0,0,1600,900,32,1
- **Reference3**: After moving: left, top, right, bottom, bit depth, whether it is the primary monitor (0/1)

**対応:** SSP 2.4.09
