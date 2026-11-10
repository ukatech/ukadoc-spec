# `\![execute,rss-get,URL,オプション,オプション,オプション...]`

**カテゴリ:** 未分類コマンド

使用[※選項](bang-execute-http-options-URL.note.md)執行 http get 請求，並將回應解析為 RSS/Atom feed，再將解析結果作為事件通知。<br />
參數群的指定方式與 http-post 相同。

取得的項目會透過[OnExecuteRSSComplete](../../shiori-event/other-communication/OnExecuteRSSComplete.md)通知，失敗時則透過[OnExecuteRSSFailure](../../shiori-event/other-communication/OnExecuteRSSFailure.md)通知。

\[2.8.92\] 要回傳哪些項目以及回傳幾個項目，可使用[RSS 篩選選項](bang-execute-rss-post-URL.note.md)（--from・--to・--limit）指定。若未指定，則回傳所有項目。

**対応:** SSP 篩選 2.8.92～

## 記述例

```sakurascript
\![execute,rss-get,https://example.com/feed.xml,--async=OnMyFeed,--limit=5]最新の5件をOnMyFeedで受け取る。
```

```sakurascript
\![execute,rss-get,https://example.com/feed.xml,--async=OnMyFeed,--from=20261201,--to=20261207]2026年12月1日から7日までの項目だけを受け取る。
```
