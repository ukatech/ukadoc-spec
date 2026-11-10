# `\![execute,schedule-add,オプション,オプション,オプション...]`

**カテゴリ:** 未分类命令

向 ghost 专用日历中添加一条日程。添加的日程会显示在 SSP 日历中，与用户的日程一样会被纳入今日计划和[OnSchedule5MinutesToGo](../../shiori-event/calendar/OnSchedule5MinutesToGo.md)的处理范围。<br />
ghost 专用日历与用户的日程、计划传感器分别保存在不同文件（data/schedule/ghost/schedule.ics）中，并由所有 ghost 共享。其他 ghost 添加的日程也可以覆盖或删除。<br />
用户可以在日历中查看，但无法编辑。可通过日历菜单中的“全部删除”→“ghost 添加的日程”批量删除。<br />
结果通过[OnExecuteScheduleComplete](../../shiori-event/other-communication/OnExecuteScheduleComplete.md)通知，失败时则通过[OnExecuteScheduleFailure](../../shiori-event/other-communication/OnExecuteScheduleFailure.md)通知。无法执行从 SSTP 等外部发送的脚本。

选项（--summary 和 --start 为必需项）<br />
--summary=标题 : 日程标题（SUMMARY）。<br />
--start=日期时间 : 开始日期时间。yyyymmdd 表示全天日程；yyyymmddThhmm 或 yyyymmddThhmmss 表示带时间的日程（本地时间）。分隔符 - 和 : 会被忽略。<br />
--end=日期时间 : 结束日期时间。格式与 --start 相同。省略时，日程仅持续开始日期当天。<br />
--uid=UID : 日程标识符。仅限不含空格的半角字母数字和符号。如果存在相同 UID 的日程，则替换该日程。省略时由 SSP 分配，并通过 OnExecuteScheduleComplete 返回。<br />
--description=说明 : DESCRIPTION。<br />
--location=地点 : LOCATION。<br />
--url=URL : URL。<br />
--categories=分类 : CATEGORIES。有多个分类时以逗号分隔（将作为 iCal 的 CATEGORIES 值原样保存）。<br />
--status=状态 : STATUS（CONFIRMED / TENTATIVE / CANCELLED）。<br />
--type=类型 : 日程类型。将填入[OnSchedule5MinutesToGo](../../shiori-event/calendar/OnSchedule5MinutesToGo.md)等事件的 Reference0。<br />
--rrule=规则 : 重复规则（RRULE 的值部分。示例：FREQ=WEEKLY;BYDAY=MO）。<br />
--exdate=日期 : 从重复日程中排除的日期（yyyymmdd）。有多个日期时以逗号分隔。<br />
--notify=分钟 : 提前多少分钟通知。省略时遵循 SSP 的设置。<br />
--script=脚本 : 附加到日程的 Sakura Script。通知时和读取日程时会执行。<br />
--event=事件ID : 指定以 On 开头的 ID 后，结果的事件名称将使用该 ID（失败时会在 ID 后添加 Failure）。<br />
指定包含逗号的值（例如 --rrule、--exdate、--categories）时，请用 " " 将整个参数括起来。

**対応:** SSP 2.8.91

## 記述例

```sakurascript
\![execute,schedule-add,--uid=myghost-meeting,--summary=打ち合わせ,--start=20261001T1000,--end=20261001T1100,"--rrule=FREQ=WEEKLY;BYDAY=TH",--notify=10,--event=OnMyScheduleAdded]2026年10月1日から毎週木曜10時の予定を登録し、10分前に通知させる。
```

```sakurascript
\![execute,schedule-add,--summary=記念日,--start=20261224,--rrule=FREQ=YEARLY]毎年12月24日の終日予定を登録する。
```
