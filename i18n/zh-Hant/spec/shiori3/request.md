# request

## 範例

```
GET SHIORI/3.0
Charset: UTF-8
Sender: SSP
SenderType: internal,raise
SecurityLevel: local
Status: choosing,balloon(0=0)
ID: OnFirstBoot
BaseID: OnBoot
Reference0: 1
```

※換行碼為CR+LF。<br />
※最後以空行（加上前一行的結尾，為(CR+LF)x2）結束。

- **方法**:

  - **GET**: 預期會在回應的Value標頭中傳回某些內容的方法。
  - **NOTIFY**: 預期不會傳回任何值的方法。回應的Value標頭會被忽略。<br />
    主要用於因某些模式限制而處於「無法說話」的狀態時，或用於啟動後立即傳送狀態通知的事件。<br />
    請注意，同一個ID（事件名稱）可能同時使用GET和NOTIFY。

- **Charset**: 字元編碼。最好放在第一行，或至少放在含有非ASCII範圍字元的行之前。

- **Sender**: 事件的傳送來源。

- **SenderType \[SSP 2.5.05～擴充\]**: 事件傳送來源的屬性。如下所示。若有多個屬性，以逗號連接。<br />
  ID: OnTranslate的情況會沿用被轉譯事件的屬性。

  - **internal**: 從應用程式內部發出的事件。
  - **external**: 從應用程式外部發出的事件。
  - **sakuraapi**: 由Sakura API觸發的事件。
  - **embed**: 由 `\![embed]` 標籤觸發的事件。
  - **raise**: 由 `\![raise]` 標籤觸發的事件。
  - **property**: 因屬性系統的參照命令而觸發的事件。
  - **plugin**: 由plugin觸發的事件。
  - **sstp**: 由SSTP觸發的事件。
  - **communicate**: 由communicate規格觸發的事件。

- **SecurityLevel**: 執行腳本時的安全性等級。以下擇一。<br />
  ID: OnTranslate的情況會沿用被轉譯事件的屬性。<br />
  會盡可能在較前面的行通知。至少會出現在ID標頭之前。

  - **local**: 從執行中的裝置內部發出的通知。
  - **external**: 從執行中的裝置外部發出的通知。

  external表示通知來自執行中機器的外部，因此在安全性方面需要謹慎處理。<br />
  這與SenderType的internal/external是不同的概念；即使事件是從應用程式外部發出的，若可視為安全，仍會判定為local，因此SenderType為external時，SecurityLevel也可能是local。

- **SecurityOrigin \[SSP擴充\]**: 表示傳送來源伺服器的URL風格字串。格式如下。其概念與[HTTP標頭的Origin](https://developer.mozilla.org/ja/docs/Web/HTTP/Headers/Origin)相同。<br />
  SecurityOrigin: null<br />
  SecurityOrigin: &lt;scheme\>://&lt;hostname\><br />
  SecurityOrigin: &lt;scheme\>://&lt;hostname\>:&lt;port\><br />
  scheme通常為http、https或sstp其中之一。hostname為傳送來源伺服器名稱或IP。port為可接收回覆的連接埠。<br />
  例如SSTP未指定標頭，或根本沒有傳送來源的概念等，在沒有資訊時會設為null。<br />
  也請參閱SSTP規格中的SecurityOrigin。

- **Status \[SSP擴充\]**: ghost的執行狀態。如下所示。若有多個狀態，以逗號連接。

  - **talking**: 正在說話
  - **choosing**: 正在顯示選項
  - **minimizing**: 正在最小化
  - **induction**: 正處於 `\![enter,inductionmode]` 狀態
  - **passive**: 正處於 `\![enter,passivemode]` 狀態
  - **timecritical**: 正處於時間關鍵區段（`\t`）中
  - **nouserbreak**: 正處於 `\![enter,nouserbreak]` 狀態
  - **online**: 正在進行網路通訊
  - **opening(種類)**: 輸入方塊等正在開啟。<br />
    若同時開啟多種類型，會以/分隔列出。<br />
    "dialog"代表檔案選擇器、色彩選擇器等。<br />
    例如：opening(communicate/input/teach/dialog)
  - **balloon(ID群組)**: balloon處於顯示狀態。<br />
    以角色ID=balloon ID的格式列出。<br />
    若同時開啟多個，會以/分隔列出。<br />
    例如：balloon(0=2/1=0)表示正在顯示`\0`的大型balloon，以及`\1`的一般balloon。

- **ID**: 事件名稱或文字資源的識別碼。

- **BaseID \[SSP擴充\]**: 可相容的基本事件名稱。<br />
  例如：OnFirstBoot與OnBoot相容，而且OnFirstBoot是OnBoot的變體，因此OnFirstBoot的BaseID會設為OnBoot。

- **Reference\***: 隨事件附帶的其他資訊群組。Reference後方會加上數字。行數不限（只要記憶體允許）。

- **X-SSTP-PassThru-(任意字串) \[SSP 2.5.05～擴充\]**: 僅當事件通知來自SSTP時，SSTP請求標頭中以"X-SSTP-PassThru-"開頭的標頭才會原樣傳送通知。<br />
  其他來源不會附加此標頭。
