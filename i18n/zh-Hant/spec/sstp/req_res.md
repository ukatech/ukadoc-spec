# request/response

與 SHIORI 等其他協定一樣，這是仿照 HTTP 設計的自訂協定。<br />
request 必須指定 Charset；若未指定，則會發生錯誤，或以 OS 預設的字元編碼解讀。

- 換行碼為 CR+LF。
- request 以空行結尾（連同前一行的結尾為 (CR+LF)x2）。
- response 的結尾在 EXECUTE 等情況下可能包含附加資料。標頭結束後先空一行，接著是附加資料，最後再以一個空行結束。若沒有附加資料，可能只以標頭後的空行結束。
- 含有附加資料的 response，基於相容性考量，可能完全沒有包含 Charset 在內的標頭，只回傳附加資料。此時可假設字元編碼與 request 相同。
- request 與 response 的 SSTP 版本可能不同。請勿依賴版本號進行解讀。

## request

### request 範例

```
SEND SSTP/1.0
Charset: UTF-8
Sender: SSTPクライアント
Script: \h\s0テストー。\u\s[10]テストやな。
Option: notranslate
```

### request 各方法共通的標頭

各方法專屬的標頭請參閱後面的各方法說明。

- **Charset**: request 的字元編碼。建議出現在第一行。<br />
  除非有特殊理由，建議使用 UTF-8。
- **Sender**: 表示傳送者的字串，例如「SSTP 傳送工具」。COMMUNICATE 方法則為來源 ghost 的 `\0` 名稱。
- **SecurityLevel**: 指定由 SHIORI 或 Sakura Script 處理時的安全性層級。可為 local 或 external。<br />
  僅對 DirectSSTP，或來自 127.0.0.1 等明確為本機來源的 request 有效。<br />
  SSTP over HTTP 一律視為 external，但由 localhost 提供的 html 等內容傳送的 request 除外。
- **SecurityOrigin \[SSP 2.6.59\]**: 表示來源伺服器的 URL 形式字串。格式如下。概念與 [HTTP 標頭的 Origin](https://developer.mozilla.org/ja/docs/Web/HTTP/Headers/Origin) 相同。<br />
  SecurityOrigin: null<br />
  SecurityOrigin: &lt;scheme\>://&lt;hostname\><br />
  SecurityOrigin: &lt;scheme\>://&lt;hostname\>:&lt;port\><br />
  scheme 通常為 http、https、sstp 其中之一。hostname 為來源伺服器名稱或 IP。port 為可接收回覆的連接埠。<br />
  若未特別指定，則視為指定了 null。<br />
  SSTP over HTTP 一律使用 HTTP 的 Origin 標頭內容，並忽略 SSTP 中的 SecurityOrigin。
- **Option**: 指定 SSTP 執行的 Sakura Script 的處理方式。<br />
  可用逗號分隔來指定多個選項。可指定的字串如下。<br />
  nodescript : 停用 balloon 的 SSTP 顯示（遠端 SSTP 無效）<br />
  notranslate : 不執行 OnTranslate 或 MAKOTO 的轉換處理<br />
  nobreak : 不中斷目前執行中的腳本，等待其結束<br />
  strict : 將 Sakura Script 解讀失敗的位置記錄至錯誤日誌。対象包括指定不存在的 surface（`\s`）、動畫（`\i`）、balloon（`\b`）、未知的標籤、`\![コマンド]`、`\&[実体参照]`、缺少必要的 \[\] 或數字，以及 `\p`、`\b`、`\n`、`\c`、`\q` 的無效值。適用於 SEND 的腳本，以及 NOTIFY/GIVE 中 ghost 回傳的腳本 \[SSP 2.8.94\]
- **ID**: 稱為 "Owned SSTP" 的機制。指定由 [SHIORI uniqueid](../../list/shiori-event/notify/uniqueid.md) 傳來的 ID，或 [FMO 識別 ID（僅限 SSP）](../fmo-mutex/index.md)，即可忽略各種安全性檢查與鎖定等，將此 SSTP 以與 ghost 內部處理相同的優先順序處理。<br />
  SecurityLevel 會設為 local，即使處於由 `\t` 等設定的禁止中斷狀態，也能強制中斷並播放。
- **X-SSTP-PassThru-(任意字串)**: 與 ghost 端進行 NOTIFY 等通訊時，直接傳給 SHIORI 的標頭。<br />
  僅執行字元編碼轉換等最低限度的處理，(任意字串) 部分及其內容會原樣轉送。
- **HWnd**: 僅限 DirectSSTP，表示應接收 response 的視窗控制代碼。<br />
  將視窗控制代碼（相當於指標）的資料視為無符號十進位整數後轉換成字串。<br />
  省略時使用 WM_COMMUNICATE 的 wParam。
- **ReceiverGhostHWnd \[SSP 2.5.57\]**: 僅限 (Socket)SSTP，表示應接收 request 的 ghost 的 `\0` 視窗控制代碼。<br />
  指定後會固定處理 request 的 ghost，即使透過 Socket 也能進行與 DirectSSTP 相同的處理。<br />
  若找不到，會立即以 404 Not Found 結束並回報錯誤。
- **ReceiverGhostName \[SSP 2.5.57\]**: 僅限 (Socket)SSTP，表示應接收 request 的 ghost 的 `\0` 名稱。<br />
  指定後會固定處理 request 的 ghost，即使透過 Socket 也能進行與 DirectSSTP 相同的處理。這是 HWnd 的名稱版本。<br />
  若找不到，會立即以 404 Not Found 結束並回報錯誤。
- **ReceiverGhostUUID \[SSP 2.9.35\]**: 僅限 (Socket)SSTP，表示應接收 request 的執行中 ghost 的 [UUID](../../list/propertysystem/property-system/general-property/uuid.md)。<br />
  指定後會固定處理 request 的 ghost，即使透過 Socket 也能進行與 DirectSSTP 相同的處理。這是 HWnd 的 UUID 版本，可避免混淆同名的 ghost。<br />
  若有多個相同 UUID 的 ghost 正在執行，會選擇顯示中的 ghost；若沒有，則選擇執行中 ghost 清單的第一個。<br />
  若執行中的 ghost 沒有 UUID 相符者，會立即以 404 Not Found 結束並回報錯誤（不符合 UUID 格式的值也一樣）。<br />
  若同時指定多個 ReceiverGhostHWnd、ReceiverGhostUUID、ReceiverGhostName，會依此順序評估，並使用第一個找到的 ghost。

## response

### response 範例（無資料）

```
SSTP/1.4 200 OK
Charset: UTF-8
Script: \h\s0テストー。\u\s[10]テストやな。
```

### response 範例（有資料）

```
SSTP/1.4 200 OK
Charset: UTF-8
Script: \h\s0テストー。\u\s[10]テストやな。

追加データはここ
```

### response 各方法共通的標頭

- **Charset**: request 的字元編碼。建議出現在第一行。<br />
  除非有特殊理由，建議使用 UTF-8。<br />
  為了解決相容性問題，可能會刻意省略。此時應假設字元編碼與 request 相同。
- **X-SSTP-PassThru-(任意字串)**: 與 ghost 端進行 NOTIFY 等通訊時，由 SHIORI 直接回傳的標頭。<br />
  僅執行字元編碼轉換等最低限度的處理，(任意字串) 部分及其內容會原樣轉送。

### response 狀態碼

與 HTTP 相同，200 系列表示正常受理，其他則表示錯誤。

- **200 OK**: 正常結束（有回傳值）
- **204 No Content**: 正常結束（無回傳值）
- **210 Break**: 已執行，但在腳本執行期間被中斷<br />
  ※僅限附帶 Entry 的 SEND/1.x 等極少數情況，通常會立即回傳 200 或 204。
- **400 Bad Request**: request 存在無法處理的缺陷
- **404 Not Found ※僅限 SSP**: 指定 ghost 的 SSTP 中，該 ghost 未安裝或未啟動
- **408 Request Timeout**: 逾時：無法與 ghost／SHIORI 端通訊時等情況（平常幾乎不會發生）
- **409 Conflict**: 處於由 `\t` 標籤等設定的禁止中斷狀態，或正在處理其他 request
- **413 Payload Too Large ※僅限 SSP**: SSTP request 過長，拒絕處理
- **420 Refuse**: 因 ghost 端的設定而拒絕接收
- **500 Internal Server Error ※僅限 SSP**: 因處理系統內部偵測到的問題而無法完成處理
- **501 Not Implemented**: 包含未實作的命令等，無法處理
- **503 Service Unavailable**: 因處理系統內部因素而無法受理 SSTP
- **505 Version Not Supported ※僅限 SSP**: SSTP 版本不正確（低於 1.0、3.0 以上等）
- **512 Invisible**: ghost 因最小化等原因未顯示，無法進行任何處理
