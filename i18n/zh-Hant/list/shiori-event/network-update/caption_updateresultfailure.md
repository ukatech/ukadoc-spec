# 網路失敗理由

- **timeout**: 發生逾時。
- **too slow**: *在 SSP 中會成為 timeout，因此不會出現*。連線非常緩慢。
- **md5 miss**: MD5 不相符。
- **artificial**: 使用者操作中止更新。
- **404 等**: 以該狀態碼表示的失敗。
- **fileio**: ※僅 SSP。因容量不足，無法寫入更新目標。
- **readonly**: ※僅 SSP。因唯讀旗標，無法寫入更新目標。檔案或資料夾設有唯讀旗標時會發生。
- **virusdetect**: ※僅 SSP。可能在資料中偵測到病毒。 \[2.5.15\]
- **toomanyredirect**: ※僅 SSP。因重新導向次數過多而中止處理。 \[2.5.15\]
- **executing**: ※僅 SSP。因更新已在執行中，阻止重複啟動。 \[2.5.26\]
- **parse**: ※僅 SSP。雖然已取得資料，但解析內容時失敗。在 rss-get/rss-post、ical-get/ical-post 中發生。
- **downloading**: ※僅 SSP。因相同 URL 的取得作業已在進行中，阻止重複取得。在 execute-http/rss/ical 中發生。 \[2.8.90\]
- **paramerror**: ※僅 SSP。因更新執行標籤設定錯誤，無法執行更新。 \[2.5.26\]
