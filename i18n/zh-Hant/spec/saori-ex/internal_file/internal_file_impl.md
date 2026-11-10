# MediaInfo 實作備註（供 baseware 開發者參考）

MediaInfo 的範圍限定在其他 OS 的 baseware 也能利用現有元件（ffprobe / libavformat、TagLib、OS 標準的媒體 API 等）輕鬆實作的程度。

- **必須遵守（MUST）**：上列鍵名、單位與格式；無法取得的值設為空字串；值的格式化（換行的`0x01`、移除 NUL）；相對路徑的基準（ghost/master）；回應格式（`Result` + `Value0..`）；規格中沒有的鍵設為空，不回傳自訂鍵；接受以`/`作為路徑分隔符。
- **建議遵守（SHOULD）**：也接受以`\`作為路徑分隔符（ghost 作者會使用`\`撰寫，但在其他 OS 上`\`可能是一般檔名字元）。多個值的標籤以` ;  `連接。
- **可依實作而異**：支援的格式（ICO、HEIC 等額外格式，能取得時可回傳，無法取得也不算故障）、原始標籤字元編碼的推定、VBR 長度的精確度、`Result`的判定方式、各格式可取得的項目。規格不決定各格式標籤的對應方式（例如 ID3v2 的`TIT2`對應為`title`）。
- **符合性確認方式**：有回傳值時，值必須正確。沒有回傳值（空白）也算合格。`duration`允許誤差（參考值為 ±100 毫秒或 1%）。

使用 ffprobe / libavformat 實作時的參考：

- `duration`使用`format.duration`。`width` / `height`在影片中使用影像串流的值。
- Ogg 或 Opus 標籤位於`streams[].tags`，而不是`format.tags`。
- MP3 或 M4A 的內嵌封面圖片會以附有`attached_pic`的影像串流回報。若將其計為影片，音訊就會變成`video`。
- `track`（`3/12`格式）和`date`（`2024-05-06`格式）必須整理成規格中的`track`（僅曲目編號）和`year`（前 4 位數字）格式。

## 實作 ImageInfo / IsMediaLoadable / IsImageLoadable 時

- **ImageInfo**遵守與 MediaInfo 相同的規則（鍵、單位、無法取得的值設為空字串、路徑處理）。只有在能取得圖片本身的像素數時，才將`Result`設為`image`；音訊和影片檔案的所有`Value`都設為空。
- **IsMediaLoadable / IsImageLoadable**的 4 個階段（`none` / `read` / `embed` / `write`）代表該 baseware 本身的能力。`embed`是指「能在 ghost 或 balloon 中載入並處理」（能將素材讀取為 surface、balloon 圖片或`\![sound]`音訊等）；`write`是指「能以該格式輸出」。`read`是為「可以讀取，但不保證能載入並處理」的格式而設的階段；在 SSP 中，這類格式沒有內建載入器，而是交由 OS 編解碼器處理。如果實作是使用自有載入器讀取素材，則大多數可讀取的格式都會屬於`embed`；若沒有屬於`read`的格式，就不必回傳`read`。較高階段包含較低階段。
- 不限制判定依據（標頭或副檔名）。檔案不存在或目標是資料夾時，回傳 400（`file not found`）；其他情況不要回傳錯誤，無法讀取時則回傳`none`。
