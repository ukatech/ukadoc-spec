# 网络更新失败原因

- **timeout**: 超时。
- **too slow**: *在 SSP 中会变成 timeout，因此不发出*。网络连接非常慢。
- **md5 miss**: MD5 不匹配。
- **artificial**: 用户操作导致更新中断。
- **404 等**: 因该状态码导致失败。
- **fileio**: ※仅 SSP。因空间不足，无法写入更新目标。
- **readonly**: ※仅 SSP。因只读标志，无法写入更新目标。文件或文件夹带有只读标志时会发生。
- **virusdetect**: ※仅 SSP。可能在数据中检测到了病毒。 \[2.5.15\]
- **toomanyredirect**: ※仅 SSP。因重定向次数过多而中止处理。 \[2.5.15\]
- **executing**: ※仅 SSP。由于更新已在执行中，阻止重复启动。 \[2.5.26\]
- **parse**: ※仅 SSP。虽然获取成功，但解析内容失败。在 rss-get/rss-post・ical-get/ical-post 中发生。
- **downloading**: ※仅 SSP。由于同一 URL 的获取已在进行中，阻止重复获取。在 execute-http/rss/ical 中发生。 \[2.8.90\]
- **paramerror**: ※仅 SSP。由于更新执行标签的设置错误，无法执行更新。 \[2.5.26\]
