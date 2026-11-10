# `\![execute,dumpsurface,ディレクトリ,スコープID,サーフェスリスト,prefix,イベントID,ゼロ位置切り出し,アニメーションID]`

**カテゴリ:** 未分類コマンド

將合成完成的 surface 圖片輸出至指定目錄。<br />
未指定事件 ID 時，script 會停止執行，直到處理完成。<br />
scope ID：指定與`\s`標籤相同的 ID。此指定會影響 dressup 狀態等依 scope 而異的處理。<br />
surface 清單：使用與[surface ID 指定](../../../descript/shell-surfaces/surface-brace/caption_surfacebraceid.md)相同的格式，或指定以下項目。<br />
\_\_system_surface_all\_\_：輸出所有可作為 shell 使用的 surface<br />
\_\_system_surface_defined\_\_：只輸出 surfaces.txt 中定義的所有 surface<br />
參考：若要在 Sakura Script 的大括號參數中指定逗號，建議以 " " 括住。<br />
prefix：（可省略）加在輸出檔名前方的字串。省略時為 surface。<br />
事件 ID：（可省略）指定後會在繼續執行 Sakura Script 的同時持續輸出，並在完成後觸發指定事件。Reference0 會帶有成功輸出的檔案數。<br />
零位置裁切：指定 1 時，不論動畫定義為何，一律從 0,0 開始 dump，並忽略負座標部分。<br />
動畫 ID：（可省略）指定後，會在各 surface 的一般圖片（prefix+surface 編號.png）之後，以與`\i[ID]`相同的方式播放該動畫，並從 prefix+surface 編號\_0000.png 開始，以從 0 起算的 4 位數連號輸出每個圖樣的圖片。只能指定一個 ID。詳細資訊與啟動選項 --dump-animation 相同。事件的 Reference0 會帶有包含連號圖片在內的檔案數。\[2.9.05\]<br />
基於安全考量，輸出目的地限制在 SSP 管理的資料夾（ghost 資料夾、balloon 資料夾等由「資料夾」設定指定的位置）之下。<br />
此外，此限制可能會視情況加強，因此建議將輸出目的地限於放置 ghost 自身資料的資料夾之下。<br />
若輸出目的地超出限制範圍，則不會輸出任何內容，並記錄至錯誤日誌。

\[2.9.08\] 也可以使用以下格式指定。以 -- 開頭的引數順序不限，也可以與上述各引數指定方式混用（不以 -- 開頭的引數會依出現順序視為目錄、scope ID、surface 清單、prefix、事件 ID、零位置裁切、動畫 ID）。<br />
除目錄外的引數皆可省略，省略 scope ID 時會使用 0。

- **--dir=ディレクトリ**：輸出目的地的目錄。
- **--scope=スコープID**：scope ID。
- **--surface=サーフェスリスト**：surface 清單。包含逗號時，請以雙引號括住整個引數，例如 "--surface=0,10"。
- **--prefix=prefix**：加在輸出檔名前方的字串。
- **--event=イベントID**：事件 ID。--async= 也相同。
- **--fromzero=真偽値**：零位置裁切。
- **--animation=アニメーションID**：動畫 ID。

**対応:** SSP \[2.5.98\]

## 記述例

```sakurascript
\0のサーフェス0～9をdumpフォルダに出力する。\![execute,dumpsurface,--dir=dump,--scope=0,"--surface=0-9"]
```
