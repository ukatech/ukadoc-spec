# `\![open,textareabox,ID,表示時間,テキスト,オプション,...]`

**カテゴリ:** Open command

Open a multiline input box (textareabox).<br />
When input is confirmed (by pressing the OK button or Ctrl+Enter), the SHIORI event [OnTextAreaInput](../../shiori-event/inputbox/OnTextAreaInput.md) occurs. The Enter key inserts a line break.<br />
If the display time elapses (timeout) or the box is closed using the close button, [OnTextAreaInputCancel](../../shiori-event/inputbox/OnTextAreaInputCancel.md) occurs.

<br />
Line breaks in the input are passed as characters with byte value 1 (`\1`) as separators. The same applies to the text (initially displayed content): `\1` represents a line break.<br />
The handling of ID (when it begins with “On”, an event with that ID name occurs) is the same as for [InputBox IDs](bang-close-textareabox-ID.note-2.md).<br />
The display time, text, and [※options](bang-close-textareabox-ID.note.md) are the same as for [inputbox](bang-open-inputbox-ID.md), except for the following points.<br />
・--limit= counts line breaks as one character.<br />
・--placeholder=(text displayed faintly when the field is empty) also uses `\1` to represent line breaks.<br />
・Input completion ([inputbox.autocomplete](../../shiori-event/inputbox/inputbox.autocomplete.md)) is unavailable.<br />
・If --balloon= is omitted, balloonc5 is used. If the balloon does not have balloonc5, the current balloon image of the speaking character is used as the background, and the validrect area is used as the input field (the text font, size, and color are also those of the balloon text). The input field is horizontal even in a vertical-writing balloon.

**対応:** SSP 2.9.10

## 記述例

```sakurascript
\![open,textareabox,感想,--timeout=300000] 複数行の入力ボックスを開く。5分でタイムアウトする。
```

```sakurascript
\![open,textareabox,OnDiaryInput,--limit=400] 決定時にOnDiaryInputが発生する。改行込みで400文字まで。
```

```sakurascript
\![open,textareabox,OnDiaryInput,--placeholder=今日の出来事(Ctrl+Enterで決定)] 空欄に案内文を薄く表示する。
```
