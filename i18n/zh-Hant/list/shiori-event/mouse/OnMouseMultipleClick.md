# OnMouseMultipleClick

**カテゴリ:** 滑鼠事件

連續點擊3次以上時觸發。<br />
※若SHIORI未回應此事件，則會照常回到OnMouseClick和OnMouseDoubleClick的流程。

- **Reference0**: 滑鼠游標的 x 座標（區域座標）
- **Reference1**: 滑鼠游標的 y 座標（區域座標）
- **Reference2**: 固定為0。
- **Reference3**: 本體為0，搭檔為1。之後為2～
- **Reference4**: 命中判定的識別碼。
- **Reference5**: 左鍵點擊為0，右鍵點擊為1
- **Reference6**: 來自支援多點觸控環境中的觸控面板（※不含觸控板）輸入時為touch，來自繪圖板輸入時為pen，來自繪圖板橡皮擦端輸入時為eraser，來自滑鼠等輸入時為mouse
- **Reference7**: 連續點擊次數

**対応:** SSP
