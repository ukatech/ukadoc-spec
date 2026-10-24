# `\![execute,ping,パラメータ1,パラメータ2,...]`

**カテゴリ:** 未分類コマンド

指定したホストにpingを打つ。IPv6対応。<br />
パラメータは以下の通り。

- --host=ホスト名またはIP
- --ttl=TTL……(パケット生存期間(何回ルーティングできるか) 標準255
- --count=送信回数……標準3
- --size=送信サイズ……(--data有効の時は--size無効) 標準32
- --timeout=タイムアウト(ms)……標準5000
- --df=(true|false)……パケット分割不能true 分割可false 標準false
- --data=文字列……ICMP Echoのデータフィールドに埋め込む文字列(UTF-8に変換される)
- --event=イベントまたは識別子……Onではじまる文字列を指定すると(後述のイベントの替わりに)そのイベントが起きる

動作中・動作後のイベントに関する仕様は[OnPingProgress](../../shiori-event/other-communication/OnPingProgress.md)・[OnPingComplete](../../shiori-event/other-communication/OnPingProgress.md)を参照。

**対応:** SSP

## 記述例

```sakurascript
\![execute,ping,--host=ssp.shillest.net,--event=pingテスト]ばぐとら研究所にデフォルト設定でpingを打つ。
```
