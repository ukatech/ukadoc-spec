# 日程传感器的更新时间与事件

- **手动更新**: 在日历菜单中选择传感器并更新时。Begin→Complete（或Failure）都会触发。
- **定期检查**: SSP每隔30分钟自动轮询所有传感器时。仅触发[OnSchedulesenseFailure](OnSchedulesenseFailure.md)。<br />
  定期触发所有传感器的Begin/Complete会导致ghost说话过多，因此仅在发生异常时通知。
