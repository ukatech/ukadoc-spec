# `\![leave,selectmode]`

**カテゴリ:** 未分類コマンド

解除上述模式。執行後會觸發[OnSelectModeComplete](../../shiori-event/select-region-mode/OnSelectModeComplete.md)。<br />
若命中判定區域無效（未選取）等情況，則會觸發[OnSelectModeCancel](../../shiori-event/select-region-mode/OnSelectModeCancel.md)。

**対応:** SSP

## 記述例

```sakurascript
\![leave,selectmode]セレクトモードを解除する。
```
