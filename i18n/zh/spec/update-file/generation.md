# 生成处理

通过SSP的「创建更新文件」功能等，可以根据ghost的文件列表生成updates2.dau / updates.txt。

- **文件扫描**: 递归扫描目录。以下文件会被排除。

  - 隐藏文件 (`FILE_ATTRIBUTE_HIDDEN`)
  - [developer_options.txt](../../descript/install/developer_options.txt/index.md) 中通过 `noupdate` 指定的文件
  - 被.gitignore格式的过滤文件排除的文件

- **复制到ghost\\master**: 如果目录直属位置存在 `ghost\master` 文件夹，也会将生成的更新文件复制到该目录。
