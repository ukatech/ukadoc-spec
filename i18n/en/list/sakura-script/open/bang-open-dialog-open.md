# `\![open,dialog,open,パラメータ]`

**カテゴリ:** Open command

Opens a file selection dialog. Selecting a file in this dialog does not actually open the file.<br />
When confirmed, the SHIORI event [OnSystemDialog](../../shiori-event/dialogbox/OnSystemDialog.md) is raised, with "open" stored in reference0 and the file path stored in Reference2. Each ghost author must implement and run the actual processing here.<br />
When the dialog is closed, the SHIORI event [OnSystemDialogCancel](../../shiori-event/dialogbox/OnSystemDialogCancel.md) is raised.<br />
[Specify multiple parameters as described below](bang-open-dialog-color.note.md), separated by commas.

**対応:** SSP

## 記述例

```sakurascript
\![open,dialog,open,--title=オープンダイアログ表示テスト,--dir=C:/SSP/ghost/emily4/ghost/master,--filter=辞書ファイル|dic*.txt;*.dic;*.aym;*.kis|全てのファイル|*.*,--id=テストダイアログ]SSPがCドライブ直下に、SSPという名前のフォルダで存在する場合、Emily/Phase4.5の[実行したゴーストのフォルダ]/ghost/masterを初期位置とし、dic～.txtと～.dicと～.aymと～.kisのファイルのみ表示する。
```
