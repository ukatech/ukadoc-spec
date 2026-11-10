# `\![execute,nslookup,パラメータ1,パラメータ2,...]`

**カテゴリ:** Unclassified command

Specify a hostname to look up its IP, or an IP to look up its hostname. Supports IPv6.<br />
The parameters are as follows.

- --host=hostname or IP
- --event=event or identifier……If a string starting with On is specified, that event occurs instead of the event described below

See [OnNSLookupComplete](../../shiori-event/other-communication/OnNSLookupComplete.md) and [OnNSLookupFailure](../../shiori-event/other-communication/OnNSLookupFailure.md) for the specifications of events during and after execution.

**対応:** SSP

## 記述例

```sakurascript
\![execute,nslookup,--host=ssp.shillest.net,--event=nslookupテスト]ばぐとら研究所のホスト名指定でIPを調べる。調べた内容は成功時に通知されるOnNSLookupCompleteのReference3に入っている。
```
