# `\![open,dialog,folder,パラメータ]`

**カテゴリ:** 開啟指令

開啟選擇資料夾的對話框。在此對話框中選取資料夾，不會實際執行任何操作。<br />
按下確定時會觸發 SHIORI 事件[OnSystemDialog](../../shiori-event/dialogbox/OnSystemDialog.md)，reference0 會存入「folder」，Reference2 會存入資料夾路徑，因此各 ghost 作者須在此處實作並執行實際處理。<br />
關閉時會觸發 SHIORI 事件[OnSystemDialogCancel](../../shiori-event/dialogbox/OnSystemDialogCancel.md)。<br />
以逗號分隔，可指定多個[參數設定方式請見後述](bang-open-dialog-color.note.md)。

**対応:** SSP

## 記述例

```sakurascript
\![open,dialog,folder,--title=フォルダ選択ダイアログ表示テスト,--id=OnTestFolderDialog]ダイアログで前回開いた場所を初期位置として、フォルダ選択ダイアログを開く。保存ボタンを押すと、指定したID名が「OnTestFolderDialog」でOnで始まっているため、同名のSHIORIイベントOnTestFolderDialogが通知される。
```
