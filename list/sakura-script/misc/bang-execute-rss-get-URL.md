# `\![execute,rss-get,URL,オプション,オプション,オプション...]`

**カテゴリ:** 未分類コマンド

[※オプション](notes_executehttp.md)付きでhttp get リクエストを行い、レスポンスをRSS/Atomフィードとして解析したのち、解析結果をイベントとして通知する。<br />
パラメータ群の指定はhttp-postと同じ。

取得した項目は[OnExecuteRSSComplete](../../shiori-event/other-communication/OnExecuteRSSComplete.md)、失敗時は[OnExecuteRSSFailure](../../shiori-event/other-communication/OnExecuteRSSFailure.md)で通知される。

\[2.8.92\] どの項目をいくつ返すかは[RSS絞り込みオプション](notes_executerss.md)（--from・--to・--limit）で指定できる。無指定の場合は全項目を返す。

**対応:** SSP 絞り込み 2.8.92～

## 記述例

```sakurascript
\![execute,rss-get,https://example.com/feed.xml,--async=OnMyFeed,--limit=5]最新の5件をOnMyFeedで受け取る。
```

```sakurascript
\![execute,rss-get,https://example.com/feed.xml,--async=OnMyFeed,--from=20261201,--to=20261207]2026年12月1日から7日までの項目だけを受け取る。
```
