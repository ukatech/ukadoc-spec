# `\![open,dialog,color,パラメータ]`

**カテゴリ:** Open command

Open the color palette dialog. Selecting a color in this dialog does not perform any action by itself.<br />
When a selection is confirmed, the SHIORI event [OnSystemDialog](../../shiori-event/dialogbox/OnSystemDialog.md) is triggered. The selected color is stored in Reference2 in the format "R,G,B", and "color" is stored in Reference0. Each ghost author must implement and run the actual processing here.<br />
When the dialog is closed, the SHIORI event [OnSystemDialogCancel](../../shiori-event/dialogbox/OnSystemDialogCancel.md) is triggered.<br />
The following parameters can be specified, separated by commas.

- **--color=R G B**: Specify each RGB value from 0 to 255
- **--id=event ID**: ID to send with OnSystemDialog/OnSystemDialogCancel<br />
  If the event ID starts with On, an event with that ID is triggered. The Reference contents are the same as for OnSystemDialog.<br />
  Reference0 is always set to "color".

**対応:** SSP

## 記述例

```sakurascript
\![open,dialog,color,--color=255 0 0,--id=テストカラーダイアログ]初期表示色が赤のカラーパレットダイアログを表示。
```
