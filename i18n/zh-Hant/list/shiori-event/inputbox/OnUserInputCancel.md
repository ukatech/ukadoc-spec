# OnUserInputCancel

**カテゴリ:** 輸入框事件

InputBox 關閉時觸發。<br />
逾時且此事件沒有收到回應時，為確保相容性，會傳送 OnUserInput Reference1=timeout。

- **Reference0**: 輸入事件的 ID。
- **Reference1**: 逾時時為 timeout，關閉時為 close。
- **Reference2**: 輸入內容的補充資訊（僅 sliderinput 使用，為最小值、最大值；其他情況為空欄）
- **Reference3～**: 以 --reference= 指定的其他資訊

**対応:** SSP / Ninix
