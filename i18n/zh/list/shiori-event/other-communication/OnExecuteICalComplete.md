# OnExecuteICalComplete

**カテゴリ:** 其他通信事件

通过[`\![execute,ical-get/ical-post]`](../../sakura-script/misc/bang-execute-ical-get-URL.md)成功获取并完成解析时触发。

Reference0包含整个日历的信息，Reference1及之后的Reference各包含一条日程。每个Reference内部以字节值1（下文记为\[`\1`\]）分隔。<br />
返回的日程数量及其顺序由[iCal筛选选项](../../sakura-script/misc/bang-execute-ical-post-URL.note.md)决定。

- **Reference0**: 日历名称(X-WR-CALNAME) \[`\1`\] 时区(X-WR-TIMEZONE) \[`\1`\] 历法(CALSCALE。通常为GREGORIAN) \[`\1`\] 本事件返回的日程数 \[`\1`\] 文件中的日程总数 \[`\1`\] 筛选期间的开始日期 \[`\1`\] 筛选期间的结束日期<br />
  期间的开始日期和结束日期采用“年,月,日,,,”格式。如果未指定--from・--to・--expand・--limit，则为空。
- **Reference1～**: UID \[`\1`\] 开始日期时间 \[`\1`\] 结束日期时间 \[`\1`\] 标题(SUMMARY) \[`\1`\] 说明(DESCRIPTION) \[`\1`\] 位置(LOCATION) \[`\1`\] URL \[`\1`\] 状态(STATUS) \[`\1`\] 分类(CATEGORIES) \[`\1`\] 重复规则(RRULE原文) \[`\1`\] 全天标志 \[`\1`\] 发生日期<br />
  按日程数量依次追加Reference1、2、3～。<br />
  开始日期时间、结束日期时间和发生日期采用与RSS相同的逗号分隔格式“年,月,日,时,分,秒”。全天日程的时、分、秒为空，例如“2026,9,10,,,”。<br />
  结束日期时间是该日程的最后一天（DTEND的日期值为排他指定，因此此处的值会减去一天）。如果日程使用DURATION而非DTEND指定时长，则此处为开始日期时间加上时长后的值（全天日程同样会减去一天）。<br />
  如果有多个分类，则以逗号分隔。分类名称本身包含的逗号与分隔用的逗号无法区分。<br />
  全天标志在全天日程时为1，有具体时刻时为0。<br />
  仅在指定了--from・--to・--expand中的任意一个选项时，才会包含发生日期。指定--expand时，包含展开后某一次发生的日期；未指定--expand时，包含期间内最早发生的日期。未指定这些选项时为空。<br />
  RRULE会按原文传递，因此也可以不使用SSP的展开功能，而是自行解析。<br />
  标题、说明、位置、URL、分类和日历名称都经过转义，不会被解释为Sakura Script（\\→\\\\、%→\\%、换行符和制表符→半角空格）。

**対応:** SSP 2.8.90
