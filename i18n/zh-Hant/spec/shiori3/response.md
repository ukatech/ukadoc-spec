# response

## 範例

```
SHIORI/3.0 200 OK
Charset: UTF-8
Sender: AYA
Value: \1\s[10]\0\s[0]\e
```

※換行碼為CR+LF。<br />
※最後以空行（加上前一行的結尾，為(CR+LF)x2）結束。

- **狀態碼**: 與HTTP相同，200系列表示成功，其他則表示某種失敗（錯誤）。<br />
  目前主要使用的狀態碼如下。

  - **200**: 200 OK<br />
    成功，有回傳值（Value）。
  - **204**: 204 No Content<br />
    成功，沒有回傳值。
  - **311**: 311 Not Enough<br />
    在ID: OnTeach（SHIORI/2系列的TEACH方法）中，表示需要更多資訊。<br />
    再次開啟輸入方塊詢問使用者，輸入完成後新增包含輸入字串的Reference。
  - **312**: 312 Advice<br />
    在ID: OnTeach（SHIORI/2系列的TEACH方法）中，表示最近輸入的字串無法解讀，應予以捨棄。<br />
    捨棄最後一個Reference，再次開啟輸入方塊詢問使用者，輸入完成後新增包含輸入字串的Reference。
  - **400**: 400 Bad Request<br />
    無法解讀請求字串。
  - **500**: 500 Internal Server Error<br />
    SHIORI內部發生某種錯誤，無法傳回回應。

- **Charset**: 字元編碼。最好放在第一行，或至少放在含有非ASCII範圍字元的行之前。

- **Sender**: 傳送者。通常是SHIORI的名稱。

- **Value**: 要說出的腳本。

- **ValueNotify \[SSP擴充 2.5.35\]**: *\[實驗性功能\]*<br />
  即使請求方法為NOTIFY，也能執行Sakura Script的擴充功能。<br />
  若以此標頭傳回Sakura Script，會立即執行。若為GET，則會在執行Value標頭中的腳本之前執行。<br />
  可執行的標籤非常有限，其他標籤及所有其他字串都會被忽略。<br />
  <del>若方法不是NOTIFY，或Value標頭已存在，則會被忽略。</del> 2.6.76已取消限制<br />
  目前可執行的標籤如下：

  - `\![sound]`
  - `\![set,trayicon]`
  - `\![set,trayballoon]`
  - `\![raise]`
  - `\![raiseother]`
  - `\![raiseplugin]`
  - `\![timerraiseother]`
  - `\![timerraiseplugin]`
  - `\![notify]`
  - `\![notifyother]`
  - `\![notifyplugin]`
  - `\![get,property]` ＋2.6.82
  - `\![set,property]` ＋2.6.82

- **SecurityLevel \[SSP擴充\]**: 以下擇一。

  - **local**: 相當於來自執行中裝置內部的腳本之安全性等級。
  - **external**: 相當於來自執行中裝置外部的腳本之安全性等級。

  要說出的腳本之SecurityLevel。若為external，部分腳本會因安全性功能而無法執行。

- **Marker \[SSP擴充\]**: 要顯示於balloon標記（balloon下方的附加資訊）的字串。

- **ErrorLevel \[SSP擴充\]**: SHIORI內部發生錯誤的等級。以下擇一。若要表示多個錯誤，以位元組值1分隔。

  - **info**: 資訊。不是錯誤。
  - **notice**: 通知。雖然難以稱為錯誤，但有需要修正的描述等。
  - **warning**: 警告。有描述錯誤等問題，處理尚未停止，但最好加以處理。
  - **error**: 一般錯誤。因描述錯誤等問題，部分處理已停止且無法恢復。
  - **critical**: 嚴重錯誤。比error更嚴重，最好立即採取某種處理。

  若有此標頭，會通知使用者發生了某種錯誤。<br />
  通知的等級可由使用者變更設定。一般為error以上。<br />
  在SSP中，錯誤會記錄在錯誤記錄中，通知區域也會顯示錯誤圖示。

- **ErrorDescription \[SSP擴充\]**: SHIORI內部發生錯誤的詳細資訊。只有在有ErrorLevel時才有效。<br />
  若要表示多個錯誤，以位元組值1分隔。<br />
  ErrorLevel和ErrorDescription的元素數量必須相同。

- **BalloonOffset \[SSP擴充\]**: balloon的偏移值（X,Y）。

- **Reference0**: 若要傳送communicate，填入ghost的`\0`側名稱。

- **Reference1～**: communicate的其他資訊。<br />
  回應的Reference1＝SSTP Communicate的Reference0＝接收方OnCommunicate的Reference2<br />
  請注意，因相容性問題，項目會如上所示錯開。

- **Age \[SSP擴充\]**: communicate的世代數。第一次為零。每往返一次就+1。<br />
  雖然是SSP擴充，實際上是SHIORI/2.x相容處理。

- **MarkerSend \[SSP擴充\]**: communicate期間要顯示在「對方側」的balloon標記字串。<br />
  會作為SSTP的Marker標頭傳送。

- **X-SSTP-PassThru-(任意字串) \[SSP 2.5.03～擴充\]**: 僅限來自SSTP的事件通知所產生的回應，此標頭會原樣附加至SSTP回應。<br />
  其他來源會忽略此標頭。<br />
  可指定多個標頭，但若要傳回多個標頭，請使用不同的標頭名稱。<br />
  （舊標頭名稱：X-SSTP-Return- 預定廢止）
