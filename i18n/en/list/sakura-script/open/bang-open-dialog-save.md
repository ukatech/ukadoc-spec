# `\![open,dialog,save,パラメータ]`

**カテゴリ:** Open command

Opens a file save dialog. Saving a file in this dialog does not actually save anything.<br />
When confirmed, the SHIORI event [OnSystemDialog](../../shiori-event/dialogbox/OnSystemDialog.md) is raised, with "save" stored in reference0 and the file path stored in Reference2. Each ghost author must implement and run the actual processing here.<br />
When the dialog is closed, the SHIORI event [OnSystemDialogCancel](../../shiori-event/dialogbox/OnSystemDialogCancel.md) is raised.<br />
[Specify multiple parameters as described below](bang-open-dialog-color.note.md), separated by commas.

**対応:** SSP

## 記述例

```sakurascript
\![open,dialog,save,--title=セーブダイアログ表示テスト,--dir=__system_mydocument__,--filter=テキストファイル|*.txt;*.dic,--ext=txt,--name=test,--id=テスト保存ダイアログ]マイドキュメントを初期位置として、.txtと.dicのファイルのみを表示し、初期ファイル名「test.txt」の保存ダイアログを開く。
```
