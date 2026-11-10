# InputBox 選項

以 ○○ 的形式指定。即使不指定任何選項也能運作。

- **--option=(noclose|noclear)**: noclose：輸入後不關閉 inputbox，繼續顯示。<br />
  noclear：輸入後不清除輸入內容，繼續顯示。<br />
  與 noclose 同時指定（範例：`\![inputbox,入力内容,,,--option=noclose,--option=noclear]`）。<br />
  noclear 對不輸入文字的 inputbox（sliderinput、dateinput、timeinput、ipinput）沒有作用。
- **--text=預設顯示內容**: 從一開始就要顯示的字串。<br />
  sliderinput 為初始值、最小值、最大值／dateinput 為年、月、日／timeinput 為時、分、秒
- **--placeholder=提示文字 \[2.9.10\]**: 只有在輸入欄為空時才會淡色顯示，用來說明應輸入的內容（相當於 HTML 的 placeholder）。輸入文字後會消失，清空輸入欄後會再次顯示。<br />
  與 --text= 不同，此文字不會包含在輸入內容中，也不會計入 --limit= 的字元數。<br />
  文字顏色可透過 balloon 的 [communicatebox.placeholder.color](../../../descript/balloon/descript-txt/communicatebox.placeholder.color.r.md) 指定。若未指定，文字顏色會調整為接近輸入欄背景色且飽和度更低的顏色。<br />
  適用於 inputbox、passwordinput、textareabox（passwordinput 也會直接顯示文字，不會以遮蔽字元取代）。在 textareabox 中，以 `\1` 表示換行。
- **--timeout=逾時毫秒數**: 輸入方塊自動關閉前等待的時間。指定零或負數時不會關閉。
- **--balloon=ID**: 指定要填入 balloonc?.png/txt 中 ? 的 ID，會使用與該 ID 對應的圖片。<br />
  若未指定，則會使用各輸入方塊預設的 ID。（SSP 2.6.23）
- **--limit=文字輸入限制長度**: 限制輸入方塊可輸入的字元數。
- **--reference=附加資訊**: 將指定的附加資訊加入 OnUserInput 的 Reference3，或加入以 On 開頭的指定事件之 Reference2 以後。
