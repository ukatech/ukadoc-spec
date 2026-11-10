# OnTextAreaInputCancel

**カテゴリ:** 输入框事件

多行输入框(textareabox)关闭时触发。<br />
无论ID为何，都会触发此事件。与OnUserInputCancel不同，超时时不会重新触发输入确认事件。

- **Reference0**: textareabox的ID。
- **Reference1**: 超时时为timeout，关闭时为close。
- **Reference2**: 关闭前输入的内容。换行以字节值1的字符(`\1`)分隔。
- **Reference3～**: 由--reference=指定的附加信息

**対応:** SSP 2.9.10
