# OnSchedulesenseComplete

**カテゴリ:** 日历事件

日程传感器处理完成时触发。<br />
此通知会发送给所有正在运行的ghost，而不是特定的ghost。

**仅在手动更新时触发。**定期检查时不会触发，详见[后文](caption_schedulesensetiming.md)。<br />
即使成功获取数据但没有更新（304 Not Modified或内容相同），也会视为成功并触发此事件。

- **Reference0**: 日程传感器名称
- **Reference1**: 日程传感器返回的日程数据数量

**対応:** SSP
