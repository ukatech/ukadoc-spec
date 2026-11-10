# OnMouseWheel

**カテゴリ:** 滑鼠事件

滑鼠滾輪轉動時觸發。<br />
自SSP2.3.53起，在觸控面板環境中，若SHIORI未回應Reference5為up或down的[OnMouseGesture](OnMouseGesture.md)（回傳204 No Content），也會觸發OnMouseWheel作為替代事件。此時Reference2的數值會根據原本OnMouseGesture的移動量及up、down方向轉換（up為正數，down為負數）。

- **Reference0**: 滑鼠游標的 x 座標（區域座標）
- **Reference1**: 滑鼠游標的 y 座標（區域座標）
- **Reference2**: 滑鼠滾輪的轉動量與方向。
- **Reference3**: 本體為0，搭檔為1。SSP/CROW中也有2以上的值。
- **Reference4**: 命中判定的識別碼。
- **Reference5**: ※僅限SSP/NINIX　固定為0。
- **Reference6**: ※僅限SSP/NINIX　來自支援多點觸控環境中的觸控面板（※不含觸控板）輸入時為touch，來自繪圖板輸入時為pen，來自繪圖板橡皮擦端輸入時為eraser，來自滑鼠等輸入時為mouse

**対応:** Materia / SSP / CROW / Ninix
