# ghost

master ghost 文件夹中的文件如下。

```filetree
+-(myghost)
　　+-ghost
　　　　+-master
　　　　　　+-descript.txt
　　　　　　+-shiori.dll
　　　　　　+-(saori).dll
　　　　　　+-makoto.dll
　　　　　　+-updates2.dau （旧仕様）
　　　　　　+-updates.txt （旧仕様）
　　　　　　+-*.ico
　　　　　　+-*.cur
　　　　　　+-thumbnail.png
　　　　　　+-ai0.png
　　　　　　+-ai0_dark.png
```

- **[descript.txt](../descript/ghost/index.md)**: 用于识别 ghost 的文件。

  没有此文件则不会被 baseware 识别。

  文本中的记载内容等详细信息参见[链接](../descript/ghost/index.md)。

- **[updates2.dau](update.md)**

- **[updates.txt](update.md)**: 记载更新信息的文件。

  放在此位置是旧规格，通常只需放在根目录（(myghost) 下）即可。

  详情参见[链接](update.md)

- **shiori.dll**: ghost 的核心。几乎必需。

  目前有许多通用 SHIORI，通常使用其中之一。

  接收 baseware（如 SSP）发送的 [SHIORI Event](../list/shiori-event/index.md)（[补充说明](../memo/shiori-event.md)），构建作为 ghost 行为指令的 [Sakura Script](../list/sakura-script/index.md)，并将其返回给 baseware。

  实际对话的写法等 ghost 核心部分的制作方法因 SHIORI 而完全不同，请参阅各 SHIORI 的文档。

- **(saori).dll**: SHIORI 的功能扩展模块。

  基本上与 shiori.dll 放在同一层级。

  不过从 SHIORI 调用时也可以指定相对路径。

  使用步骤取决于 SHIORI，请参阅相应 SHIORI 的文档。

  此文件可省略。

- **[makoto.dll](translator.md)**: 用于转换的 DLL。

  详情参见[链接](translator.md)。也可放在 [shell 侧](shell.md)。

  此文件可省略。

- **\*.ico**: 图标文件。

  可使用 32×32 和 16×16 的图标。

  图标化时以及在 ghost 资源管理器等位置显示。

  此文件可省略。省略时使用默认图标。

- **\*.cur**: 光标文件。

  光标移动到 ghost 上时会变为指定的光标。

  此文件可省略。省略时保持普通光标。

- **thumbnail.png**: 在菜单树中选择 ghost 时显示的缩略图。

  可使用的图片格式为 png 或 jpg。

  将 png 重命名为 pnr 后，图片左上角的 1 个像素（坐标 0,0）的同色区域会变为透明。

  此文件可省略。

- **ai0.png / ai0_dark.png**: 参见 [AI 图表说明](../descript/shell/descript-txt/shiori.logo.file.md)。

  此文件可省略。

此外，SHIORI 等通常还会在 dll 外部配备一些文件，例如称为“字典”的字符串资源文件（ghost 制作者往往主要编辑这些文件）。<br />
这些文件的详情请参阅所用 SHIORI 的文档。
