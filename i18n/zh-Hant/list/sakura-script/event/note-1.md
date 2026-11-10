# 補充說明

## 更新選項指定

- **checkonly**：不執行一般的更新事件，而是通知 SHIORI 事件[OnUpdateCheckComplete](../../shiori-event/network-update/OnUpdateCheckComplete.md)，若失敗則通知[OnUpdateCheckFailure](../../shiori-event/network-update/OnUpdateCheckFailure.md)，並在確認是否有更新後立即中止處理。<br />
  全部更新完成後，會彙整結果；使用 updateother 時觸發[OnUpdateCheckResultEx](../../shiori-event/network-update/OnUpdateCheckResultEx.md)，其他情況則觸發[OnUpdateCheckResult](../../shiori-event/network-update/OnUpdateCheckResult.md)。
- **testonly**：和正式更新相同，會下載更新檔案，但不會實際取代檔案。<br />
  在 SSP 中，行為與從開發用面板執行的"Update Full Check"相同。
- **recovery \[SSP 2.5.26～\]**：以修復模式執行更新。在 SSP 中，行為與按住在設定-ゴースト(1)-修復模式への切り替えキー有效中設定的按鍵來執行更新相同。<br />
  忽略本機端的所有更新定義檔，只採用從網路下載的更新定義，並與本機端所有檔案的雜湊值比對，下載不同的檔案。
