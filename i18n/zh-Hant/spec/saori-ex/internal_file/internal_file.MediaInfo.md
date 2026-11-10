# MediaInfo

**カテゴリ:** internal_file

取得音訊・影片檔案的標籤、長度與尺寸，**不載入檔案**（不準備播放，只讀取標頭與標籤）。即使不使用`\![sound]`建立元素，也能只指定路徑讀取。`sound.*`的清單不會增加元素，也不會觸發`OnSound*`事件，且不會建立暫存檔。\[SSP 2.9.27\] 影像尺寸請使用[ImageInfo](internal_file.ImageInfo.md)讀取。不保證將影像檔傳給MediaInfo時的處理方式（SSP從\[SSP 2.9.25\]起維持原樣，也會回傳影像的`Result`・`width` / `height`）。<br />
**視環境而定，可能無法取得**。\[SSP 2.9.32\] 對於MP3等的ID3（v1 / v2.2 / v2.3 / v2.4）、FLAC・Ogg Vorbis・Opus的註解，以及WAV・AVI的INFO標籤，SSP會自行讀取。其他格式（MP4・WMA・MKV / WebM等），以及SSP無法讀取的項目，則會仰賴OS的屬性處理常式（與在檔案總管的檔案詳細資料中顯示資訊時相同的機制）讀取。因此，若OS沒有該格式的處理常式，或處理常式不會回傳部分項目，該值就會是空白（無法與沒有標籤的檔案區分）。無法取得資料不會造成錯誤。<br />
請注意，同步呼叫時，ghost會在讀取期間停止。依檔案所在位置（例如網路磁碟機）而定，讀取可能需要一些時間，因此也請考慮使用[`--async`](../async.md)。

- **Argument1**: 檔案路徑。相對路徑以ghost資料夾（ghost/master）為基準。路徑分隔符可使用`/`或`\`。在沒有ghost的情況下呼叫並傳入相對路徑時，會回傳400（`ghost required`）。檔案不存在（包括資料夾）時，會回傳400（`file not found`）。不接受URL。
- **Argument2以降**: 所需值的鍵。至少必須有1個（若沒有則回傳400 `invalid parameter`），最多11個（12個以上則回傳400 `invalid parameter`）。鍵不區分大小寫。

鍵如下。所有值都是字串（數值為十進位整數）。標籤項目的名稱與意義，和`sound.(要素名).meta.*`相同。

- **title / artist / albumartist / album / genre / comment**: 字串。
- **year**: 4位數西元年。若原始值是完整日期，則取前4位數。
- **track**: 只有曲目編號的整數。不包含總數（若為`3/12`則是`3`）。
- **duration**: 音訊・影片的長度（毫秒）。影像為空白。VBR MP3等格式可能會提供估算值。
- **width / height**: 像素數（px）。影片為影像尺寸。音訊為空白。只有專輯封面等嵌入式封面影像的檔案，不會被視為影片。

回應的`Result`表示種類，可能是`audio`（音訊）或`video`（影片）。若無法判別則為空白。\[SSP 2.9.32\] 即使是OS不會回傳種類的Ogg・Opus・WebM等格式，也會根據檔案內容決定（Matroska / WebM有影像軌時為`video`，沒有時為`audio`）。種類僅供參考，因此即使`Result`為空白，`Value`仍可能有值。請勿依`Result`分支判斷，而應依`Value`是否為空白來判斷。未來可能會增加種類。<br />
`Value0`以後的值，依序對應到`Argument2`以後列出的鍵。無法取得的值・未知的鍵會是**空字串**（不會造成錯誤，也不會回傳實作專用的鍵）。即使格式無法讀取或不受支援，也不會回傳400，而是以200回應，且`Result`與所有`Value`皆為空白。

- 值中的換行會替換成位元組值`0x01`（CRLF也替換成1個`0x01`。只有LF或只有CR時，也各自替換成1個`0x01`）。NUL會被移除。
- 含有多個值的標籤（例如多位演出者）會以` ;  `（分號與半形空白）連接成一個字串。
- 回應字元編碼遵循要求的`Charset`。
- \[SSP 2.9.32\] 在SSP自行讀取的標籤中，未指定字元編碼的項目（ID3v1、ID3v2的ISO-8859-1、WAV・AVI的INFO），SSP會依序使用UTF-8 → Shift_JIS → OS的預設字元編碼進行推定。這只是推定，尤其在非日文OS上，可能會混淆西歐語言與日文。SSP不會自行讀取的格式，其標籤字元編碼推定交由OS處理，可能會發生亂碼。
- 各格式的各個項目能否取得，會因OS環境而異。根據在SSP上的確認結果，在Windows 11的標準環境中，MKV / WebM的大部分標籤與影像尺寸等都無法取得（從\[SSP 2.9.32\]起，WAV標籤與MP3註解由SSP自行讀取，因此可以取得）。

## 記述例

```
Argument0: MediaInfo
Argument1: sound/bgm01.mp3
Argument2: title
Argument3: artist
Argument4: duration
Argument5: --async=OnMediaInfo

→ 204（結果はOnMediaInfoイベントで届く）
　Reference0: OnMediaInfo
　Reference1: audio
　Reference2: internal_file
　Reference3: MediaInfo
　Reference4: タイトル
　Reference5: アーティスト
　Reference6: 215000
```

**対応:** SSP 2.9.25
