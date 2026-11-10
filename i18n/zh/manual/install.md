# 安装

关于如何创建分发用归档，请参阅“[创建分发用文件](../dev/nar.md)”页面。

ghost 通常以扩展名为`nar`的归档形式分发（nar。Nanika ARchive）。

nar只是将zip的扩展名改成了nar，实际内容仍是zip，因此有些服务器也会以zip格式分发。

虽然只要有解压DLL，lzh也可以安装，但除非有充分理由，否则不要使用。

在SSP中，也可以安装cab或自解压exe。

可以解压归档后手动安装，但如果正确准备了`install.txt`，就可以通过拖放等方式调用安装程序功能，自动完成安装。

将包含install.txt的ghost文件夹拖放到baseware（SSP）本体上，即可创建nar。

这与手动压缩为zip后再重命名的效果相同，但要注意不要让文件夹层级过深。

分发ghost时，注意不要包含ghost和shell文件夹中的profile文件夹或存档数据等内容。

网络更新也同样如此。

SSP提供了`developer_options.txt`来控制这一点。

- **标准ghost的情况**:

  ```filetree
  +-(myghost)
  　　+-ghost
  　　+-shell
  　　+-install.txt
  　　+-developer_options.txt (SSPのみ)
  　　+-readme.txt
  　　+-thumbnail.png
  　　:
  　　:
  ```

  !!! tip "提示"

      对于*supplement*，保持上述内容的*文件夹结构不变*，仅包含要添加的文件并将其打包为归档。

      例如，要将dic_supplement.txt文件添加到ghost/master/中

      ```filetree
      +-(mysupplement)
      　　+-install.txt
      　　+-developer_options.txt (SSPのみ)
      　　+-ghost
      　　　　+-master
      　　　　　　+-dic_supplement.txt
      ```

      即可。

- **标准附加shell的情况**:

  ```filetree
  +-(additional_shell)
  　　+-install.txt
  　　+-developer_options.txt (SSPのみ)
  　　+-descript.txt
  　　+-readme.txt
  　　+-thumbnail.png
  　　+-surface*.png
  　　+-surfaces.txt
  　　:
  　　:
  ```

- **标准balloon的情况**:

  ```filetree
  +-(myballoon)
  　　+-install.txt
  　　+-developer_options.txt (SSPのみ)
  　　+-descript.txt
  　　+-balloonc*.png
  　　+-balloons*.png
  　　+-balloonk*.png
  　　:
  　　:
  ```

- **在ghost中附带balloon等内容的情况**:

  ```filetree
  +-(myghost)
  　　+-install.txt
  　　+-developer_options.txt (SSPのみ)
  　　+-ghost
  　　+-shell
  　　+-(myballoon)
  　　　　+-descript.txt
  　　　　+-balloons0.png
  　　　　:
  　　　　:
  ```

  plugin等也同样处理（如果要附带shell，则不应采用这种结构，直接放在shell文件夹下即可）。

  另外，被附带的内容（上例中的balloon）不需要install.txt。即使存在也会被忽略。

- **(仅限SSP)多项安装用软件包**:

  ```filetree
  +-(mypackage)
  　　+-install.txt (package用)
  　　+-(myghost1)
  　　　　+-install.txt (myghost1用)
  　　　　+-developer_options.txt (SSPのみ)
  　　　　+-ghost
  　　　　+-shell
  　　　　:
  　　+-(myghost2)
  　　　　+-install.txt (myghost2用)
  　　　　+-developer_options.txt (SSPのみ)
  　　　　+-ghost
  　　　　+-shell
  　　　　:
  ```

  请注意，软件包本身和各个内容都需要分别准备install.txt。

  不限于ghost，任何可以单独打包为归档的内容都可以附带，但对于shell或supplement等有特定目标的内容，请注意不要混入目标不同的内容。

其他内容也同样如此，例如headline sensor或单独分发的plugin，都要将install.txt放在最上层目录中。

- **[install.txt](../descript/install/index.md)**: 描述安装设置的文本文件。

  如果没有此文件，通过拖放等方式触发的自动安装功能将无法运行。

  设置归档内容的类型、归档名称、目录名等。

  详情请参阅[链接目标](../descript/install/index.md)。

- **[developer_options.txt](../descript/install/developer_options.txt/index.md)**: 仅限SSP。可省略。

  将其放在与install.txt相同的位置。

  但请注意，对于多项安装用软件包，应将其放在各个内容的install.txt所在位置，而不是最上层install.txt所在位置。

  这是在SSP中创建nar时，用于设置不包含在目标中的文件等内容的文件。

  关于格式等详细信息，请参阅[链接目标](../descript/install/developer_options.txt/index.md)。
