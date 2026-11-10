# OnExecuteICalFailure

**カテゴリ:** 其他通訊事件

`\![execute,ical-get/ical-post]`發生取得錯誤時觸發。

- **Reference0～**: 解析失敗時為Reference4=parse。同一個URL的取得已在進行中時，則為Reference4=downloading。其他情況與[OnExecuteHTTPFailure相同](OnExecuteHTTPFailure.md)（請注意，順序與Complete不同）。

**対応:** SSP 2.8.90
