# OnExecuteRSSFailure

**カテゴリ:** 其他通信事件

通过`\![execute,rss-get/post]`获取时发生错误时触发。

- **Reference0～**: 解析失败时，Reference4=parse。如果相同URL的获取已经在进行中，则Reference4=downloading \[2.8.90\]。其他内容与[OnExecuteHTTPFailure相同](OnExecuteHTTPFailure.md)

**対応:** SSP
