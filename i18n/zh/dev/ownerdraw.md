# owner draw 菜单的设置

本文介绍如何设置 owner draw 菜单（右键菜单）的显示方式。

请同时参考文件结构中的「[owner draw 菜单](../manual/owner-draw-menu.md)」。

设置可写在 shell 的`descript.txt`中，也可通过响应为获取资源而发出的若干 SHIORI Event 来设置。

## 目次

1. [在 shell 的 descript.txt 中设置](ownerdraw.md#シェルのdescripttxtで設定する)
2. [通过 SHIORI Event 设置](ownerdraw.md#shiori-eventで設定する)

## 在 shell 的 descript.txt 中设置

shell 的`descript.txt`中可以设置用于普通背景、选中背景和侧边栏的三张图片，以及文字颜色。

仅 SSP 还支持指定文字大小和字体。

dressup 菜单的项目排列等也在 shell 的`descript.txt`中设置，详情请参阅「[dressup 设置](bind.md)」页面。

请注意，如果同一项目同时通过 SHIORI Event 设置，则 SHIORI Event 的设置优先。

在 SSP 中，也可以在 ghost 的`descript.txt`（`ghost/master/descript.txt`）中写入相同项目。如果 shell 的`descript.txt`中也有相同项目，则 shell 侧的设置优先。

以下是通过`descript.txt`设置的示例。

```
menu.background.bitmap.filename,background.png
menu.foreground.bitmap.filename,foreground.png
menu.sidebar.bitmap.filename,sidebar.png

menu.background.alignment,lefttop
menu.foreground.alignment,lefttop
menu.sidebar.alignment,bottom

menu.background.font.color.r,0
menu.background.font.color.g,0
menu.background.font.color.b,0
menu.foreground.font.color.r,0
menu.foreground.font.color.g,0
menu.foreground.font.color.b,255
menu.separator.color.r,0
menu.separator.color.g,0
menu.separator.color.b,0
menu.disable.font.color.r,120
menu.disable.font.color.g,120
menu.disable.font.color.b,120
```

各行的详细说明见「[Shell 设置](../descript/shell/descript-txt/menu.font.name.md)」，下面作简要说明。

```
menu.background.bitmap.filename,background.png
menu.foreground.bitmap.filename,foreground.png
menu.sidebar.bitmap.filename,sidebar.png
```

以上三行分别设置 owner draw 菜单使用的三种图片。

background 是菜单的普通背景。

foreground 是选中项目的背景图片。具体来说，owner draw 菜单中只有光标所在的部分，会将 background 图片替换为 foreground 图片对应位置的部分。

sidebar 是附在 owner draw 菜单左侧的图片。

[![owner draw 菜单使用的三张图片](../assets/image/ownerdraw_materials.png)](../assets/image/ownerdraw_materials.png)

[![owner draw 菜单的显示效果](../assets/image/ownerdraw_view.png)](../assets/image/ownerdraw_view.png)

*上方是使用的三张图片，下方是实际显示效果（例：Emily/Phase4.5）*

```
menu.background.alignment,lefttop
menu.foreground.alignment,lefttop
menu.sidebar.alignment,bottom
```

以上三行分别设置三种图片的排列方式。

在上述示例中，background 和 foreground 图片以左上角为起点排列。如果菜单因文字数量或项目数量而大于背景图片，超出区域的右侧和下侧将分别延伸图片右边缘和左边缘的颜色来显示。

```
menu.background.font.color.r,0
menu.background.font.color.g,0
menu.background.font.color.b,0
menu.foreground.font.color.r,0
menu.foreground.font.color.g,0
menu.foreground.font.color.b,255
menu.separator.color.r,0
menu.separator.color.g,0
menu.separator.color.b,0
menu.disable.font.color.r,120
menu.disable.font.color.g,120
menu.disable.font.color.b,120
```

以上是文字颜色的设置。

background 是菜单普通状态下的文字颜色，foreground 是光标位于项目上时的文字颜色，separator 是菜单分隔符的颜色，disable 是非活动项目的文字颜色，例如没有 dressup 的 shell 中的 dressup 菜单，或不支持 network update 的 ghost 中的 network update 项目。

RGB 颜色的各个分量使用 0～255 的数值指定。rgb 全部为 255 时是白色，全部为 0 时是黑色。

## 通过 SHIORI Event 设置

除了与 shell 侧`descript.txt`相同的设置外，还可以设置菜单各项目的显示名称以及收藏夹和门户链接集的内容。

即使 shell 侧`descript.txt`中设置了同一项目，SHIORI Event 的设置也会优先。

如何为获取菜单资源的 SHIORI Event 设置并返回值，需要参阅各 SHIORI 的说明。

例如，使用 Satori 时，可以参考以下页面。

[Satori wiki - 右键菜单](http://soliton.sub.jp/satori/index.php?%B1%A6%A5%AF%A5%EA%A5%C3%A5%AF%A5%E1%A5%CB%A5%E5%A1%BC)

有关其他 SHIORI Event，请参阅「[SHIORI Resource](../list/shiori-resource/ownerdraw-image/menu.sidebar.bitmap.filename.md)」页面。
