# OnRecycleBinEmpty

**カテゴリ:** OS状态事件

通过[`\![execute,emptyrecyclebin]`](../../sakura-script/misc/bang-execute-emptyrecyclebin.md)清空回收站时触发。<br />
除执行脚本的ghost外，所有正在运行的ghost也会收到OnRecycleBinEmptyFromOther通知。

- **Reference0**: 当前回收站中的文件数(刚清空后通常为0)
- **Reference1**: 当前回收站中的文件大小(刚清空后通常为0) 单位：字节
- **Reference2**: 当前回收站中的文件数与清空前的差值(刚清空后通常为负值)
- **Reference3**: 当前回收站中的文件大小与清空前的差值(刚清空后通常为负值) 单位：字节
- **Reference4**: 成功清空时为1，发生错误时为0(即使原本为空也为0)
- **Reference5**: 执行标签的ghost的主体侧名称(sakuraname)。

**対応:** SSP 2.6.04/Ref4为2.6.35
