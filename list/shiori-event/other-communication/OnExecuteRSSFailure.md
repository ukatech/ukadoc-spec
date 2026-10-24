# OnExecuteRSSFailure

**カテゴリ:** その他通信イベント

`\![execute,rss-get/post]`で取得エラーした際に発生。

- **Reference0～**: 解析失敗時はReference4=parse。同じURLの取得がすでに進行中だった場合はReference4=downloading \[2.8.90\]。他は[OnExecuteHTTPFailureと同じ](OnExecuteHTTPFailure.md)

**対応:** SSP
