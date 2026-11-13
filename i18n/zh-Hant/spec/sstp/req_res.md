# request/response

與SHIORI等其他協定一樣，這是模仿HTTP的自訂協定。<br />
request必須指定Charset，未指定時會發生錯誤，或被解讀為OS預設的字元編碼。

- 換行碼為CR+LF。
- request以空行結尾（連同前一行的結尾為(CR+LF)x2）。
- response的結尾在EXECUTE等情況下可能包含附加資料。標頭結束後隔一個空行，接著是附加資料，最後再以一個空行結束。沒有附加資料時，可能只以標頭後的空行結束。
- 包含附加資料的response基於相容性考量，可能完全沒有包含Charset在內的標頭，只回傳附加資料。此時可假定使用與request相同的字元編碼。
- request與response的SSTP版本可能不同。請勿依賴版本號進行解讀。

## request

### request範例

```
SEND SSTP/1.0
Charset: UTF-8
Sender: SSTPクライアント
Script: \h\s0テストー。\u\s[10]テストやな。
Option: notranslate
```

### 各種request方法共用的標頭

各方法專用的標頭請參閱後面的各方法說明。

- **Charset**: request的字元編碼。建議出現在第一行。<br />
  除非有特殊理由，建議使用UTF-8。
- **Sender**: 表示傳送者的字串，例如「SSTP傳送工具」。COMMUNICATE方法的情況下，為來源ghost的`\0`名稱。
- **SecurityLevel**: 指定以SHIORI或Sakura Script處理時的安全性等級。可指定local或external。<br />
  僅對DirectSSTP，或來自127.0.0.1等明顯為本機的request有效。<br />
  SSTP over HTTP一律視為external，但從localhost提供的html等內容傳送的情況除外。
- **SecurityOrigin \[SSP 2.6.59\]**: 表示來源伺服器的類URL字串，格式如下。概念與[HTTP標頭的Origin](https://developer.mozilla.org/ja/docs/Web/HTTP/Headers/Origin)相同。<br />
  SecurityOrigin: null<br />
  SecurityOrigin: &lt;scheme\>://&lt;hostname\><br />
  SecurityOrigin: &lt;scheme\>://&lt;hostname\>:&lt;port\><br />
  scheme通常為http、https、sstp其中之一。hostname為來源伺服器名稱或IP。port為可接收回覆的連接埠。<br />
  未特別指定時，視為指定了null。<br />
  SSTP over HTTP一律使用HTTP的Origin標頭內容，SSTP中的SecurityOrigin會被忽略。
- **Option**: 指定以SSTP執行的Sakura Script應如何處理。<br />
  可用逗號分隔，指定多個選項。可指定的字串如下。<br />
  nodescript : 停用balloon上的SSTP顯示（遠端SSTP無效）<br />
  notranslate : 不執行OnTranslate或MAKOTO的翻譯處理<br />
  nobreak : 不中斷目前執行中的指令碼，等待其執行完畢<br />
  strict : 將Sakura Script解讀失敗的位置記錄到錯誤日誌。對象包括不存在的surface（`\s`）、動畫（`\i`）、balloon（`\b`）指定，未知的標籤、`\![コマンド]`、`\&[実体参照]`，缺少必要的\[\]或數字，以及`\p`、`\b`、`\n`、`\c`、`\q`的無效值。對SEND的指令碼及NOTIFY/GIVE中ghost回傳的指令碼有效 \[SSP 2.8.94\]
- **ID**: 稱為"Owned SSTP"的功能。指定由[SHIORI uniqueid](../../list/shiori-event/notify/uniqueid.md)傳來的ID，或[FMO的識別ID（僅限SSP）](../fmo-mutex/index.md)時，會忽略各種安全性檢查及鎖定等，以與ghost內部處理相同的優先度處理此SSTP。<br />
  SecurityLevel會設為local，並且即使處於`\t`等禁止中斷的狀態，也能強制中斷並播放。
- **X-SSTP-PassThru-(任意字串)**: 透過NOTIFY等與ghost通訊時，直接傳給SHIORI的標頭。<br />
  僅進行字元編碼轉換等最低限度的處理，(任意字串)的部分及內容會原樣轉送。
- **HWnd**: 僅限DirectSSTP，表示應回覆response的視窗控制代碼。<br />
  將視窗控制代碼（相當於指標）的資料視為無號十進位整數，再轉成字串。<br />
  省略時使用WM_COMMUNICATE的wParam。
- **ReceiverGhostHWnd \[SSP 2.5.57\]**: 僅限(Socket)SSTP，表示應接收request的ghost的`\0`視窗控制代碼。<br />
  指定後會固定處理該request的ghost，即使透過Socket也能進行與DirectSSTP相同的處理。<br />
  找不到時，立即以404 Not Found錯誤結束。
- **ReceiverGhostName \[SSP 2.5.57\]**: 僅限(Socket)SSTP，表示應接收request的ghost的`\0`名稱。<br />
  指定後會固定處理該request的ghost，即使透過Socket也能進行與DirectSSTP相同的處理。這是HWnd的名稱版本。<br />
  \[SSP 2.9.35\] 也可填入UUID而非名稱，此時會指定該UUID的ghost（與專用的ReceiverGhostUUID相同）。<br />
  找不到時，立即以404 Not Found錯誤結束。
- **ReceiverGhostUUID \[SSP 2.9.35\]**: 僅限(Socket)SSTP，表示應接收request的執行中ghost的[UUID](../../list/propertysystem/property-system/general-property/uuid.md)。<br />
  指定後會固定處理該request的ghost，即使透過Socket也能進行與DirectSSTP相同的處理。這是HWnd的UUID版本，可避免混淆同名的ghost。<br />
  若有多個相同UUID的ghost正在執行，會選擇顯示中的ghost；若沒有，則選擇執行中ghost排列的第一個。<br />
  若執行中的ghost沒有符合UUID的項目，立即以404 Not Found錯誤結束（值不符合UUID格式時也一樣）。<br />
  若同時指定ReceiverGhostHWnd、ReceiverGhostUUID、ReceiverGhostName，會依此順序評估，並使用第一個找到的ghost。

## response

### response範例（無資料）

```
SSTP/1.4 200 OK
Charset: UTF-8
Script: \h\s0テストー。\u\s[10]テストやな。
```

### response範例（有資料）

```
SSTP/1.4 200 OK
Charset: UTF-8
Script: \h\s0テストー。\u\s[10]テストやな。

追加データはここ
```

### 各種response方法共用的標頭

- **Charset**: request的字元編碼。建議出現在第一行。<br />
  除非有特殊理由，建議使用UTF-8。<br />
  為解決相容性問題，可能會刻意省略。此時應假定使用與request相同的字元編碼。
- **X-SSTP-PassThru-(任意字串)**: 透過NOTIFY等與ghost通訊時，由SHIORI直接回傳的標頭。<br />
  僅進行字元編碼轉換等最低限度的處理，(任意字串)的部分及內容會原樣轉送。

### response狀態碼

與HTTP相同，200系列表示正常受理，其餘表示錯誤。

- **200 OK**: 正常結束（有回傳值）
- **204 No Content**: 正常結束（無回傳值）
- **210 Break**: 已執行，但在執行指令碼時被中斷<br />
  ※僅限附帶Entry的SEND/1.x等極少數情況，通常會立即回傳200或204。
- **400 Bad Request**: request有無法處理的缺陷
- **404 Not Found ※僅限SSP**: 指定ghost的SSTP中，對應的ghost未安裝或未啟動
- **408 Request Timeout**: 逾時：例如無法與ghost/SHIORI端通訊時（平時幾乎不會發生）
- **409 Conflict**: 處於`\t`標籤等禁止中斷的狀態，或正在處理其他request
- **413 Payload Too Large ※僅限SSP**: SSTP request過長，拒絕處理
- **420 Refuse**: 因ghost端的設定而拒絕接收
- **500 Internal Server Error ※僅限SSP**: 因處理系統內部偵測到某些問題而無法完成處理
- **501 Not Implemented**: 因包含未實作的命令等而無法處理
- **503 Service Unavailable**: 因處理系統內部因素，處於無法受理SSTP的狀態
- **505 Version Not Supported ※僅限SSP**: SSTP版本有誤（低於1.0、3.0以上等）
- **512 Invisible**: ghost因最小化等原因未顯示，處於無法處理任何事項的狀態
