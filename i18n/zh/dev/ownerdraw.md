# Owner draw 菜单的设置

说明如何设置 owner draw 菜单（右键菜单）的显示。

也请一并参考文件结构中的「[Owner draw 菜单](../manual/owner-draw-menu.md)」。

设置可以记载在 shell 的`descript.txt`中，也可以作为对用于获取资源的若干 SHIORI Event 的响应进行设置。

## 目次

1. [在 shell 的descript.txt中设置](ownerdraw.md#シェルのdescripttxtで設定する)
2. [通过 SHIORI Event 设置](ownerdraw.md#shiori-eventで設定する)

## 在 shell 的descript.txt中设置

可以在 shell 的`descript.txt`中设置通常状态和选中状态的背景、用作侧边栏的三张图像，以及文字颜色。

只有 SSP 还可以指定文字大小和字体。

此外，换装菜单项目的排列等也在 shell 的`descript.txt`中设置，相关内容请参阅「[换装设置](bind.md)」页面。

请注意，如果同一项目也通过 SHIORI Event 进行了设置，则优先采用 SHIORI Event 的设置。

以下是通过`descript.txt`进行设置的示例。

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
menu.disable.font.color.120
menu.disable.font.color.120
menu.disable.font.color.120
```

各行的详细说明见「[Shell 设置](../descript/shell/descript-txt/menu.font.name.md)」，下面先作大致说明。

```
menu.background.bitmap.filename,background.png
menu.foreground.bitmap.filename,foreground.png
menu.sidebar.bitmap.filename,sidebar.png
```

以上三行分别设置 owner draw 菜单使用的三种图像。

background 是通常状态下的菜单背景。

foreground 是选中项目的背景图像。稍难理解的是，只有 owner draw 菜单中光标当前所在的部分，才会用 foreground 图像对应位置的部分替换 background 图像。

sidebar 是附加在 owner draw 菜单左侧的图像。

[![owner draw 菜单使用的三张图像](../assets/image/ownerdraw_materials.png)](../assets/image/ownerdraw_materials.png)

[![owner draw 菜单的显示效果](../assets/image/ownerdraw_view.png)](../assets/image/ownerdraw_view.png)

*上方是使用的3张图像，下方是实际显示效果（示例：Emily/Phase4.5）*

```
menu.background.alignment,lefttop
menu.foreground.alignment,lefttop
menu.sidebar.alignment,bottom
```

以上三行分别设置三种图像的排列位置。

在上例中，background 和 foreground 图像以左上角为基准排列。如果菜单因文字或项目数量而大于背景图像，超出区域的右侧和下侧会分别延伸图像右端和左端的颜色。

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
menu.disable.font.color.120
menu.disable.font.color.120
menu.disable.font.color.120
```

以上是文字颜色的设置。

background 是通常状态下的菜单文字颜色，foreground 是光标停留在项目上时的文字颜色，separator 是菜单分隔符的颜色，disable 是非活动项目的文字颜色，例如没有换装的 shell 中的换装菜单，或不支持 network update 的 ghost 中的 network update 项目。

RGB 的各个颜色分量以0～255的数值指定。rgb全部为255时是白色，全部为0时是黑色。

## 通过 SHIORI Event 设置

除了与 shell 侧`descript.txt`相同的设置外，还可以设置各菜单项目的显示名称，以及收藏夹和门户链接列表的内容。

请注意，即使 shell 侧的`descript.txt`设置了同一项目，也会优先采用 SHIORI Event 的设置。

如何为获取菜单相关资源的 SHIORI Event 设置并返回值，需要参阅各 SHIORI 的说明。

例如，里々可以参考以下页面。

[里々wiki - 右键菜单](http://soliton.sub.jp/satori/index.php?%B1%A6%A5%AF%A5%EA%A5%C3%A5%AF%A5%E1%A5%CB%A5%E5%A1%BC)

有关其他 SHIORI Event，请参阅「[SHIORI Resource](../list/shiori-resource/ownerdraw-image/menu.sidebar.bitmap.filename.md)」页面。
