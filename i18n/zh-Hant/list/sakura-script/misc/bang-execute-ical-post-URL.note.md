# iCal 篩選選項 \[2.8.90\]

在[`\![execute,ical-get/ical-post]`](bang-execute-ical-get-URL.md)中，指定從取得的行事曆回傳哪些事件的選項。<br />
\[2.8.92\] rss-get/rss-post 也可使用同名選項，但省略時的處理方式不同（請參閱[RSS 篩選選項](bang-execute-rss-post-URL.note.md)）。其他請求會忽略此選項。

指定 --from・--to・--expand・--limit 任一選項時，會進入「期間模式」，只回傳期間內發生的行程。若只指定 --limit，期間模式會從當日開始。<br />
若以上皆未指定，則會依序原樣回傳檔案中的所有 VEVENT（不依期間篩選，也不限制件數）。

- **期間的決定方式**: 開始日期為 --from 指定的日期，若省略則為當日。<br />
  結束日期為 --to 指定的日期（包含該日）。省略 --to 時，若有 --expand=日數，則期間為指定日數；若 --expand 未指定日數，則為30日；若未指定 --expand，則為1830日。<br />
  期間長度最多為1830日（超過時會截斷為1830日）。若 --to 早於 --from，期間會是空的，不會回傳行程。
- **有 --expand（以發生次數為單位）**: 將 RRULE 的重複行程逐次展開，每次「發生」回傳一筆 Reference。依日期升冪排列。<br />
  同一行程在期間內發生多次時，會依發生次數排列多筆 Reference。
- **沒有 --expand（以 VEVENT 為單位）**: 期間內至少發生一次的行程，每個 VEVENT 僅回傳一筆。依期間內首次發生日期升冪排列（同一天則依開始時間排列）。<br />
  此時，各 Reference 的「發生日」會是期間內首次發生的日期。
- **件數上限**: 達到 --limit 指定的件數時即停止。期間模式未指定時，上限為200件；--limit=0 表示不限件數。<br />
  非期間模式（未指定任何選項）不設上限。
- **發生日的判定**: 解析 RRULE（FREQ・INTERVAL・COUNT・UNTIL・BYDAY・BYMONTHDAY・BYMONTH）與 EXDATE 後進行判定。<br />
  從 DTSTART 到 DTEND（以 DURATION 表示長度時則為該行程的結束時間）跨越多日的行程，所有這些日期都視為「發生日」。<br />
  EXDATE 列出的日期，無論是否有重複設定，都視為不會發生。
