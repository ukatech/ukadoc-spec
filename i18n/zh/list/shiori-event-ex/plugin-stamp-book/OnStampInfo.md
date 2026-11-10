# OnStampInfo

**カテゴリ:** 插件“印章簿”

通知印章相关信息的事件。<br />
在ghost启动、插件加载或卸载时，以及发送OnStampInfoCall时的任意时刻触发。

- **Reference0**: 印章总数。
- **Reference1**: 是否存在该ghost的印章。存在时为1，不存在时为0。<br />
  同时启动多个ghost时，此信息的可靠性会降低。若要确切了解，建议通过OnStampInfoCall主动触发此事件。
- **Reference2**: 插件路径。
- **Reference3**: 所有印章信息。每条信息包含ghost名称、印章图像文件名、印章标题、印章评论和盖章时间，各字段以字节值1分隔；每条信息再以字节值2分隔，按印章数量依次排列。
- **Reference4**: 此插件正在运行时为1，否则为0。
