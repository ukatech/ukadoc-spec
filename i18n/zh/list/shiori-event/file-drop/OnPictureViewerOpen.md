# OnPictureViewerOpen

**カテゴリ:** 文件拖放事件

文件被拖放后，若幽灵未响应 OnFileDrop2（或执行了[`\![execute,dropdefault,file]`](../../sakura-script/misc/bang-execute-dropdefault-file-.-bang-execute-dropdefault-url-URL.md)，\[2.9.10\]），并且图片查看器已打开时触发。Reference 与 OnFileDrop2 相同。

- **Reference0**: 被拖放文件的路径。有多个文件/目录时，以 byte 值1分隔。
- **Reference1**: 被拖放角色的 scope 编号。本体侧为0，搭档为1，第三人及之后为2以上。
- **Reference2**: 被拖放文件的 MIME 类型。有多个文件/目录时，以 byte 值1分隔。

**対応:** SSP 2.8.51
