# `\![execute,ping,パラメータ1,パラメータ2,...]`

**カテゴリ:** 未分类命令

向指定主机发送 ping。支持 IPv6。<br />
参数如下。

- --host=主机名或 IP
- --ttl=TTL……（数据包生存时间，即可路由次数）默认255
- --count=发送次数……默认3
- --size=发送大小……（--data 有效时 --size 无效）默认32
- --timeout=超时时间（ms）……默认5000
- --df=(true|false)……true 表示禁止拆分数据包，false 表示允许拆分，默认 false
- --data=字符串……嵌入 ICMP Echo 数据字段的字符串（将转换为 UTF-8）
- --event=事件或标识符……指定以 On 开头的字符串时，将触发该事件（代替下文所述事件）

有关运行期间及运行结束后的事件规格，请参阅[OnPingProgress](../../shiori-event/other-communication/OnPingProgress.md)・[OnPingComplete](../../shiori-event/other-communication/OnPingProgress.md)。

**対応:** SSP

## 記述例

```sakurascript
\![execute,ping,--host=ssp.shillest.net,--event=pingテスト]ばぐとら研究所にデフォルト設定でpingを打つ。
```
