# `\![execute,ping,パラメータ1,パラメータ2,...]`

**カテゴリ:** Unclassified command

Ping the specified host. Supports IPv6.<br />
The parameters are as follows.

- --host=hostname or IP
- --ttl=TTL……(packet lifetime (number of times it can be routed); default 255
- --count=number of transmissions……default 3
- --size=transmission size……(--size is ignored when --data is enabled); default 32
- --timeout=timeout (ms)……default 5000
- --df=(true|false)……true means packets cannot be fragmented; false means fragmentation is allowed; default false
- --data=string……String embedded in the ICMP Echo data field (converted to UTF-8)
- --event=event or identifier……If a string starting with On is specified, that event occurs instead of the event described below

See [OnPingProgress](../../shiori-event/other-communication/OnPingProgress.md) and [OnPingComplete](../../shiori-event/other-communication/OnPingProgress.md) for the specifications of events during and after execution.

**対応:** SSP

## 記述例

```sakurascript
\![execute,ping,--host=ssp.shillest.net,--event=pingテスト]ばぐとら研究所にデフォルト設定でpingを打つ。
```
