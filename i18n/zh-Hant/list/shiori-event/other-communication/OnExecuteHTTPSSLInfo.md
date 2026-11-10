# OnExecuteHTTPSSLInfo

**カテゴリ:** 其他通信事件

即使取得失敗（HTTP 回應不是 200），只要 SSL/TLS 層級的連線成功，就會發出通知。

即使透過 --async・--sync 指定以 On 開頭的 ID，事件名稱也不會替換，一律以本事件通知。請透過 Reference0 判斷所屬的請求。

- **Reference0**: async ID（若未指定則為空）
- **Reference1**: 取得 URL
- **Reference2**: http 回應代碼（即使發生錯誤也會通知）
- **Reference3**: 通訊版本。目前大多是 "TLSv1/SSLv3"（SSP 內部會拒絕 SSLv2，因此實際上只會收到這個值）
- **Reference4**: 加密方式<br />
  例如：AES256-SHA
- **Reference5**: 簽發對象。若要確認名稱，建議擷取 /O= 後面的字串<br />
  給程式設計者：內容是經過 OpenSSL 的 X509_NAME_oneline 處理後的結果<br />
  例如：/1.3.6.1.4.1.311.60.2.1.3=US/1.3.6.1.4.1.311.60.2.1.2=Delaware/businessCategory=Private Organization/serialNumber=4337446/C=US/postalCode=94107/ST=California/L=San Francisco/street=795 Folsom St, Suite 600/O=Twitter, Inc./OU=Twitter Operations/CN=twitter.com
- **Reference6**: 有效期限起始日期時間，格式為年、月、日、時、分、秒<br />
  例如：2011,7,7,9,0,0
- **Reference7**: 有效期限結束日期時間，格式為年、月、日、時、分、秒<br />
  例如：2012,7,28,8,59,59
- **Reference8**: 簽發者。若要確認名稱，建議擷取 /O= 後面的字串<br />
  給程式設計者：內容是經過 OpenSSL 的 X509_NAME_oneline 處理後的結果<br />
  例如：/C=US/O=VeriSign, Inc./OU=VeriSign Trust Network/OU=Terms of use at https://www.verisign.com/rpa (c)06/CN=VeriSign Class 3 Extended Validation SSL CA
- **Reference9 (2.4.51～)**: 憑證鏈中的 CommonName(CN)，以逗號分隔並依序列出

**対応:** SSP
