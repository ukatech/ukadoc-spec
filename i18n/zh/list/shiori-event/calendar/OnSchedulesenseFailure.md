# OnSchedulesenseFailure

**カテゴリ:** 日历事件

日程传感器处理失败时触发。<br />
此通知会发送给所有正在运行的ghost，而不是特定的ghost。

与Begin/Complete不同，[定期检查时也会触发](caption_schedulesensetiming.md)。

- **Reference0**: [失败原因](../headline-rss/caption_headlinesenseresult.md)（与headline sensor使用的原因相同）。无法获取时为can't download；成功获取但无法解析为iCal时为can't analyze。
- **Reference1**: 日程传感器名称。定期检查时不会触发Begin，因此没有此项就无法知道哪个传感器发生了故障

**対応:** SSP
