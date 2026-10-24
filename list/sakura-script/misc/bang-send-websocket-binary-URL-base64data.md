# `\![send,websocket-binary,URL,base64data]`

**カテゴリ:** 未分類コマンド

接続済みのWebSocketセッションに対して、バイナリフレームとして送信する。URLで対象のセッションを特定する。セッションが存在しない場合はタグは無視される。

- URL……接続時に使ったURLと同じ文字列。
- base64data……Base64エンコードされたバイナリデータ。

**対応:** SSP 2.8.05

## 記述例

```sakurascript
\![send,websocket-binary,ws://example.com/stream,SGVsbG8=]ws://example.com/stream に Base64デコードしたバイナリデータをバイナリフレームとして送信する。
```
