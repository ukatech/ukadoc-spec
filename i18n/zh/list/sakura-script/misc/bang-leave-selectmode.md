# `\![leave,selectmode]`

**カテゴリ:** 未分类命令

解除上述模式。执行后会触发[OnSelectModeComplete](../../shiori-event/select-region-mode/OnSelectModeComplete.md)。<br />
如果命中检测区域无效（未选择）等，则会触发[OnSelectModeCancel](../../shiori-event/select-region-mode/OnSelectModeCancel.md)。

**対応:** SSP

## 記述例

```sakurascript
\![leave,selectmode]セレクトモードを解除する。
```
