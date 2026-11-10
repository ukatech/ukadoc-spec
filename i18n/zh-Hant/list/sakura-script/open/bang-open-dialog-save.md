# `\![open,dialog,save,パラメータ]`

**カテゴリ:** 開啟指令

開啟檔案儲存對話框。在此對話框中執行儲存，不會實際儲存任何內容。<br />
按下確定時會觸發 SHIORI 事件[OnSystemDialog](../../shiori-event/dialogbox/OnSystemDialog.md)，reference0 會存入「save」，Reference2 會存入檔案路徑，因此各 ghost 作者須在此處實作並執行實際處理。<br />
關閉時會觸發 SHIORI 事件[OnSystemDialogCancel](../../shiori-event/dialogbox/OnSystemDialogCancel.md)。<br />
以逗號分隔，可指定多個[參數設定方式請見後述](bang-open-dialog-color.note.md)。

**対応:** SSP

## 記述例

```sakurascript
\![open,dialog,save,--title=セーブダイアログ表示テスト,--dir=__system_mydocument__,--filter=テキストファイル|*.txt;*.dic,--ext=txt,--name=test,--id=テスト保存ダイアログ]マイドキュメントを初期位置として、.txtと.dicのファイルのみを表示し、初期ファイル名「test.txt」の保存ダイアログを開く。
```
