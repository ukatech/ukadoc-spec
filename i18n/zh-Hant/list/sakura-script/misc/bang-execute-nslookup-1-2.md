# `\![execute,nslookup,パラメータ1,パラメータ2,...]`

**カテゴリ:** 未分類命令

指定主機名稱時查詢 IP，指定 IP 時查詢主機名稱。支援 IPv6。<br />
參數如下。

- --host=主機名稱或 IP
- --event=事件或識別碼……指定以 On 開頭的字串時，會觸發該事件（取代下述事件）

關於執行中及執行後的事件規格，請參閱[OnNSLookupComplete](../../shiori-event/other-communication/OnNSLookupComplete.md)・[OnNSLookupFailure](../../shiori-event/other-communication/OnNSLookupFailure.md)。

**対応:** SSP

## 記述例

```sakurascript
\![execute,nslookup,--host=ssp.shillest.net,--event=nslookupテスト]ばぐとら研究所のホスト名指定でIPを調べる。調べた内容は成功時に通知されるOnNSLookupCompleteのReference3に入っている。
```
