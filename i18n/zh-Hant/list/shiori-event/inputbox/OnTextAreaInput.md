# OnTextAreaInput

**カテゴリ:** 輸入框事件

在[多行輸入框(textareabox)](../../sakura-script/open/bang-open-textareabox-ID.md)輸入並確認時觸發。<br />
ID 以「On」開頭時，會改為觸發名稱為該 ID 的事件，並將輸入內容放入 Reference0（後續的 Reference 編號依序提前一位）。規則與[InputBox 的 ID](../../sakura-script/open/bang-close-textareabox-ID.note-2.md)相同。

- **Reference0**: textareabox 的 ID。
- **Reference1**: 輸入的內容。換行以位元組值 1 的字元(`\1`)分隔。
- **Reference2**: 空欄（為了與 OnUserInput 的 Reference 位置對齊）
- **Reference3～**: 以 --reference= 指定的其他資訊

**対応:** SSP 2.9.10
