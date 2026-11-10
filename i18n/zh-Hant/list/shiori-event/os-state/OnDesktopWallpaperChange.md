# OnDesktopWallpaperChange

**カテゴリ:** OS 狀態事件

OS 端變更桌面桌布時觸發。*\[啟動時NOTIFY/其他GET\]*<br />
除了使用者在個人化設定等處變更桌布之外，透過投影片播放或 Windows 聚焦自動更換桌布，以及切換佈景主題時也會觸發。<br />
投影片播放和聚焦最短會每隔1分鐘自動切換一次，因此若由這兩者觸發，即使在啟動後也會以 NOTIFY（無法發話）通知。<br />
這與透過影像檔 DnD 變更桌布時的[OnWallpaperChange](../file-drop/OnWallpaperChange.md)是不同事件；若 SSP 自行變更桌布（Reference1 為 self），則兩個事件都會觸發。若同時處理兩者，請注意避免重複處理。<br />
在[視窗模式](OnWindowModeChange.md)中，對 ghost 而言，桌布就是容器的背景。OS 端變更桌布時，只有容器背景為「桌面」才會觸發；背景為白、灰、黑或影像時則不會觸發。相對地，容器背景切換時（容器選單、[`\![set,wallpaper]`](../../sakura-script/event/bang-set-wallpaper.md)、[`\![restore,wallpaper]`](../../sakura-script/event/bang-restore-wallpaper.md)），以及切換視窗模式使 ghost 所見的背景改變時，會觸發此事件。僅重新選取相同背景不會觸發。<br />
若為 perghost（每個 ghost 使用一個容器），只有自己所在容器的背景變更時才會觸發。

- **Reference0**: init（啟動時通知）或 update（啟動後變更）
- **Reference1**: 變更原因。<br />
  user：使用者變更<br />
  slideshow：投影片播放自動切換<br />
  spotlight：Windows 聚焦自動更新<br />
  theme：因切換佈景主題而變更<br />
  self：由 SSP 自行變更（影像 DnD・從設定檔還原）<br />
  unknown：確定已變更，但無法判別原因<br />
  在視窗模式中，由容器選單或切換視窗模式造成的變更為 user；由 `\![set,wallpaper]`・`\![restore,wallpaper]` 造成的變更為 self。若啟動時通知（init）時容器背景不是「桌面」，則為 unknown。
- **Reference2**: 目前桌布影像的完整路徑。若為單色背景或無法取得，則為空。<br />
  依 Windows 的規格，路徑可能是 OS 建立的快取（TranscodedWallpaper 或聚焦快取），而非使用者選取的原始影像檔案。<br />
  在視窗模式中，若容器背景為「桌面」，則為 OS 端的桌布；若為影像，則為該影像的完整路徑；若為白、灰、黑或未指定影像的純色，則為空。
- **Reference3**: 前一張桌布影像的完整路徑。若 Reference0 為 init，則為空。
- **Reference4**: 顯示樣式。為 center / tile / stretch / fit / fill / span 之一。<br />
  在視窗模式中，若容器背景為影像，也可能是 stretch-x / stretch-y。若為白、灰、黑，則為 center。
- **Reference5**: 桌面的背景色。即桌布空白處顯示的顏色。以半形逗號分隔的 R,G,B。<br />
  在視窗模式中，若容器背景為影像，則為其底色（若有指定顏色則採用該色，否則依影像計算）；若為白、灰、黑，則為該顏色。
- **Reference6～**: 依照以下格式，接續列出與螢幕數量相同筆數的各螢幕桌布資訊。\[`\1`\]代表位元組值1。<br />
  螢幕編號\[`\1`\]桌布影像的完整路徑\[`\1`\]顯示樣式<br />
  螢幕編號的順序對應[OnDisplayChangeEx](OnDisplayChangeEx.md)的 Reference1～順序（Reference1 為螢幕編號0）。<br />
  OS 不會為各螢幕個別保存顯示樣式，因此目前所有值都相同（與 Reference4 相同）。<br />
  無法處理各螢幕桌布的環境（Windows 7 以前）不會提供 Reference6 以後的資料。<br />
  在視窗模式中，不論容器背景類型為何，都只會附上一筆資料，將容器視為一個螢幕（螢幕編號0）。

**対応:** SSP 2.8.86
