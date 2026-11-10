# `\![open,inputbox,ID,表示時間,テキスト,オプション,...]`

**カテゴリ:** 打开命令

打开InputBox。<br />
确认时（按下OK按钮）会触发SHIORI事件[OnUserInput](../../shiori-event/inputbox/OnUserInput.md)。<br />
超过显示时间（超时）或按关闭按钮关闭时，会触发[OnUserInputCancel](../../shiori-event/inputbox/OnUserInputCancel.md)。<br />
如果OnUserInputCancel没有响应，并且因显示时间到期而超时，为确保兼容性，会触发OnUserInput，并将输入文本设为"timeout"。<br />
输入过程中曾会禁止其他所有操作，但SSP中没有此限制。

<br />
ID会存放在确认时触发的OnUserInput中；如果ID以“On”开头，则会触发以该ID命名的事件。参见[※ID](bang-close-textareabox-ID.note-2.md)。<br />
显示时间以毫秒为单位指定。省略或指定小于等于0的数值时，显示时间不受限制。<br />
文本是在展开输入框后预先显示的文本（CROW不支持），可以省略。<br />
仅SSP支持以--option=○○的格式指定[※选项](bang-close-textareabox-ID.note.md)，可以省略。

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
