# `\![execute,dumpballoon,ディレクトリ,スコープID,prefix,イベントID]`

**カテゴリ:** 未分類コマンド

將指定 scope 的 balloon 目前的繪製內容，以圖片形式輸出至指定目錄。<br />
與 surface 不同，無法指定狀態重新繪製，而是直接輸出當下繪製在 balloon 上的內容。輸出的圖片不會套用放大縮小或半透明（包含淡出），且維持原始尺寸。<br />
即使 balloon 隱藏，只要仍有繪製內容就會輸出。<br />
輸出檔名為 prefix+scope ID+.png（例：balloon0.png）。<br />
scope ID：指定與`\s`標籤相同的 ID。<br />
prefix：（可省略）加在輸出檔名前方的字串。省略時為 balloon。<br />
事件 ID：（可省略）輸出完成後，觸發指定事件。Reference0 會帶有成功輸出的檔案數（0 或 1）。<br />
輸出目的地的限制與`\![execute,dumpsurface]`相同。若超出限制範圍，則不會輸出任何內容，並記錄至錯誤日誌。

\[2.9.08\] 也可以使用以下格式指定。以 -- 開頭的引數順序不限，也可以與上述各引數指定方式混用（不以 -- 開頭的引數會依出現順序視為目錄、scope ID、prefix、事件 ID）。<br />
除目錄外的引數皆可省略，省略 scope ID 時會使用 0。

- **--dir=ディレクトリ**：輸出目的地的目錄。
- **--scope=スコープID**：scope ID。
- **--prefix=prefix**：加在輸出檔名前方的字串。
- **--event=イベントID**：事件 ID。--async= 也相同。
- **--hide=項目**：不繪製指定項目，重新繪製後輸出。這不會影響顯示中的 balloon。指定多個項目時，以逗號分隔，例如 "--hide=balloonmarker,balloonnum"，並以雙引號括住整個引數。<br />
  balloonmarker：SSTP 標記（顯示`\![set,balloonmarker]`，或顯示由 SSTP 接收的 script 來源）<br />
  balloonnum：顯示`\![set,balloonnum]`<br />
  使用此指定時，輸出內容不是當下的繪製內容，而是依當下狀態重新繪製的內容（即使在`\![lock,balloonrepaint]`期間也會重新繪製）。

**対応:** SSP 2.9.02

## 記述例

```sakurascript
SSTPマーカーとballoonnumを除いて、\0のバルーンをdumpフォルダに出力する。\![execute,dumpballoon,--dir=dump,--scope=0,"--hide=balloonmarker,balloonnum"]
```
