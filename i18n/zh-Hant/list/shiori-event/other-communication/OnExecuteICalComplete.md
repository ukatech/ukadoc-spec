# OnExecuteICalComplete

**カテゴリ:** 其他通訊事件

在[`\![execute,ical-get/ical-post]`](../../sakura-script/misc/bang-execute-ical-get-URL.md)成功取得並完成解析時觸發。

Reference0 是整個行事曆的資訊，Reference1 以後則是每筆行程。各 Reference 的內容以位元組值 1（以下稱為\[`\1`\]）分隔。<br />
行程的數量及排列順序由[iCal 篩選選項](../../sakura-script/misc/bang-execute-ical-post-URL.note.md)決定。

- **Reference0**: 行事曆名稱(X-WR-CALNAME) \[`\1`\] 時區(X-WR-TIMEZONE) \[`\1`\] 曆法(CALSCALE。通常是GREGORIAN) \[`\1`\] 此事件回傳的行程數 \[`\1`\] 檔案中的行程總數 \[`\1`\] 篩選期間的開始日期 \[`\1`\] 篩選期間的結束日期<br />
  期間的開始日期與結束日期採用「年,月,日,,,」格式。未指定 --from、--to、--expand、--limit 時為空。
- **Reference1～**: UID \[`\1`\] 開始日期時間 \[`\1`\] 結束日期時間 \[`\1`\] 標題(SUMMARY) \[`\1`\] 說明(DESCRIPTION) \[`\1`\] 地點(LOCATION) \[`\1`\] URL \[`\1`\] 狀態(STATUS) \[`\1`\] 分類(CATEGORIES) \[`\1`\] 重複規則(RRULE 原文) \[`\1`\] 全天旗標 \[`\1`\] 發生日<br />
  依行程數量，Reference1、2、3～會依序排列。<br />
  開始日期時間、結束日期時間與發生日採用和 RSS 相同的逗號分隔「年,月,日,時,分,秒」格式。全天行程的時、分、秒為空，例如「2026,9,10,,,」。<br />
  結束日期時間是該行程的最後一天（DTEND 的日期值為排他指定，因此會填入往前一天的日期）。若行程以 DURATION 而非 DTEND 指定長度，則會填入開始日期時間加上該長度的值（全天行程也同樣往前一天）。<br />
  分類有多個時會以逗號分隔。分類名稱本身包含的逗號與分隔用逗號不會區分。<br />
  全天行程的全天旗標為 1，附有時間的行程則為 0。<br />
  只有指定 --from、--to、--expand 其中之一時才會填入發生日。指定 --expand 時，填入展開後其中一次的發生日；未指定 --expand 時，填入期間內首次發生的日期。未指定時為空。<br />
  RRULE 會以原文傳遞，因此也可以不使用 SSP 的展開功能，自行解讀。<br />
  標題、說明、地點、URL、分類與行事曆名稱會經過跳脫，以避免被解讀為 Sakura Script（\\→\\\\、%→\\%、換行與定位字元→半形空格）。

**対応:** SSP 2.8.90
