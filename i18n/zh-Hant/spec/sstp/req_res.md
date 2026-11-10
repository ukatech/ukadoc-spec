# request/response

與SHIORI等其他協定相同，這是模仿HTTP的自訂協定。<br />
請求必須指定Charset；若未指定，會發生錯誤，或會以OS預設字元編碼解讀。

- 換行字元為CR+LF。
- 請求以空行結尾（加上前一行的結尾，為(CR+LF)x2）。
- response結尾可能會在EXECUTE等情況下包含額外資料。標頭結束後會隔一個空行，接著放入額外資料，再以一個空行結束。沒有額外資料時，也可能只以標頭後的空行結束。
- 含有額外資料的response，基於相容性考量，有時會完全不包含Charset等標頭，只傳回額外資料。此時可假設其字元編碼與request相同。
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

### request各方法共用的標頭

方法專屬的標頭請參閱後面的各方法說明。

- **Charset**: request的字元編碼。最好出現在第一行。<br />
  除非有特別理由，建議使用UTF-8。
- **Sender**: 表示傳送者的字串，例如「SSTP傳送工具」。使用COMMUNICATE方法時，為來源ghost的`\0`名稱。
- **SecurityLevel**: 指定使用SHIORI或SakuraScript處理時的安全性層級。可指定local或external。<br />
  僅DirectSSTP，或明確來自本機的request（例如127.0.0.1）有效。<br />
  SSTP over HTTP一律視為external，但若request是由localhost提供的html等傳送則除外。
- **SecurityOrigin \[SSP 2.6.59\]**: 表示來源伺服器的類URL字串。格式如下。概念與[HTTP標頭的Origin](https://developer.mozilla.org/ja/docs/Web/HTTP/Headers/Origin)相同。<br />
  SecurityOrigin: null<br />
  SecurityOrigin: &lt;scheme\>://&lt;hostname\><br />
  SecurityOrigin: &lt;scheme\>://&lt;hostname\>:&lt;port\><br />
  scheme 通常為http、https或sstp。hostname為來源伺服器名稱或IP。port為可接收回覆的連接埠。<br />
  未特別指定時，視為指定了null。<br />
  SSTP over HTTP一律會設定HTTP的Origin標頭內容，並忽略SSTP中的SecurityOrigin。
- **Option**: 指定SSTP執行的SakuraScript如何處理。<br />
  可用逗號分隔指定多個選項。可指定的字串如下。<br />
  nodescript : 停用在balloon中顯示SSTP（停用來自遠端的SSTP）<br />
  notranslate : 不執行OnTranslate或MAKOTO的轉換處理<br />
  nobreak : 不中斷目前正在執行的script，等待其結束<br />
  strict : 將SakuraScript解讀失敗的位置記錄到錯誤記錄。適用項目包括不存在的surface (`\s`)、動畫 (`\i`)、balloon (`\b`) 指定、未知的標籤、`\![命令]`、`\&[字元參照]`、缺少必要的\[\]或數字，以及`\p`・`\b`・`\n`・`\c`・`\q`的無效值。適用於SEND的script，以及NOTIFY/GIVE中ghost傳回的script \[SSP 2.8.94\]
- **ID**: 稱為「Owned SSTP」的項目。指定透過[SHIORI uniqueid](../../list/shiori-event/notify/uniqueid.md)傳送的ID，或[FMO識別ID（僅SSP）](../fmo-mutex/index.md)，即可忽略各種安全檢查與鎖定等，並以與ghost內部處理相同的優先度處理此SSTP。<br />
  SecurityLevel會設為local，即使處於禁止中斷的狀態（例如`\t`），也能強制中斷播放。
- **X-SSTP-PassThru-(任意字串)**: 與ghost端通訊（例如NOTIFY）時，直接傳遞給SHIORI的標頭。<br />
  只會進行字元編碼轉換等最低限度的處理，(任意字串)的部分與內容都會原樣轉送。
- **HWnd**: 僅適用於DirectSSTP，表示應回覆response的視窗控制代碼。<br />
  將視窗控制代碼（相當於指標）的資料視為無號十進位整數，並轉換為字串。<br />
  省略時使用WM_COMMUNICATE的wParam。
- **ReceiverGhostHWnd \[SSP 2.5.57\]**: 僅適用於(Socket)SSTP，表示應傳送request的ghost之`\0`視窗控制代碼。<br />
  指定此項目後，應處理的ghost會固定，即使透過Socket，也能進行與DirectSSTP相同的處理。<br />
  找不到時會立即以404 Not Found錯誤結束。
- **ReceiverGhostName \[SSP 2.5.57\]**: 僅適用於(Socket)SSTP，表示應傳送request的ghost之`\0`名稱。<br />
  指定此項目後，應處理的ghost會固定，即使透過Socket，也能進行與DirectSSTP相同的處理。這是HWnd的名稱版本。<br />
  找不到時會立即以404 Not Found錯誤結束。

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

### response各方法共用的標頭

- **Charset**: request的字元編碼。最好出現在第一行。<br />
  除非有特別理由，建議使用UTF-8。<br />
  為了解決相容性問題，有時會刻意省略。此時請假設字元編碼與request相同。
- **X-SSTP-PassThru-(任意字串)**: 與ghost端通訊（例如NOTIFY）時，直接從SHIORI傳回的標頭。<br />
  只會進行字元編碼轉換等最低限度的處理，(任意字串)的部分與內容都會原樣轉送。

### response的狀態碼

與HTTP相同，200系列表示正常受理，其餘為錯誤。

- **200 OK**: 正常結束（有傳回值）
- **204 No Content**: 正常結束（無傳回值）
- **210 Break**: 已執行，但在script執行期間中斷<br />
  ※僅限帶有Entry的SEND/1.x等極少數情況，一般會立即傳回200或204。
- **400 Bad Request**: request有某種無法處理的缺失
- **404 Not Found ※僅SSP**: 指定ghost的SSTP中，對應的ghost尚未安裝或啟動
- **408 Request Timeout**: 逾時：無法與ghost/SHIORI端通訊等情況（平常幾乎不會發生）
- **409 Conflict**: 處於禁止中斷的狀態（例如`\t`標籤），或正在處理其他request
- **413 Payload Too Large ※僅SSP**: SSTP request過長，拒絕處理
- **420 Refuse**: 因ghost端的設定而拒絕接收
- **500 Internal Server Error ※僅SSP**: 因處理系統內部偵測到某種問題而無法完成處理
- **501 Not Implemented**: 含有尚未實作的命令等，無法處理
- **503 Service Unavailable**: 因處理系統內部狀況而無法接收SSTP
- **505 Version Not Supported ※僅SSP**: SSTP版本無效（例如低於1.0或高於3.0）
- **512 Invisible**: ghost因最小化等原因未顯示，無法進行任何處理
