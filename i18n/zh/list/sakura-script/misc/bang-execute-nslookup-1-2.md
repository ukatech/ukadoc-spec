# `\![execute,nslookup,パラメータ1,パラメータ2,...]`

**カテゴリ:** 未分类命令

指定主机名时查询 IP，指定 IP 时查询主机名。支持 IPv6。<br />
参数如下。

- --host=主机名或 IP
- --event=事件或标识符……指定以 On 开头的字符串时，将触发该事件（代替下文所述事件）

有关运行期间及运行结束后的事件规格，请参阅[OnNSLookupComplete](../../shiori-event/other-communication/OnNSLookupComplete.md)・[OnNSLookupFailure](../../shiori-event/other-communication/OnNSLookupFailure.md)。

**対応:** SSP

## 記述例

```sakurascript
\![execute,nslookup,--host=ssp.shillest.net,--event=nslookupテスト]ばぐとら研究所のホスト名指定でIPを調べる。調べた内容は成功時に通知されるOnNSLookupCompleteのReference3に入っている。
```
