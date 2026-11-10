# OnFileDrop2

**カテゴリ:** 文件拖放事件

文件被拖放时触发。这是目前最新规格的事件。<br />
响应此事件后，不会执行本体的默认处理（在图像查看器、媒体播放器或归档查看器中打开）。若要在响应事件的同时执行默认处理，请使用[`\![execute,dropdefault,file]`](../../sakura-script/misc/bang-execute-dropdefault-file-.-bang-execute-dropdefault-url-URL.md)。\[2.9.10\]

- **Reference0**: 被拖放文件的路径。有多个文件/目录时，以字节值 1 分隔。
- **Reference1**: 被拖放角色的 scope 编号。本体侧为 0，搭档为 1，第三人及之后为 2 及以上。
- **Reference2**: 被拖放文件的 MIME 类型（SSP 2.7.98 及更高版本）。有多个文件/目录时，以字节值 1 分隔。

**対応:** Materia / SSP / CROW / Ninix
