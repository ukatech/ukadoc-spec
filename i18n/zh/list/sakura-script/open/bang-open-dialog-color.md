# `\![open,dialog,color,パラメータ]`

**カテゴリ:** 开放命令

打开颜色调色板对话框。即使在此对话框中指定了颜色，也不会实际执行任何操作。<br />
确认时会触发 SHIORI 事件 [OnSystemDialog](../../shiori-event/dialogbox/OnSystemDialog.md)，reference0 中存放「color」，Reference2 中以「R,G,B」形式存放所选颜色，因此各 ghost 作者需在此处编写并执行实际处理。<br />
关闭时会触发 SHIORI 事件 [OnSystemDialogCancel](../../shiori-event/dialogbox/OnSystemDialogCancel.md)。<br />
参数可以用逗号分隔，指定如下内容。

- **--color=R G B**：分别以 0～255 指定 RGB 值
- **--id=事件ID**：发送给 OnSystemDialog/OnSystemDialogCancel 的 ID<br />
  如果事件 ID 设为以 On 开头的值，则会触发该 ID 对应的事件。Reference 的内容与 OnSystemDialog 相同。<br />
  Reference0 固定为「color」。

**対応:** SSP

## 記述例

```sakurascript
\![open,dialog,color,--color=255 0 0,--id=テストカラーダイアログ]初期表示色が赤のカラーパレットダイアログを表示。
```
