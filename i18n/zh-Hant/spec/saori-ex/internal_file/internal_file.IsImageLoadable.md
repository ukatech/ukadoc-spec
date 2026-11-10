# IsImageLoadable

**カテゴリ:** internal_file

檢查 SSP 能處理到何種程度的圖片檔案。不載入檔案，根據標頭與副檔名進行判定。供 ghost 事先確認檔案是否可作為 surface 或 balloon 圖片使用，以及是否可以儲存。<br />
判定時使用的元件，與將圖片檔案拖放至 SSP 時，判斷是否可用內建圖片檢視器開啟的元件相同。

- **Argument1**: 檔案路徑。相對路徑以 ghost 資料夾（ghost/master）為基準。分隔符可使用`/`或`\`。若在未指定 ghost 的呼叫中傳入相對路徑，會回傳 400（`ghost required`）。檔案不存在（包含資料夾）時，會回傳 400（`file not found`）。不接受 URL。

回應的`Result`表示處理等級，為下列其中一種。

- **none**: 無法讀取。不是圖片，或是未支援的格式。
- **read**: 僅供讀取。無法保證能作為 ghost 或 balloon 素材載入並處理，但可讀取的格式。在 SSP 中，這類格式是內建載入器無法讀取，但 OS 的圖片編解碼器（WIC）可以讀取的格式。可在檢視器等程式中顯示，但只會顯示第一格，且不保證可作為 surface 等素材使用。
- **embed**: 可載入 ghost 或 balloon 中處理。可作為 surface 或 balloon 圖片使用的格式。在 SSP 中，這類格式是內建載入器可讀取的格式。
- **write**: 也可寫入。除了 embed 以外，還包含 SSP 可用該格式儲存圖片的格式（PNG / BMP / JPEG / WebP）。不包含動畫 PNG 與加密 PNG。

較後面的等級包含前面的等級（`write`也屬於`embed`）。判定時與實際載入器相同，優先使用檔案開頭的標頭；若無法從標頭判定，則參照副檔名。EXE / DLL（用於擷取圖示）不視為圖片。<br />
適用的等級可能會依 SSP 版本或 OS 環境而異。日後可能會增加等級。

## 記述例

```
Argument0: IsImageLoadable
Argument1: image/bg01.png

→ 200
　Result: write
```

**対応:** SSP 2.9.27
