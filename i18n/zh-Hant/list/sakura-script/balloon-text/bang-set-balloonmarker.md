# `\![set,balloonmarker,マーカー表示文字列]`

**カテゴリ:** balloon、文字指令

顯示接收 SSTP 時要顯示的標記文字串。<br />
顯示位置為目前 scope 所屬的 balloon。<br />
顯示文字串可省略。要清除時，請省略引數或留空。

持續有效直到 ghost 結束，或 SSTP 接收等原本會使用此區域的功能啟動。

清除的意思是「取消以此標籤指定的文字串」，並非隱藏標記本身。在播放透過 SSTP 接收的腳本時清除，會恢復為預設的來源顯示（from 來源）。<br />
此外，如果 SSTP 或 SHIORI 的 Marker 標頭已指定標記文字串，則會以該設定為優先，不會顯示此標籤指定的內容。<br />
若要在輸出為圖片時排除標記，請在 [`\![execute,dumpballoon]`](../misc/bang-execute-dumpballoon-ID-prefix-ID.md) 使用 --hide=balloonmarker。

**対応:** SSP 2.6.67
