# `\![execute,ping,パラメータ1,パラメータ2,...]`

**カテゴリ:** 未分類命令

對指定主機發送 ping。支援 IPv6。<br />
參數如下。

- --host=主機名稱或 IP
- --ttl=TTL……（封包存留時間（可路由的次數），預設255
- --count=傳送次數……預設3
- --size=傳送大小……（--data 有效時 --size 無效）預設32
- --timeout=逾時時間（ms）……預設5000
- --df=(true|false)……true 表示不可分割封包，false 表示可分割，預設 false
- --data=字串……嵌入 ICMP Echo 資料欄位的字串（會轉換為 UTF-8）
- --event=事件或識別碼……指定以 On 開頭的字串時，會觸發該事件（取代下述事件）

關於執行中及執行後的事件規格，請參閱[OnPingProgress](../../shiori-event/other-communication/OnPingProgress.md)・[OnPingComplete](../../shiori-event/other-communication/OnPingProgress.md)。

**対応:** SSP

## 記述例

```sakurascript
\![execute,ping,--host=ssp.shillest.net,--event=pingテスト]ばぐとら研究所にデフォルト設定でpingを打つ。
```
