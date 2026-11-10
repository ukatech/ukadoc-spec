# OnMouseMultipleClickEx

**カテゴリ:** 滑鼠事件

使用左、右鍵以外的按鍵連續點擊3次以上時觸發。<br />
※若SHIORI未回應此事件，則會照常回到OnMouseClickEx和OnMouseDoubleClickEx的流程。

- **Reference0**: 滑鼠游標的 x 座標（區域座標）
- **Reference1**: 滑鼠游標的 y 座標（區域座標）
- **Reference2**: 固定為0。
- **Reference3**: 本體為0，搭檔為1。之後為2～
- **Reference4**: 命中判定的識別碼。
- **Reference5**: 滾輪點擊（或三鍵滑鼠的中鍵）為middle，擴充按鈕1（通常指定為「上一頁」）為xbutton1，擴充按鈕2（通常指定為「下一頁」）為xbutton2。
- **Reference6**: 來自支援多點觸控環境中的觸控面板（※不含觸控板）輸入時為touch，來自繪圖板輸入時為pen，來自繪圖板橡皮擦端輸入時為eraser，來自滑鼠等輸入時為mouse
- **Reference7**: 連續點擊次數

**対応:** SSP
