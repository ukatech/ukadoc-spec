# OnExecuteRSSComplete

**カテゴリ:** 其他通信事件

通过`\![execute,rss-get/post]`成功获取内容时触发。

\[2.8.92\] 返回的项目数量及其顺序由[RSS筛选选项](../../sakura-script/misc/bang-execute-rss-post-URL.note.md)决定。

- **Reference0～**: 标题 \[`\1`\] URL \[`\1`\] 更新时间（格式为逗号分隔：年,月,日,时,分,秒）\[`\1`\] 作者名 \[`\1`\] 内容或摘要<br />
  有更新时，将按RSS中的项目数依次追加Reference0、1、2～<br />
  \[`\1`\]是字节值1

**対応:** SSP 作者名・内容 2.4.10～
