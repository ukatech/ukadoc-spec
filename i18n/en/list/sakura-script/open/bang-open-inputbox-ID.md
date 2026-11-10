# `\![open,inputbox,ID,表示時間,テキスト,オプション,...]`

**カテゴリ:** Open command

Open an InputBox.<br />
When confirmed (by pressing the OK button), the SHIORI event [OnUserInput](../../shiori-event/inputbox/OnUserInput.md) is raised.<br />
If the display time elapses (times out), or if the box is closed with the close button, [OnUserInputCancel](../../shiori-event/inputbox/OnUserInputCancel.md) is raised.<br />
If there is no response to OnUserInputCancel and the display time has elapsed, OnUserInput is raised with "timeout" as the input text for compatibility.<br />
Input used to block all other operations while being entered, but this is not the case in SSP.

<br />
The ID is stored in OnUserInput, which is raised upon confirmation. If the ID begins with "On", an event named after the ID is raised. See [※ID](bang-close-textareabox-ID.note-2.md).<br />
Specify the display time in milliseconds. If omitted or set to a value of 0 or less, the display time is unlimited.<br />
The text is the text displayed in the box immediately after it opens (not available in CROW); it is optional.<br />
In SSP only, options can be specified in the form --option=○○. See [※Options](bang-close-textareabox-ID.note.md). This is optional.

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
