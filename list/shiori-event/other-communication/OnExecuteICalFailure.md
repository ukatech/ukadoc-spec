# OnExecuteICalFailure

**カテゴリ:** その他通信イベント

`\![execute,ical-get/ical-post]`で取得エラーした際に発生。

- **Reference0～**: 解析失敗時はReference4=parse。同じURLの取得がすでに進行中だった場合はReference4=downloading。他は[OnExecuteHTTPFailureと同じ](OnExecuteHTTPFailure.md)（Completeとは並びが違う点に注意）。

**対応:** SSP 2.8.90
