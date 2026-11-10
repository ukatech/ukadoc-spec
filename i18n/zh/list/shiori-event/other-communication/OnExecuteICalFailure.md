# OnExecuteICalFailure

**カテゴリ:** 其他通信事件

通过`\![execute,ical-get/ical-post]`获取时发生错误时触发。

- **Reference0～**: 解析失败时，Reference4=parse。如果相同URL的获取已经在进行中，则Reference4=downloading。其他内容与[OnExecuteHTTPFailure相同](OnExecuteHTTPFailure.md)（请注意其顺序与Complete不同）。

**対応:** SSP 2.8.90
