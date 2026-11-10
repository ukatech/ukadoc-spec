# OnSelectModeComplete

**カテゴリ:** Selection region mode events

Occurs when rectangle selection mode is exited after `\![leave,selectrect]` is executed.

- **Reference0**: 0 for the main character, 1 for the partner. SSP/CROW may also use 2 or higher.
- **Reference1**: Selection mode. Currently only "rect".
- **Reference2**: Selection result (rectangle). Coordinates are comma-separated in the order left,top,right,bottom.

**対応:** SSP
