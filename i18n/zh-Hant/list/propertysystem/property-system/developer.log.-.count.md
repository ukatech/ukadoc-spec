# developer.log.ログ種別.count

**カテゴリ:** 屬性系統

SSP 記錄的日誌目前項目數量。日誌種類可使用以下字串。

- **script**: 腳本日誌（日誌視窗中的種類為 Script）。
- **error**: 錯誤日誌（同 Error）。
- **network**: 網路日誌（同 Network）。
- **update**: 更新日誌（同 Update）。

各日誌可保留的項目數量有上限（預設為 50 件），超過上限時會從最舊的項目開始刪除。<br />
所有 developer.log.～ 屬性皆為唯讀，無論開發者功能的設定為何，都可以取得。<br />
錯誤日誌中，若相同內容的日誌連續出現，有時會合併為一筆 type 為 System 的摘要。

**対応:** SSP
