# InputBox 选项

以 ○○ 的形式指定。即使全部省略也能正常工作。

- **--option=(noclose|noclear)**：noclose：输入后不关闭 inputbox，继续显示。<br />
  noclear：输入后不清空输入内容，继续显示。<br />
  与 noclose 同时指定（例如：`\![inputbox,入力内容,,,--option=noclose,--option=noclear]`）。<br />
  对不输入文字的 inputbox（sliderinput、dateinput、timeinput、ipinput），noclear 无效。
- **--text=默认显示**：最初显示的字符串。<br />
  sliderinput 中为初始值、最小值、最大值；dateinput 中为年、月、日；timeinput 中为时、分、秒
- **--placeholder=提示文字 \[2.9.10\]**：仅在输入栏为空时以浅色显示，用于提示应输入的内容（相当于 HTML 的 placeholder）。输入文字后会消失，清空输入栏后会再次显示。<br />
  与 --text= 不同，它不会包含在输入内容中，也不会计入 --limit= 的字符数。<br />
  文字颜色可以通过气球的 [communicatebox.placeholder.color](../../../descript/balloon/descript-txt/communicatebox.placeholder.color.r.md) 指定。未指定时，颜色会向输入栏文字的背景色靠近，并进一步降低饱和度。<br />
  适用于 inputbox、passwordinput 和 textareabox（即使是 passwordinput，也会直接显示文字而不隐藏）。在 textareabox 中，`\1`表示换行。
- **--timeout=超时毫秒数**：自动关闭输入框前的等待时间。指定零或负数时不会关闭。
- **--balloon=ID**：指定要填入 balloonc?.png/txt 中 ? 位置的 ID，即可使用与该 ID 对应的图像。<br />
  未指定时，每种输入框都有预设的 ID。（SSP 2.6.23）
- **--limit=文字输入长度限制**：限制可在输入框中输入的字符数。
- **--reference=附加信息**：将指定的附加信息添加到 OnUserInput 的 Reference3，或以 On 开头的指定事件的 Reference2 及之后。
