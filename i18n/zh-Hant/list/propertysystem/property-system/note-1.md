# 補充

## ※SHIORI Status 標頭

多個項目可能以逗號(,)分隔回傳，也可能回傳空值。

- **talking**：目前正在執行 script（說話中）。
- **passive**：處於 passive 模式（`\![enter,passivemode]`）。
- **induction**：處於 induction 模式（`\![enter,inductionmode]`）。
- **timecritical**：由 `\t` 標籤鎖定中。
- **nouserbreak**：處於 nouserbreak 模式（`\![enter,nouserbreak]`）。
- **online**：連線中（例如取得 headline 資料、校時或執行自身的 network update）。
- **choosing**：正在顯示由 `\q`、`\__q` 標籤產生的選項。
- **minimizing**：最小化中（化為工作列通知區域圖示）。
- **opening(種類)**：輸入視窗展開中。<br />
  種類欄位會以斜線分隔，列出目前開啟的項目，包括 communicate、input、teach、textarea、dialog。<br />
  例：opening(input/dialog)<br />
  ※SSP 2.3.97 起使用斜線。在此之前以逗號分隔<br />
  ※textarea 自 SSP 2.9.10 起支援
- **balloon(資訊)**：正在顯示 balloon。<br />
  資訊欄位會以(角色 ID)=(balloon ID)的格式列出正在顯示的 balloon。balloon ID 不區分左右（固定為偶數）。<br />
  例：balloon(0=2/1=0)<br />
  ※SSP 2.3.97 起使用斜線。在此之前以逗號分隔

※Status 標頭也可依下列方式從各 SHIORI 取得。

- 華和梨……System.Request.Status 項目
- YAYA……status 變數內
- 里々……資訊取得變數（Status）
