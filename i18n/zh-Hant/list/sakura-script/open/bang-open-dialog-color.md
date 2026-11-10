# `\![open,dialog,color,パラメータ]`

**カテゴリ:** 開啟命令

開啟色彩選擇器對話方塊。在此對話方塊中指定顏色，不會直接執行任何操作。<br />
按下確定時會觸發 SHIORI 事件 [OnSystemDialog](../../shiori-event/dialogbox/OnSystemDialog.md)，Reference0 會存放「color」，Reference2 會以「R,G,B」格式存放選取的顏色，因此各 ghost 作者需在此建立並執行實際處理。<br />
關閉時會觸發 SHIORI 事件 [OnSystemDialogCancel](../../shiori-event/dialogbox/OnSystemDialogCancel.md)。<br />
參數可用逗號分隔，指定如下。

- **--color=R G B**: RGB 各以 0～255 指定
- **--id=事件 ID**: 傳送至 OnSystemDialog/OnSystemDialogCancel 的 ID<br />
  若事件 ID 以 On～ 開頭，則會觸發該 ID 的事件。Reference 的內容與 OnSystemDialog 相同。<br />
  Reference0 固定為「color」。

**対応:** SSP

## 記述例

```sakurascript
\![open,dialog,color,--color=255 0 0,--id=テストカラーダイアログ]初期表示色が赤のカラーパレットダイアログを表示。
```
