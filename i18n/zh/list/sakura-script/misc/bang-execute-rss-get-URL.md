# `\![execute,rss-get,URL,オプション,オプション,オプション...]`

**カテゴリ:** 未分类命令

使用[※选项](bang-execute-http-options-URL.note.md)执行 http get 请求，将响应解析为 RSS/Atom feed 后，将解析结果作为事件通知。<br />
参数组的指定方式与 http-post 相同。

获取的项目通过[OnExecuteRSSComplete](../../shiori-event/other-communication/OnExecuteRSSComplete.md)通知，失败时则通过[OnExecuteRSSFailure](../../shiori-event/other-communication/OnExecuteRSSFailure.md)通知。

\[2.8.92\] 要返回哪些项目以及返回多少项，可通过[RSS筛选选项](bang-execute-rss-post-URL.note.md)（--from・--to・--limit）指定。不指定时返回所有项目。

**対応:** SSP 支持筛选 2.8.92～

## 記述例

```sakurascript
\![execute,rss-get,https://example.com/feed.xml,--async=OnMyFeed,--limit=5]最新の5件をOnMyFeedで受け取る。
```

```sakurascript
\![execute,rss-get,https://example.com/feed.xml,--async=OnMyFeed,--from=20261201,--to=20261207]2026年12月1日から7日までの項目だけを受け取る。
```
