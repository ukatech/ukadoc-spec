# `\![execute,ping,パラメータ1,パラメータ2,...]`

**カテゴリ:** Uncategorized command

Ping the specified host. Supports IPv6.<br />
The parameters are as follows.

- --host=hostname or IP address
- --ttl=TTL……(packet lifetime (number of times it can be routed); default 255
- --count=number of packets to send……default 3
- --size=packet size……(--size is ignored when --data is enabled) default 32
- --timeout=timeout (ms)……default 5000
- --df=(true|false)……true: packet fragmentation disabled; false: fragmentation allowed; default false
- --data=string……String to embed in the ICMP Echo data field (converted to UTF-8)
- --event=event or identifier……If a string beginning with On is specified, that event is raised instead of the event described below

For details about events during and after execution, see [OnPingProgress](../../shiori-event/other-communication/OnPingProgress.md) and [OnPingComplete](../../shiori-event/other-communication/OnPingProgress.md).

**対応:** SSP

## 記述例

```sakurascript
\![execute,ping,--host=ssp.shillest.net,--event=pingテスト]ばぐとら研究所にデフォルト設定でpingを打つ。
```
