# OnMouseDown

**カテゴリ:** 滑鼠事件

按下滑鼠左鍵或右鍵時會發生。

- **Reference0**: 滑鼠游標的 x 座標（區域座標）
- **Reference1**: 滑鼠游標的 y 座標（區域座標）
- **Reference2**: 一律為 0。
- **Reference3**: 本體為 0，搭檔為 1。SSP/CROW 中也可能有 2 以上的值。
- **Reference4**: 命中測試識別碼。
- **Reference5**: 左鍵點擊為 0，右鍵點擊為 1，中鍵點擊為 2（相容規格：建議改用 OnMouseClickEx）。
- **Reference6**: 從支援多點觸控環境的觸控面板（※不包括觸控板）輸入時為 touch，從繪圖板輸入時為 pen，從繪圖板的橡皮擦端輸入時為 eraser，從滑鼠等裝置輸入時為 mouse

**対応:** SSP / Ninix
