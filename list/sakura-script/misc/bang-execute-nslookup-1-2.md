# `\![execute,nslookup,パラメータ1,パラメータ2,...]`

**カテゴリ:** 未分類コマンド

ホスト名を指定するとIP、IPを指定するとホスト名を調べる。IPv6対応。<br />
パラメータは以下の通り。

- --host=ホスト名またはIP
- --event=イベントまたは識別子……Onではじまる文字列を指定すると(後述のイベントの替わりに)そのイベントが起きる

動作中・動作後のイベントに関する仕様は[OnNSLookupComplete](../../shiori-event/other-communication/OnNSLookupComplete.md)・[OnNSLookupFailure](../../shiori-event/other-communication/OnNSLookupFailure.md)を参照。

**対応:** SSP

## 記述例

```sakurascript
\![execute,nslookup,--host=ssp.shillest.net,--event=nslookupテスト]ばぐとら研究所のホスト名指定でIPを調べる。調べた内容は成功時に通知されるOnNSLookupCompleteのReference3に入っている。
```
