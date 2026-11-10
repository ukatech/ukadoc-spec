# 整体结构

## ghost 与 shell

ghost 的构成文件放置在 baseware（SSP、materia 等）的 ghost 存放文件夹中。

所有 ghost 都必须有一个 master ghost 和 master shell。

从 shell 的角度来看，所有 shell 都必须属于某一个 ghost。

因此，两者的文件结构如下所示，shell 包含在 ghost 中。

```filetree
+-(myghost)
　　+-ghost
　　　　+-master
　　　　　　+-descript.txt
　　　　　　+-shiori.dll
　　　　　　+-makoto.dll
　　　　　　+-updates2.dau
　　　　　　+-*.ico
　　　　　　+-*.cur
　　+-shell
　　　　+-master
　　　　　　+-descript.txt
　　　　　　+-surface*.png
　　　　　　+-surface*.pna
　　　　　　+-(element).png
　　　　　　+-(element).pna
　　　　　　+-surfaces.txt
　　　　　　+-makoto.dll (必要な時のみ)
　　　　　　+-menu_background.png
　　　　　　+-menu_foreground.png
　　　　　　+-menu_sidebar.png
　　　　　　+-readme.txt (必要な時のみ)
　　　　　　+-thumbnail.png
　　　　　　+-surfaces**.txt (SSPのみ）
　　　　　　+-surfacetable.txt (必要な時のみ)(SSPのみ)
　　　　　　+-alias.txt (必要な時のみ)(旧仕様）
　　　　+-(additional_shell)
　　+-delete.txt (必要な時のみ)
　　+-delete1.txt (delete[数字].txtも追加で認識できる)
　　+-developer_options.txt (必要な時のみ)(SSPのみ)
　　+-.narignore (必要な時のみ)(SSPのみ)
　　+-.updateignore (必要な時のみ)(SSPのみ)
　　+-.narinclude (必要な時のみ)(SSPのみ)
　　+-.updateinclude (必要な時のみ)(SSPのみ)
　　+-readme.txt または readme.md (必要な時のみ)
　　+-terms.txt または terms.md (必要な時のみ)
　　+-thumbnail.png
```

## balloon

balloon 不是按 ghost 分别管理，而是由一个 baseware 统一管理，并由所有 ghost 共享。

各 balloon 的构成文件放置在 baseware 的 balloon 存放文件夹下，结构如下所示。

```filetree
+-(myballoon)
　　+-descript.txt
　　+-balloons*s.txt
　　+-balloonk*s.txt
　　+-readme.txt または readme.md (必要な時のみ)
　　+-terms.txt または terms.md (必要な時のみ)
　　+-balloons*.png
　　+-balloonk*.png
　　+-balloons*.pna （MATERIA不可）
　　+-balloonk*.pna （MATERIA不可）
　　+-balloonc*.png
　　+-online*.png
　　+-sstp.png
　　+-arrow*.png
　　+-thumbnail.png
　　+-ok_down.png/ok_up.png （SSPのみ）
　　+-cancel_down.png/cancel_up.png （SSPのみ）
　　+-mode_down.png/mode_up.png （SSPのみ）
　　+-sstp_new.png （SSPのみ）
　　+-marker.png （SSPのみ）
　　+-delete.txt (SSPのみ・必要な時のみ)
　　+-delete1.txt (delete[数字].txtも追加で認識できる)
```

- **(myghost)\\**：各 ghost 主目录（根文件夹）。

  文件夹名称建议使用英数字。

- **(myghost)\\ghost\\**：用于 ghost 内部运行的文件夹。

- **(myghost)\\ghost\\master\\**：ghost 默认使用的文件夹。

  目前只使用 master（这是过去设计遗留下来的）。

ghost 文件夹内文件结构的详细信息，请参阅「[ghost](ghost.md)」页面。

有关 makoto.dll，请参阅「[转换器](translator.md)」页面。

- **(myghost)\\shell\\**：用于存放 ghost 的 shell（用于显示图形的一组文件）的文件夹。

- **(myghost)\\shell\\master\\**：默认 shell 的文件夹。必需。

- **(myghost)\\shell\\(additional_shell)\\**：附加 shell 的文件夹。名称任意（建议使用英数字）。文件结构与 master 相同。

  可以存在任意多个。存在时，可以通过 owner draw 菜单等进行切换选择。

shell 文件夹内文件结构的详细信息，请参阅「[shell](shell.md)」页面。

有关 menu_background.png、menu_foreground.png、menu_sidebar.png，请参阅「[owner draw 菜单](owner-draw-menu.md)」页面。

有关 makoto.dll，请参阅「[转换器](translator.md)」页面。

- **(myghost)\\[delete.txt](../descript/install/delete.txt/index.md)**：文件删除设置文件。

  详情请参阅[链接目标](../descript/install/delete.txt/index.md)。

  可省略。

- **(myghost)\\[developer_options.txt](../descript/install/developer_options.txt/index.md)**：仅限 SSP 使用。用于设置 NAR 和更新文件创建功能的文件。

  详情请参阅[链接目标](../descript/install/developer_options.txt/index.md)。

  可省略。

- **(myghost)\\readme.txt または readme.md**：整个 ghost 的 readme。

  通常会注明发布者、发布来源等信息。

  在第 1 行写入 charset,UTF-8，或包含 BOM，即可使用 Shift JIS 以外的编码。

  安装时会打开，也可以通过 owner draw 菜单等打开。

  可以省略，但建议提供。

  可以使用 readme.md 代替 readme.txt，此时会解析 Markdown 格式，并以带有文字大小、表格等装饰的形式显示。<br />
  也可以解析图像嵌入 `\![画像説明]`(画像パス)，但只有在图像路径为相对路径、文件实际存在于 ghost 中，并且图像为 PNG 或 JPEG 时才能使用。

- **(myghost)\\terms.txt または terms.md**：显示使用条款。安装 NAR/ZIP 文件前，会弹出显示其内容的对话框。

  由于会中断安装并显示对话框，因此只在确实需要时才添加。

  与 readme 一样，在第 1 行写入 charset,UTF-8，或包含 BOM，即可使用 Shift JIS 以外的编码。

  可以省略，而且*如果不需要，建议省略*。

  terms.md 也可以在与 readme.md 相同的条件下使用。

- **(myghost)\\thumbnail.png**：在菜单树中选择 ghost 时显示的缩略图。

  可使用的图像格式为 PNG 或 JPG。

  将 PNG 重命名为 PNR 后，图像左上角 1 个点（坐标 0,0）的同色区域会变为透明。

  可以省略。

- **(myballoon)\\**：各 balloon 主目录（根文件夹）。

  文件夹名称建议使用英数字。

balloon 文件夹内文件结构的详细信息，请参阅「[balloon](balloon.md)」页面。
