# `\![leave,selectmode]`

**カテゴリ:** Unclassified command

Exit the mode described above. [OnSelectModeComplete](../../shiori-event/select-region-mode/OnSelectModeComplete.md) runs afterward.<br />
If the hit-test region is invalid (not selected), for example, [OnSelectModeCancel](../../shiori-event/select-region-mode/OnSelectModeCancel.md) runs instead.

**対応:** SSP

## 記述例

```sakurascript
\![leave,selectmode]セレクトモードを解除する。
```
