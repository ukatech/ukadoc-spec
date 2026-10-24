# スケジュールセンサの更新タイミングとイベント

- **手動更新**: カレンダーのメニューからセンサを選んで更新した場合。Begin→Complete（または Failure）が全て発生する。
- **定期チェック**: SSPが30分おきに全センサを自動で巡回する場合。[OnSchedulesenseFailure](OnSchedulesenseFailure.md)のみ発生する。<br />
  全センサぶんのBegin/Completeが定期的に流れるとゴーストが喋りすぎるため、異常時だけ通知される。
