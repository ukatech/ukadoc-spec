# `\![send,websocket,URL,data1,data2,...]`

**カテゴリ:** 未分類コマンド

接続済みのWebSocketセッションに対して、テキストフレームとして送信する。URLで対象のセッションを特定する。dataを2つ以上指定すると、それらをCRLFで結合したテキストが送られる。セッションが存在しない場合（接続前・切断後）はタグは無視される。

- URL……接続時に使ったURLと同じ文字列。
- data1,data2,……送信するUTF-8テキスト。2つ以上指定するとCRLFで結合される。

**対応:** SSP 2.8.05

## 記述例

```sakurascript
\![send,websocket,ws://example.com/chat,Hello!,World]ws://example.com/chat に "Hello!\r\nWorld" をテキストフレームとして送信する。
```
