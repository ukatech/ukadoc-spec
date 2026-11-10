# http/rss/ical/websocket 選項

- **--accept=Accept 請求標頭的內容 \[2.7.34\]**: 指定用來設定可接收 Content-Type 格式的 Accept 標頭。
- **--accept-language=Accept-Language 請求標頭的內容 \[2.7.34\]**: 指定用來控制國際化相關行為的 Accept-Language 標頭。
- **--async=識別碼**: 不等待處理完成，繼續執行 SakuraScript，並在處理完成後通知事件。<br />
  HTTP 時會觸發[OnExecuteHTTPComplete](../../shiori-event/other-communication/OnExecuteHTTPComplete.md)或[OnExecuteHTTPFailure](../../shiori-event/other-communication/OnExecuteHTTPFailure.md)。<br />
  RSS 時會觸發[OnExecuteRSSComplete](../../shiori-event/other-communication/OnExecuteRSSComplete.md)或[OnExecuteRSSFailure](../../shiori-event/other-communication/OnExecuteRSSFailure.md)。<br />
  iCal 時會觸發[OnExecuteICalComplete](../../shiori-event/other-communication/OnExecuteICalComplete.md)或[OnExecuteICalFailure](../../shiori-event/other-communication/OnExecuteICalFailure.md)。 \[2.8.90\]<br />
  WebSocket 時會在連線、接收、斷線的各個時機觸發[OnExecuteWebSocketOpen](../../shiori-event/other-communication/OnExecuteWebSocketOpen.md)/[Receive](../../shiori-event/other-communication/OnExecuteWebSocketReceive.md)/[Reconnect](../../shiori-event/other-communication/OnExecuteWebSocketReconnect.md)/[Close](../../shiori-event/other-communication/OnExecuteWebSocketClose.md)/[Failure](../../shiori-event/other-communication/OnExecuteWebSocketFailure.md)（一律為非同步執行，因此不適用 --sync）。<br />
  指定不以 On 開頭的識別碼時，會觸發名稱與上述事件相同的事件。<br />
  指定以 On 開頭的識別碼時，HTTP/RSS/iCal 會觸發\[指定的識別碼\]（成功）/\[指定的識別碼\]Failure（失敗）。WebSocket 會觸發\[指定的識別碼\]Open/\[指定的識別碼\]（接收）/\[指定的識別碼\]Reconnect/\[指定的識別碼\]Close/\[指定的識別碼\]Failure。<br />
  範例：--async=OnExample 時，HTTP/RSS/iCal→OnExample/OnExampleFailure，WebSocket→OnExampleOpen/OnExample/OnExampleReconnect/OnExampleClose/OnExampleFailure<br />
  不過，SSLInfo 類事件([OnExecuteHTTPSSLInfo](../../shiori-event/other-communication/OnExecuteHTTPSSLInfo.md)/[OnExecuteRSS_SSLInfo](../../shiori-event/other-communication/OnExecuteRSS_SSLInfo.md)/[OnExecuteICal_SSLInfo](../../shiori-event/other-communication/OnExecuteICal_SSLInfo.md)/[OnExecuteWebSocket_SSLInfo](../../shiori-event/other-communication/OnExecuteWebSocket_SSLInfo.md))不在此限，即使指定以 On 開頭的識別碼，也一律會以上述事件名稱通知。<br />
  若要暫停 SakuraScript 的處理，請改用 --sync（不適用於 WebSocket）。
- **--authorization=Authorization 請求標頭的內容 \[2.6.37\]**: OAuth 等情況需要 Authorization 標頭時，請事先設定。
- **--cookie=Cookie 資料**: 指定 Cookie 資料；視需要可直接使用 OnExecuteHTTPComplete 的 Reference5 值。
- **--content-type=(multipart/form-data | application/x-www-form-urlencoded | 其他任意指定)**: 僅適用於 http-post。指定如何傳送以 param 指定的參數。<br />
  未指定時，使用 application/x-www-form-urlencoded。<br />
  請注意，某些指定格式會限制 param 的寫法。<br />
  從 \[2.6.37\] 起，這項資訊會直接反映在 Content-Type 請求標頭中。
- **--expand 或 --expand=天數 \[2.8.90\]**: 僅適用於 ical-get/ical-post。請參閱[※iCal 篩選選項](bang-execute-ical-post-URL.note.md)。<br />
  展開 RRULE 重複規則，並逐一回傳每次「發生」的項目。指定天數時，會作為省略 --to 時的期間長度（預設為 30 天）。
- **--file=檔案名稱**: 指定取得資料的儲存名稱。資料會儲存至\[執行中的 ghost 資料夾\]/ghost/master/var/檔案名稱。
- **--from=yyyymmdd \[2.8.90\]**: 僅適用於 ical-get/ical-post、rss-get/rss-post \[2.8.92\]。請參閱[※iCal 篩選選項](bang-execute-ical-post-URL.note.md)和[※RSS 篩選選項](bang-execute-rss-post-URL.note.md)。<br />
  回傳事件期間的開始日期。省略時為當日。<br />
  \[2.8.92\] 在 rss-get/rss-post 中，這是回傳項目的更新時間下限（從當日 0 時起算）。省略時不設下限。
- **--header=SomeHeader: 請求標頭的內容 \[2.6.40\]**: 設定任意名稱的請求標頭。名稱與內容之間必須以冒號分隔。<br />
  這會覆寫 SSP 設定的標頭資訊，使用時請注意避免與其設定衝突。
- **--insecure \[2.7.34\]**: 略過 TLS 憑證驗證。
- **--limit=筆數 \[2.8.90\]**: 僅適用於 ical-get/ical-post、rss-get/rss-post \[2.8.92\]。請參閱[※iCal 篩選選項](bang-execute-ical-post-URL.note.md)和[※RSS 篩選選項](bang-execute-rss-post-URL.note.md)。<br />
  指定回傳事件的最大筆數。省略時為 200 筆，指定 0 則不限制。<br />
  只寫 --limit 時，會進入期間模式，開始日期為當日。若 --from、--to、--expand、--limit 都未指定，則不限制筆數（回傳所有項目）。<br />
  \[2.8.92\] 在 rss-get/rss-post 中，只有指定此選項時才會依新到舊的順序截取指定筆數。省略或指定 0 時不限制；只寫 --limit 也不會篩選期間。
- **--log=檔案名稱**: 將與伺服器的所有通訊內容記錄至日誌，主要用於開發時除錯。
- **--nodescript**: 不顯示線上顯示與下載狀態。
- **--nofile=參數（字元編碼） \[2.5.77\]**: 不建立暫存檔，而是將取得的資料展開至記憶體中，並存入事件的 Reference3。<br />
  參數指定應用來解讀取得資料的字元編碼。未指定時視為 UTF-8。<br />
  Reference 無法包含換行，因此換行字元會轉換為位元組值 1。<br />
  可取得的資料大小上限為 128KB。<br />
  \[2.8.90\] 在 rss-get/rss-post、ical-get/ical-post 中，由於解析時需要檔案，因此會忽略此設定。
- **--no-cache \[2.7.34\]**: 設定 Cache-Control: no-cache，以抑制快取的使用。
- **--param=參數**: 指定 get/post/put 的參數。可重複指定。<br />
  multipart/form-data 時：<br />
  　以 --param=欄位名稱=資料 的格式重複指定所需次數。<br />
  　範例： --param=message_body=資料<br />
  application/x-www-form-urlencoded 時：<br />
  　以 --param=欄位名稱=資料 的格式重複指定時，所有參數會以 & 串接後傳送至伺服器。<br />
  　其他情況則會以換行字元 (CRLF) 串接後傳送至伺服器（舊版相容處理）。<br />
  指定其他 content-type 時：<br />
  　若定義多個參數，會以換行字元 (CRLF) 串接後傳送至伺服器。
- **--param-charset=字元編碼**: 指定字元編碼，例如 Shift_JIS、EUC-JP、UTF-8；預設為 UTF-8。
- **--param-input-file=檔案名稱 \[2.6.40\]**: 若要傳送大到無法透過 --param 選項指定的資料，請指定存有傳送資料的檔案。<br />
  若指定的不是絕對路徑，會視為相對於\[執行中的 ghost 資料夾\]/ghost/master/的路徑。<br />
  請勿同時指定 --param。<br />
  基本上不會檢查檔案內容，因此字元編碼、編碼方式等須由使用者自行負責處理。<br />
  不過，僅在 multipart/form-data 時，會讀取第一行並將其解讀為欄位間的分隔符號。<br />
  指定的檔案路徑必須位於 SSP 管轄範圍內（SSP.exe 所在位置之下，或指定用來列舉 ghost 等項目的資料夾之下）。
- **--progress-notify \[2.6.44\]**: 下載處理期間會通知[OnExecuteHTTPProgress](../../shiori-event/other-communication/OnExecuteHTTPProgress.md)事件（ical-get/ical-post 時為[OnExecuteICalProgress](../../shiori-event/other-communication/OnExecuteICalProgress.md) \[2.8.90\]）；若事件 ID 以 On 開頭，則會在 ID 後加上 Progress 來通知事件。<br />
  指定以 On 開頭的識別碼時，會改為觸發 SHIORI Event \[指定的識別碼\]Progress。<br />
  範例：--async=OnExample 時為 OnExampleProgress<br />
  下載處理期間會逐一執行事件通知，因此下載速度會降低。<br />
  另外，若要輸出至檔案，事件通知時會先關閉檔案，收到回應後再重新開啟，因此下載速度會進一步降低，請留意。
- **--streaming 或 --streaming=類型 \[2.8.14\]**: 指定 HTTP 請求的串流處理方式。--streaming=sse 表示 Server-Sent Events，--streaming=text 表示以換行分隔的串流（例如 NDJSON）<br />
  只指定 --streaming 而未指定類型時，會根據伺服器回應的 Content-Type 執行適當的串流處理。<br />
  接收到的資料會透過[OnExecuteHTTPStreaming](../../shiori-event/other-communication/OnExecuteHTTPStreaming.md)事件通知；若事件 ID 以 On 開頭，則會在 ID 後加上 Streaming，例如 OnHogehogeStreaming。
- **--sync=識別碼 \[2.6.44\]**: 除了暫停 SakuraScript 的執行並等待處理完成外，行為與指定 --async 相同。
- **--timeout=秒數**: 指定等待回應的時間（※不是下載所需時間），上限為 300 秒。<br />
  若在指定秒數內未收到回應，會通知 SHIORI 事件「OnExecuteHTTPFailure」，並在 Reference4 中放入「timeout」。
- **--to=yyyymmdd \[2.8.90\]**: 僅適用於 ical-get/ical-post、rss-get/rss-post \[2.8.92\]。請參閱[※iCal 篩選選項](bang-execute-ical-post-URL.note.md)和[※RSS 篩選選項](bang-execute-rss-post-URL.note.md)。<br />
  回傳事件期間的結束日期（包含當日）。<br />
  \[2.8.92\] 在 rss-get/rss-post 中，這是回傳項目的更新時間上限（截至當日結束）。省略時不設上限。
- **--m_websocketProtocol=Sec-Websocket-Protocol \[2.8.08\]**: 指定 WebSocket 連線時使用的 Sec-Websocket-Protocol 標頭。若未指定，則不會傳送此標頭。
