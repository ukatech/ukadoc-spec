# `\![open,textareabox,ID,表示時間,テキスト,オプション,...]`

**カテゴリ:** 打开命令

打开多行输入框（textareabox）。<br />
确认输入时（按下 OK 按钮或 Ctrl+Enter）会触发 SHIORI 事件[OnTextAreaInput](../../shiori-event/inputbox/OnTextAreaInput.md)。Enter 键用于换行。<br />
超过显示时间（超时）或按下关闭按钮关闭时，会触发[OnTextAreaInputCancel](../../shiori-event/inputbox/OnTextAreaInputCancel.md)。

<br />
输入内容中的换行会以字节值为 1 的字符(`\1`)分隔。文本（初始显示内容）中的换行也同样用`\1`表示。<br />
ID 的处理方式（以「On」开头时会触发以该 ID 命名的事件）与[InputBox 的 ID](bang-close-textareabox-ID.note-2.md)相同。<br />
显示时间、文本的指定以及[※选项](bang-close-textareabox-ID.note.md)与[inputbox](bang-open-inputbox-ID.md)相同，但以下几点除外。<br />
・--limit=会将换行计为 1 个字符。<br />
・--placeholder=(输入为空时淡色显示的提示文字)中的换行也用`\1`表示。<br />
・不能使用输入补全([inputbox.autocomplete](../../shiori-event/inputbox/inputbox.autocomplete.md))。<br />
・省略--balloon=时会使用balloonc5。对于没有balloonc5的 balloon，会以正在说话的角色当前的 balloon 图像为背景，并将 validrect 范围设为输入框（文字字体、大小、颜色也与 balloon 正文相同）。即使是竖排的 balloon，输入框也会横向显示。

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
