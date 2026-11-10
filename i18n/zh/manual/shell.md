# Shell

shell 文件夹中的文件如下。

```filetree
+-(myghost)
　　+-shell
　　　　+-master
　　　　　　+-descript.txt
　　　　　　+-readme.txt
　　　　　　+-surface*.png
　　　　　　+-surface*.pna
　　　　　　+-(element).png
　　　　　　+-(element).pna
　　　　　　+-surfaces.txt
　　　　　　+-surfaces**.txt （SSPのみ）
　　　　　　+-alias.txt（旧仕様）
　　　　　　+-thumbnail.png
　　　　　　+-makoto.dll
　　　　　　+-surfacetable.txt (SSPのみ)
　　　　　　+-menu_background.png
　　　　　　+-menu_foreground.png
　　　　　　+-menu_sidebar.png
```

※关于 menu_background.png、menu_foreground.png、menu_sidebar.png，请参阅「[所有者绘制菜单](owner-draw-menu.md)」页面。

- **[descript.txt](../descript/shell/index.md)**: 用于识别 shell 并进行基本设置的文件。

  关于文本中的记载内容，请参阅[链接目标](../descript/shell/index.md)。

- **readme.txt**: 用于记录 shell 作者及其发布来源等信息。

  此文件可以省略，但准备好后，可在安装时或通过 baseware 的菜单等查看。

  尤其是 ghost 作者和 shell 作者不同时，建议尽量准备此文件。

- **surface\*.png**: surface 文件。

  显示在桌面上的图像。

  图像尺寸和色数没有限制。

  文件格式为 PNG[※](shell.md#シェル)。

  与图像左上角的1个像素（坐标0,0）颜色相同的区域会被视为透明色（抠图色），显示时呈透明状态。

  surface 编号有[一定程度的标准分配方式](../descript/shell-surfaces/surface-brace/caption_standarddef.md)，但基本上可以自由设定。

  不过，surface0 和 surface10 是必需的（SSP 中建议使用，但并非必需）。

  因此，即使是只有一个角色的 ghost，也需要准备 surface10.png 等图像，例如纯色填充的图像。

  如果 baseware 是 MATERIA（embryo、本家的伺か），surface 编号范围为0～8192。

  其他 baseware 没有限制。

  SSP 2.7.38及之后版本中，为 surface\*.png 指定动画GIF/APNG/WebP动画后，无需编写SERIKO定义也会播放动画。

- **surface\*.pna**: surface 的 alpha 通道定义文件。

  将灰度图像（黑色：透明←→不透明：白色）的 png 图像扩展名改为 pna。

  放置与 surface 编号相同的 pna 文件，即可使 surface 半透明。

  | ![](../assets/image/surface0_png1.jpg) | → | ![](../assets/image/surface0_pna.jpg) | → | ![](../assets/image/surface0_png2.jpg) |
  | --- | --- | --- | --- | --- |
  | surface0.png |  | surface0.pna |  | 桌面上的显示效果 |

  未完全透明的区域会产生命中判定。

  此外，在 Windows9x 或非常旧的显卡等不支持的环境中，pna 会被忽略。

  另外，在 SSP 中也可以通过[设置](../descript/shell/descript-txt/seriko.use_self_alpha.md)，使用 png 自身的 alpha 通道（透明度信息）。

- **(element).png**: 根据 [element](../descript/shell-surfaces/surface-brace/element-star.md) 规范，将任意名称的 PNG 图像[※](shell.md#シェル)作为部件合成，并作为一个 surface 使用。此文件用于提供这些部件图像。

  ※(element)部分可以替换为任意名称。可使用任意数量的图像，也可以不使用。

  SSP 2.7.38及之后版本中，在 surfaces.txt 的 element 定义中指定动画GIF/APNG/WebP动画后，无需编写SERIKO定义也会播放动画。

  详情也请参阅后文的「surfaces.txt」。

- **(element).pna**: 各 element 合成部件图像对应的 pna。

- **[surfaces.txt](../descript/shell-surfaces/index.md)**: 用于定义 surface 的 ID 分配、图层合成、动画、命中判定等内容的文件。

  关于定义内容，请参阅[surfaces.txt](../descript/shell/index.md)。

  关于动画和 dressup，请参阅动画。

- **[surfaces\*\*.txt](../descript/shell-surfaces/index.md)**: SSP 专用。

  \*\*可以使用任意字符串。

  2.01系列及之后版本开始支持 surfaces2.txt 这样的名称，能够使用任意字符串命名则是从2.2.57开始。

  功能与`surfaces.txt`相同。

  用于在保持兼容性的同时使用 SSP 专用功能。

  此文件可以省略。只追加所需部分也没有问题。

- **[alias.txt](../descript/shell-surfaces/surface-alias-brace/caption_aliastxt.md)**: 旧规范。用于记述 sakura(kero).alias 花括号的文本文件。

  目前其功能已整合到 surfaces.txt 中。

- **thumbnail.png**: 在菜单树中选择 shell 时显示的缩略图。

  可使用的图像格式为 png 或 jpg。

  将 png 重命名为 pnr 后，与图像左上角的1个像素（坐标0,0）颜色相同的部分会变为透明。

  此文件可以省略。

- **[makoto.dll](translator.md)**: 用于使用转译功能。

  与可在[ghost 一侧](ghost.md)准备的文件相同。详情请参阅[链接目标](translator.md)。

  此文件可以省略。

- **[surfacetable.txt](../descript/shell-surfacetable/index.md)**: SSP 专用。

  用于 SSP 开发用调色板的「surface 测试」功能，以及其他 shell 制作辅助工具中定义 surface 内容的文件。

  详情请参阅[链接目标](../descript/shell-surfacetable/index.md)。

  此文件可以省略。

!!! tip "提示"

    - **[※1](shell.md#シェル),[※2](shell.md#シェル)**: SSP 也可以使用加密PNG(DAP/DDP/DFP/DGP)、GIF（非动画）、JPEG、BMP，但*不推荐*。

      为了兼容过去的内容，仍可读取这些格式，但无法保证今后新增的功能或规范会支持 PNG 以外的格式。

      此外，目前所有 PNG 以外的格式都无法使用透明度规范（pna 以及[seriko.use_self_alpha](../descript/shell/descript-txt/seriko.use_self_alpha.md)）；JPEG 还容易因压缩导致颜色偏移，因此与透明色不兼容。
