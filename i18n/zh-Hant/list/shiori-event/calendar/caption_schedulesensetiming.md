# 行程感測器的更新時機與事件

- **手動更新**: 從行事曆的選單選取感測器並更新時。Begin→Complete（或 Failure）都會觸發。
- **定期檢查**: SSP 每 30 分鐘自動巡訪所有感測器時。只會觸發 [OnSchedulesenseFailure](OnSchedulesenseFailure.md)。<br />
  若定期傳送所有感測器的 Begin/Complete 事件，ghost 會說個不停，因此只有發生異常時才會通知。
