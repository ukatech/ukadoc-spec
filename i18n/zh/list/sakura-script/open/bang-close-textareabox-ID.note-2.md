# InputBox 的 ID

确认输入时会触发 [OnUserInput](../../shiori-event/inputbox/OnUserInput.md)，但如果指定的 ID 是以「On」开头的字符串，则会改为触发以该 ID 命名的事件。<br />
在 OnUserInput 中，Reference0 会存放指定的 ID，Reference1 会存放输入内容；而在以 ID 命名的事件中，Reference0 会存放输入内容。<br />

示例<br />
通过 `\![open,inputbox,インプットテスト,10000,テスト入力]` 确认输入时。

- 触发「OnUserInput」
- Reference0 为「インプットテスト」
- Reference1 为输入内容
- Reference2 为输入内容补充信息（仅 sliderinput 有值，为最小值、最大值；其他情况为空）
- Reference3 及之后为通过 --reference= 指定的附加信息

通过 `\!`\[open,inputbox,*On*インプットテスト,10000,テスト入力\] 确认输入时。

- 触发「Onインプットテスト」
- Reference0 为输入内容
- Reference1 为输入内容补充信息（仅 sliderinput 有值，为最小值、最大值；其他情况为空）
- Reference2 及之后为通过 --reference= 指定的附加信息

无论 ID 是什么，按下关闭按钮或超时都会触发 [OnUserInputCancel](../../shiori-event/inputbox/OnUserInputCancel.md)。
