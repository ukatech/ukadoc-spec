# `\![open,dialog,color,パラメータ]`

**カテゴリ:** Open command

Open the color palette dialog. Selecting a color in this dialog does not perform any action by itself.<br />
When a selection is confirmed, the SHIORI event [OnSystemDialog](../../shiori-event/dialogbox/OnSystemDialog.md) is triggered. Reference0 contains "color", and Reference2 contains the selected color in "R,G,B" format. Each ghost author must implement and run the actual processing here.<br />
When the dialog is closed, the SHIORI event [OnSystemDialogCancel](../../shiori-event/dialogbox/OnSystemDialogCancel.md) is triggered.<br />
The following parameters can be specified as comma-separated values.

- **--color=R G B**: Specify each RGB value from 0 to 255.
- **--id=event ID**: ID to send with OnSystemDialog/OnSystemDialogCancel.<br />
  If the event ID begins with On~, an event with that ID is triggered. The Reference contents are the same as for OnSystemDialog.<br />
  Reference0 is fixed to "color".

**対応:** SSP

## 記述例

```sakurascript
\![open,dialog,color,--color=255 0 0,--id=テストカラーダイアログ]初期表示色が赤のカラーパレットダイアログを表示。
```
