# `\![leave,selectmode]`

**カテゴリ:** Unclassified commands

Exit the mode described above. After execution, [OnSelectModeComplete](../../shiori-event/select-region-mode/OnSelectModeComplete.md) is executed.<br />
If the hit-test region is invalid (not selected), [OnSelectModeCancel](../../shiori-event/select-region-mode/OnSelectModeCancel.md) is executed instead.

**対応:** SSP

## 記述例

```sakurascript
\![leave,selectmode]セレクトモードを解除する。
```
