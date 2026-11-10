# 網路更新事件的發生順序

SSP 一般網路更新（ghost 更新）時的事件發生順序如下。

1. OnUpdateProcessExec　※僅從選單等位置執行時發生。若回傳 script，之後的標準更新處理將不會執行。

2. OnUpdateBegin

3. OnUpdateReady　※僅在有更新檔案時發生。若沒有更新檔案，則略過之後的事件，並發生 OnUpdateComplete（Reference0 為 none）。

4. 每個更新檔案都會重複以下處理。

   1. OnUpdate.OnDownloadBegin
   2. OnUpdate.OnMD5CompareBegin
   3. OnUpdate.OnMD5CompareComplete 或 OnUpdate.OnMD5CompareFailure<br />
      若 MD5 不相符，會針對同一檔案從 OnUpdate.OnDownloadBegin 重新開始。若超過重試次數仍不相符，則發生 OnUpdateFailure（md5 miss），之後的檔案不會再處理。

5. 取得所有檔案後，替換更新檔案並重新載入 SHIORI、shell 等項目，接著發生 OnUpdateComplete。因此，接收 OnUpdateComplete 的是重新載入後的 ghost。

- 若途中失敗（包括中止），會在失敗當下發生 OnUpdateFailure，並結束。同一次更新不會同時發生 OnUpdateFailure 和 OnUpdateComplete。
- OnUpdateReady、各檔案處理完成後，以及替換檔案前，都會等待此前發生的事件所回傳的 script 播放完畢，再進入下一步。因此，若這些事件回傳 script，更新會等到 script 播放完畢後才進入下一階段。
- OnUpdateReady 的 script 播放完畢、準備開始取得檔案時，若按著快轉鍵（SSP 設定「啟用快轉鍵」所指定的按鍵。預設為 Ctrl），該次更新的所有檔案都不會發生 OnUpdate.OnDownloadBegin 和 OnUpdate.OnMD5Compare\*（但仍會取得檔案並進行 MD5 比對）。OnUpdateBegin、OnUpdateReady、OnUpdateComplete、OnUpdateFailure 仍會照常發生。
- 自動更新（更新理由為 auto）時，OnUpdateBegin 會在確認有更新檔案時發生，也就是緊接在 OnUpdateReady 之前。若沒有更新檔案，或在確認更新檔案之前失敗，則 OnUpdateBegin、OnUpdateComplete、OnUpdateFailure 都不會發生。
- 只檢查更新（例如從 ghost explorer 執行檢查）時，不會發生 OnUpdateBegin、OnUpdateReady、OnUpdate.OnDownloadBegin、OnUpdate.OnMD5Compare\*、OnUpdateComplete、OnUpdateFailure，而會改為發生 OnUpdateCheckComplete 或 OnUpdateCheckFailure。
- 更新 ghost 以外的項目（例如 shell、balloon）時，上述事件名稱會替換為 OnUpdateOther〜（OnUpdateOtherBegin、OnUpdateOther.OnDownloadBegin 等）。發生順序相同。

一併更新 ghost 本體、shell、balloon 時，會依 ghost → shell → balloon（→ 建議使用的 balloon）的順序，各自發生上述一連串事件。所有更新完成後，最後只會發生一次 OnUpdateResultEx。只有在 OnUpdateResultEx 未回傳 script 時，才會接著發生 OnUpdateResult。只檢查更新時，則會分別改為 OnUpdateCheckResultEx、OnUpdateCheckResult。
