# OnTextAreaInputCancel

**カテゴリ:** 輸入框事件

多行輸入框(textareabox)關閉時觸發。<br />
無論 ID 為何，都會觸發此事件。與 OnUserInputCancel 不同，逾時時不會重新傳送至輸入確認事件。

- **Reference0**: textareabox 的 ID。
- **Reference1**: 逾時時為 timeout，關閉時為 close。
- **Reference2**: 關閉前輸入的內容。換行以位元組值 1 的字元(`\1`)分隔。
- **Reference3～**: 以 --reference= 指定的其他資訊

**対応:** SSP 2.9.10
