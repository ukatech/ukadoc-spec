# OnNotifyHolidayInfo

**カテゴリ:** Notify 事件

通知今天的节日名称。启动时，在 [OnNotifyUserInfo](OnNotifyUserInfo.md) 之后发送。*\[NOTIFY\]*<br />
只有在 SSP 的语言文件夹中的节日表（holidays.txt；如果有地区设置对应的国家节日表，则为 holidays-XX.txt）中能获取到今天的节日名称时才会发送；非节日当天或节日表中没有名称时不会发送。<br />
“今天”会受到 SSP 的“当前时间模拟调整”（时间机器）影响。

- **Reference0**: 节日名称。（例如元旦、Christmas Day。补休可能显示为“补休日”或“Christmas Day (substitute day)”）
- **Reference1**: 日期。（以逗号分隔，例如 2026,01,01）
- **Reference2**: 已加载节日表的国家代码（ISO 3166。对于 holidays-GB.txt，为 GB）。如果使用未指定国家的默认表（holidays.txt），则为空。

**対応:** SSP 2.9.11
