# OnRSSComplete

**カテゴリ:** 标题/RSS感知事件

标题感知正常结束时触发。如果未对此事件作出响应，则会生成适合显示的脚本，并调用标题感知完成类事件。

- **Reference0**: 无更新时：no update　[※结束原因](caption_headlinesenseresult.md)<br />
  无更新时，仅有Reference0，且内容只有字符串"no update"<br />
  有更新时：RSS分发网站名称。
- **Reference1**: 仅有更新时：RSS来源URL（指向分发网站，而非Feed本身）
- **Reference2～**: 仅有更新时：标题 \[`\1`\] URL \[`\1`\] 更新时间（格式为逗号分隔：年,月,日,时,分,秒）\[`\1`\] 作者名 \[`\1`\] 内容或摘要<br />
  有更新时，将按RSS元素数量依次提供Reference0、1、2～<br />
  \[`\1`\]是字节值1

**対応:** SSP 作者名、内容 2.4.10～
