# ghost

master ghost folder中的文件如下。

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

- **[descript.txt](../descript/ghost/index.md)**：用于识别 ghost 的文件。

  没有此文件，主体将无法识别它。

  关于文本中的记载事项等详情，请参阅[链接目标](../descript/ghost/index.md)。

- **[updates2.dau](update.md)**

- **[updates.txt](update.md)**：记载更新信息的文件。

  此处是旧规格，通常只需放在根目录（(myghost) 直下）。

  详情请参阅[链接目标](update.md)。

- **shiori.dll**：ghost 的核心，几乎是必需的。

  有许多通用 SHIORI，通常使用这些即可。

  接收由 baseware（如 SSP）发送的[SHIORI Event](../list/shiori-event/index.md)（[补充说明](../memo/shiori-event.md)），构建作为 ghost 动作指示的[Sakura Script](../list/sakura-script/index.md)，并将其返回给 baseware。

  实际对话的编写方法等 ghost 核心部分的制作方式因 SHIORI 而完全不同，请参阅各 SHIORI 的文档。

- **(saori).dll**：SHIORI 的功能扩展模块。

  基本上放置在与 shiori.dll 相同的目录层级。

  但也可以在从 SHIORI 调用时指定相对路径。

  使用步骤取决于 SHIORI，请参阅 SHIORI 的文档。

  此文件可以省略。

- **[makoto.dll](translator.md)**：用于转换的 DLL。

  详情请参阅[链接目标](translator.md)。也可以放置在[shell 侧](shell.md)。

  此文件可以省略。

- **\*.ico**：图标文件。

  可以使用 32×32 和 16×16 的图标。

  在图标化时或在 ghost Explorer 等位置显示。

  此文件可以省略。省略时将使用默认图标。

- **\*.cur**：光标文件。

  鼠标光标移到 ghost 上时会变为指定的光标。

  此文件可以省略。省略时保持常规光标。

- **thumbnail.png**：在菜单树中选择 ghost 时显示的缩略图。

  可以使用的图像格式为 png 或 jpg。

  将 png 重命名为 pnr 后，图像左上角的 1 个点（坐标 0,0）同色部分将变为透明。

  此文件可以省略。

- **ai0.png / ai0_dark.png**：请参阅[AI 图表说明](../descript/ghost/descript-txt/shiori.logo.file.md)。

  此文件可以省略。

此外，SHIORI（等）通常还会在 dll 外部配备若干文件，例如称为“词典”的字符串资源文件（实际上，ghost 制作者也经常主要编辑这些文件）。<br />
关于这些文件的详情，请参阅所用各 SHIORI 的文档。
