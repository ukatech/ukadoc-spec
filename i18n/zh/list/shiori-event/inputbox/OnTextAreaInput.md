# OnTextAreaInput

**カテゴリ:** 输入框事件

在[多行输入框(textareabox)](../../sakura-script/open/bang-open-textareabox-ID.md)中输入并确认时触发。<br />
如果ID以「On」开头，则会触发以该ID命名的事件，而非此事件；输入内容会放入Reference0（之后的Reference编号依次前移）。规则与[InputBox的ID](../../sakura-script/open/bang-close-textareabox-ID.note-2.md)相同。

- **Reference0**: textareabox的ID。
- **Reference1**: 输入内容。换行以字节值1的字符(`\1`)分隔。
- **Reference2**: 空白（用于与OnUserInput的Reference位置对齐）
- **Reference3～**: 由--reference=指定的附加信息

**対応:** SSP 2.9.10
