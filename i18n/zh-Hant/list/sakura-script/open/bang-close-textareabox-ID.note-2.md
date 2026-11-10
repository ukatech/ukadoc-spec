# InputBox 的 ID

按下確定時會觸發 [OnUserInput](../../shiori-event/inputbox/OnUserInput.md)，但若指定以「On」開頭的字串作為 ID，則會改為觸發以該 ID 名稱命名的事件。<br />
在 OnUserInput 中，Reference0 會放入指定的 ID，Reference1 會放入輸入內容；若是以 ID 名稱命名的事件，Reference0 則會放入輸入內容。<br />

範例<br />
使用 `\![open,inputbox,インプットテスト,10000,テスト入力]`並按下確定時。

- 觸發「OnUserInput」
- Reference0 為「インプットテスト」
- Reference1 為輸入內容
- Reference2 為輸入內容補充資訊（僅適用於 sliderinput，內容為最小值、最大值；其他情況為空）
- Reference3 以後為以 --reference= 指定的附加資訊

使用 `\!`\[open,inputbox,*On*インプットテスト,10000,テスト入力\]並按下確定時。

- 觸發「Onインプットテスト」
- Reference0 為輸入內容
- Reference1 為輸入內容補充資訊（僅適用於 sliderinput，內容為最小值、最大值；其他情況為空）
- Reference2 以後為以 --reference= 指定的附加資訊

無論 ID 為何，按下關閉按鈕或逾時時，都會觸發 [OnUserInputCancel](../../shiori-event/inputbox/OnUserInputCancel.md)。
