# `\![execute,rss-get,URL,オプション,オプション,オプション...]`

**カテゴリ:** Unclassified commands

Send an http get request with [※options](bang-execute-http-options-URL.note.md), parse the response as an RSS/Atom feed, and then notify the parsing results as events.<br />
Specify the parameters in the same way as for http-post.

The retrieved items are reported through [OnExecuteRSSComplete](../../shiori-event/other-communication/OnExecuteRSSComplete.md), and failures through [OnExecuteRSSFailure](../../shiori-event/other-communication/OnExecuteRSSFailure.md).

\[2.8.92\] The [RSS filtering options](bang-execute-rss-post-URL.note.md) (--from, --to, --limit) specify which items to return and how many. If no options are specified, all items are returned.

**対応:** SSP filtering from 2.8.92 onward

## 記述例

```sakurascript
\![execute,rss-get,https://example.com/feed.xml,--async=OnMyFeed,--limit=5]最新の5件をOnMyFeedで受け取る。
```

```sakurascript
\![execute,rss-get,https://example.com/feed.xml,--async=OnMyFeed,--from=20261201,--to=20261207]2026年12月1日から7日までの項目だけを受け取る。
```
