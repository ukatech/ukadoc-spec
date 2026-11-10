# OnExecuteRSSComplete

**カテゴリ:** 其他通信事件

透過 `\![execute,rss-get/post]` 成功取得資料時觸發。

\[2.8.92\] 項目的數量與排列方式由 [RSS 篩選選項](../../sakura-script/misc/bang-execute-rss-post-URL.note.md) 決定。

- **Reference0～**: 標題 \[`\1`\] URL \[`\1`\] 更新時間（格式為逗號分隔：年,月,日,時,分,秒）\[`\1`\] 作者名稱 \[`\1`\] 內容或摘要<br />
  有更新時，會依 RSS 項目數量，依序列出 Reference0,1,2～<br />
  \[`\1`\] 是位元組值 1

**対応:** SSP 作者名稱・內容 2.4.10～
