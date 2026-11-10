# `\![leave,selectmode]`

**カテゴリ:** Uncategorized commands

Exit the mode described above. After execution, [OnSelectModeComplete](../../shiori-event/select-region-mode/OnSelectModeComplete.md) is issued.<br />
If the hit-test region is invalid (no region is selected), for example, [OnSelectModeCancel](../../shiori-event/select-region-mode/OnSelectModeCancel.md) is issued.

**対応:** SSP

## 記述例

```sakurascript
\![leave,selectmode]セレクトモードを解除する。
```
