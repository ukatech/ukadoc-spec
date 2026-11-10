# `\![open,dialog,open,パラメータ]`

**カテゴリ:** 開啟指令

開啟檔案開啟對話框。在此對話框中選取檔案，不會實際開啟檔案。<br />
按下確定時會觸發 SHIORI 事件[OnSystemDialog](../../shiori-event/dialogbox/OnSystemDialog.md)，reference0 會存入「open」，Reference2 會存入檔案路徑，因此各 ghost 作者須在此處實作並執行實際處理。<br />
關閉時會觸發 SHIORI 事件[OnSystemDialogCancel](../../shiori-event/dialogbox/OnSystemDialogCancel.md)。<br />
以逗號分隔，可指定多個[參數設定方式請見後述](bang-open-dialog-color.note.md)。

**対応:** SSP

## 記述例

```sakurascript
\![open,dialog,open,--title=オープンダイアログ表示テスト,--dir=C:/SSP/ghost/emily4/ghost/master,--filter=辞書ファイル|dic*.txt;*.dic;*.aym;*.kis|全てのファイル|*.*,--id=テストダイアログ]SSPがCドライブ直下に、SSPという名前のフォルダで存在する場合、Emily/Phase4.5の[実行したゴーストのフォルダ]/ghost/masterを初期位置とし、dic～.txtと～.dicと～.aymと～.kisのファイルのみ表示する。
```
