# OnArchiveViewerOpen

**カテゴリ:** 文件拖放事件

文件被拖放，ghost 未响应 OnFileDrop2（或执行了[`\![execute,dropdefault,file]`](../../sakura-script/misc/bang-execute-dropdefault-file-.-bang-execute-dropdefault-url-URL.md)，\[2.9.10\]），且打开了归档查看器时触发。Reference 与 OnFileDrop2 相同。

- **Reference0**: 被拖放文件的路径。有多个文件/目录时，以字节值 1 分隔。
- **Reference1**: 被拖放角色的 scope 编号。本体侧为 0，搭档为 1，第三人及之后为 2 及以上。
- **Reference2**: 被拖放文件的 MIME 类型。有多个文件/目录时，以字节值 1 分隔。

**対応:** SSP 2.8.57
