# `\![open,inputbox,ID,表示時間,テキスト,オプション,...]`

**カテゴリ:** Open commands

Opens an InputBox.<br />
When confirmed (the OK button is pressed), the SHIORI event [OnUserInput](../../shiori-event/inputbox/OnUserInput.md) is triggered.<br />
If the display time elapses (times out), or the dialog is closed using the close button, [OnUserInputCancel](../../shiori-event/inputbox/OnUserInputCancel.md) is triggered.<br />
If there is no response to OnUserInputCancel and the dialog times out, OnUserInput is triggered with "timeout" as the input text for compatibility.<br />
While the user is typing, all other operations used to be blocked, but this is not the case in SSP.

<br />
The ID is stored in OnUserInput when confirmed, but if the ID starts with “On”, an event with that ID is triggered. See [※ID](bang-close-textareabox-ID.note-2.md).<br />
Specify the display time in milliseconds. If omitted or set to 0 or less, the display time is unlimited.<br />
The text is displayed in the box when it opens (not supported in CROW); it is optional.<br />
In SSP only, options can be specified in the form --option=○○; see [※Options](bang-close-textareabox-ID.note.md). This is optional.

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
\![open,inputbox,インプットテスト,10000,テスト入力]「テスト入力」と初期入力されたInputBoxを開く。OKボタンを押すか、10秒経過で自動的に閉じる。
```

```sakurascript
\![open,inputbox,インプットテスト,--timeout=10000,--text=テスト入力] 上記と同じ(新オプション指定)
```

```sakurascript
\![open,inputbox,OnNameInput,--placeholder=あなたの名前] 空欄に「あなたの名前」と薄く表示されたInputBoxを開く。[2.9.10]
```
