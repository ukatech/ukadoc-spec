# ImageInfo

**カテゴリ:** internal_file

**不載入檔案**（只讀取標頭）即可取得影像檔案的尺寸。只要提供路徑即可讀取，不必建立 surface 等物件。<br />
**視環境而定，可能無法取得資料**。SSP 會先透過 OS 的屬性處理常式（與檔案總管檔案詳細資料中顯示資訊的機制相同）讀取；若無法取得，則由 SSP 自行讀取檔案標頭（不會解碼影像）。可從標頭取得資訊的格式包括 PNG（APNG）/ JPEG / GIF / BMP / TIFF / WebP / ICO・CUR（最大的項目）/ PSD / XCF / PSP（4.0 版以後）/ QOI / PCX / TGA / PBM・PGM・PPM・PAM・PFM / XBM / XPM / MAG / PI。ORA / KRA / CLIP（必須解壓縮內容才能判斷的格式）若沒有 OS 處理常式，則會回傳空值。無法取得資料不會視為錯誤。<br />
從標頭讀取時，TIFF 會使用第一頁的尺寸、GIF 會使用邏輯螢幕尺寸、ICO・CUR 會使用最大項目的尺寸。不會套用 EXIF 方向（旋轉）資訊。<br />
請注意，以同步方式呼叫時，ghost 會在讀取期間停止。讀取時間可能因檔案所在位置（例如網路磁碟機）而有所不同，因此也可考慮使用 [`--async`](../async.md)。

音訊與影片的標籤或長度可使用 [MediaInfo](internal_file.MediaInfo.md) 讀取。

- **Argument1**: 檔案路徑。相對路徑以 ghost 資料夾（ghost/master）為基準。分隔符可使用 `/` 或 `\`。若在沒有 ghost 的情況下呼叫並傳入相對路徑，會回傳 400（`ghost required`）。若檔案不存在（包括資料夾），會回傳 400（`file not found`）。不接受 URL。
- **Argument2 以後**: 要取得的值所對應的鍵。至少必須指定 1 個（未指定任何鍵時會回傳 400 `invalid parameter`），最多可指定 11 個（指定 12 個以上時會回傳 400 `invalid parameter`）。鍵不區分大小寫。

鍵如下。值為十進位整數字串。

- **width / height**: 影像的像素數（px）。

回應的 `Result` 會是 `image`（判定為影像時）或空值。若無法判定為影像（包括音訊與影片檔案），所有 `Value` 都會是空值。<br />
`Value0` 以後的值會依序對應到 `Argument2` 以後指定的鍵。無法取得的值或未知的鍵會回傳**空字串**（不會視為錯誤，也不會回傳實作自訂的鍵）。即使檔案無法讀取或格式不受支援，也不會回傳 400，而是以 200 回應，且 `Result` 和所有 `Value` 都為空值。<br />
回應的字元編碼依照要求中的 `Charset`。

## 記述例

```
Argument0: ImageInfo
Argument1: image/bg01.png
Argument2: width
Argument3: height

→ 200
　Result: image
　Value0: 640
　Value1: 480
```

**対応:** SSP 2.9.27
