# IsMediaLoadable

**カテゴリ:** internal_file

檢查 SSP 是否能處理音訊或影片檔案。不載入檔案，根據副檔名進行判定。<br />
判定時使用的元件，與將音訊或影片檔案拖放至 SSP 時，判斷是否可用內建媒體播放器開啟的元件相同（OS 的 DirectShow / Media Foundation 可能播放的副檔名集合）。不檢查檔案內容，因此即使是`read`，也不保證實際上可以播放。<br />
**任何格式的圖片都是`none`**。SSP 內建載入器可讀取的圖片（包含不只根據副檔名，也能從檔案開頭的標頭判定為圖片的情況），以及 OS 的 WIC（例如 HEIC）可讀取副檔名所對應的圖片，即使列在 OS 的 DirectShow 副檔名表中，在此仍會是`none`。也就是說，[IsImageLoadable](internal_file.IsImageLoadable.md)回傳`embed` / `write`的圖片，以及根據副檔名判定為`read`的圖片，在此函式中都是`none`。請使用`IsImageLoadable`檢查圖片是否可讀取。

- **Argument1**: 檔案路徑。相對路徑以 ghost 資料夾（ghost/master）為基準。分隔符可使用`/`或`\`。若在未指定 ghost 的呼叫中傳入相對路徑，會回傳 400（`ghost required`）。檔案不存在（包含資料夾）時，會回傳 400（`file not found`）。不接受 URL。

回應的`Result`表示處理等級，為下列其中一種。

- **none**: 無法讀取。不是音訊或影片（圖片必定屬於此類），或是未支援的格式。
- **read**: 僅供讀取。預期可以播放的格式。
- **embed**: 可載入 ghost 中處理。**目前不會回傳。**
- **write**: 也可寫入。**目前不會回傳。**

使用與[IsImageLoadable](internal_file.IsImageLoadable.md)相同的四種等級名稱。較後面的等級包含前面的等級。由於日後可能會開始回傳`embed`和`write`，建議判斷是否為`none`，而不要判斷是否等於`read`。

## 記述例

```
Argument0: IsMediaLoadable
Argument1: sound/bgm01.mp3

→ 200
　Result: read
```

**対応:** SSP 2.9.27
