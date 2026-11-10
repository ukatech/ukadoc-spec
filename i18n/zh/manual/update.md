# 网络更新

有关网络更新的设置等内容，请参阅“[网络更新支持](../dev/update.md)”页面。

与网络更新相关的文件布局如下。

- **ghost 的情况**:

  ```filetree
  +-(myghost)
  　　+-ghost
  　　+-shell
  　　+-updates2.dau
  　　+-updates.txt
  　　+-delete.txt
  　　+-delete1.txt (SSPのみ・delete[数字].txtを認識可)
  　　+-developer_options.txt (SSPのみ)
  　　+-readme.txt
  　　+-thumbnail.png
  ```

- **(仅限 SSP)使附加 shell 支持网络更新时**:

  ```filetree
  +-(myshell)
  　　+-ghost
  　　+-shell
  　　+-updates2.dau
  　　+-updates.txt
  　　+-delete.txt
  　　+-delete1.txt (SSPのみ・delete[数字].txtを認識可)
  　　+-developer_options.txt
  　　+-readme.txt
  　　+-thumbnail.png
  ```

- **(仅限 SSP)使 balloon 支持网络更新时**:

  ```filetree
  +-(myballoon)
  　　+-updates2.dau
  　　+-updates.txt
  　　+-delete.txt
  　　+-delete1.txt (SSPのみ・delete[数字].txtを認識可)
  　　+-developer_options.txt
  　　+-descript.txt
  　　+-balloons*s.txt
  　　+-balloonk*s.txt
  　　+-readme.txt
  　　+-balloons*.png
  　　+-balloonk*.png
  　　:
  　　:
  ```

  plugin、headline sensor 等也一样，放在对应文件夹中即可。

- **updates2.dau**: 列出了更新目标文件的 MD5 哈希值等信息的文件。

  网络更新时，用它来检测服务器上的文件与实际下载的文件之间是否存在文件损坏或篡改等情况。

  通常使用 baseware 的功能等生成，无需手动编辑。

  有关生成步骤等内容，请参阅“[网络更新支持](../dev/update.md)”页面

- **updates.txt**: 与 updates2.dau 的作用几乎相同。提供其中一个即可（同时提供也没有问题）。

  除了格式略有不同之外，还可以避免因扩展名限制而无法上传 dau 等问题。

- **[delete.txt](../descript/install/delete.txt/index.md)**: 文件删除设置文件。

  将它放在服务器上与 updates2.dau 相同的位置。

  用于防止不再需要的文件不断堆积等情况。

  有关格式等详细信息，请参阅[链接页面](../descript/install/delete.txt/index.md)。

- **[developer_options.txt](../descript/install/developer_options.txt/index.md)**: 仅限 SSP。

  将它放在要生成 updates2.dau 的位置（最顶层目录）。

  在 SSP 中生成 updates2.dau（updates.txt）时，用它指定不纳入更新目标的文件等。

  无需上传到服务器（例如，可将该文件自身指定为排除文件），但即使保留也没有坏处。可根据用户之后重新打包为 nar 等情况灵活处理。

  有关格式等详细信息，请参阅[链接页面](../descript/install/developer_options.txt/index.md)。
