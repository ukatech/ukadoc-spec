# iCal 筛选选项 \[2.8.90\]

此选项用于在[`\![execute,ical-get/ical-post]`](bang-execute-ical-get-URL.md)中指定从获取到的日历返回哪些事件。<br />
\[2.8.92\] rss-get/rss-post 也可以使用同名选项，但省略时的处理方式不同（请参阅[RSS 筛选选项](bang-execute-rss-post-URL.note.md)）。其他请求会忽略此选项。

指定 --from・--to・--expand・--limit 中的任意一项时，将进入“期间模式”，仅返回在期间内发生的日程。只指定 --limit 时，期间模式的起始日为当天。<br />
如果以上选项都未指定，则按文件中的顺序原样返回所有 VEVENT（不按期间筛选，也不限制数量）。

- **期间的确定方式**: 开始日期为 --from 指定的日期，省略时为当天。<br />
  结束日期为 --to 指定的日期（包含该日期）。省略 --to 时，如果指定了 --expand=天数，则期间为指定天数；如果 --expand 未指定天数，则为30天；如果未指定 --expand，则为1830天。<br />
  期间最长为1830天（超过时截断为1830天）。如果 --to 早于 --from，则期间为空，不返回日程。
- **指定了 --expand（按发生次数）**: 将 RRULE 重复规则逐次展开，每次“发生”返回一个 Reference。按日期升序排列。<br />
  同一日程在期间内多次发生时，会按发生次数返回多个 Reference。
- **未指定 --expand（按 VEVENT）**: 期间内至少发生一次的日程，每个 VEVENT 仅返回一个 Reference。按期间内首次发生日期的升序排列（日期相同时按开始时间排列）。<br />
  此时，每个 Reference 的“发生日期”是期间内首次发生的日期。
- **数量上限**: 达到 --limit 指定的数量时停止返回。期间模式下省略该选项时，上限为200；--limit=0 表示不设上限。<br />
  非期间模式下（未指定任何选项时）没有数量上限。
- **发生日期的判定**: 根据 RRULE（FREQ・INTERVAL・COUNT・UNTIL・BYDAY・BYMONTHDAY・BYMONTH）和 EXDATE 进行判定。<br />
  DTSTART 到 DTEND（以 DURATION 指定时则到其表示的结束时间）跨越多天的日程，其跨越的所有日期都视为“发生日期”。<br />
  EXDATE 中列出的日期，无论是否重复发生，均视为未发生。
