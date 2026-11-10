# Owner draw菜单

用于owner draw菜单（右键菜单）的图像文件。

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
　　　　　　+-surfaces**.txt
　　　　　　+-alias.txt
　　　　　　+-thumbnail.png
　　　　　　+-makoto.dll
　　　　　　+-surfacetable.txt
　　　　　　+-menu_background.png
　　　　　　+-menu_foreground.png
　　　　　　+-menu_sidebar.png
```

实际上，文件不一定要放在上述位置，也可以放在文件夹内等位置。

通过SHIORI Resource设置owner draw菜单时，将其放在ghost/master一侧会更方便（因为要以ghost/master为基准指定相对路径）。

- **menu_background.png**: owner draw菜单的背景图像。

  菜单区域的大小取决于菜单本身，而不是图像。

  可以省略（此时显示标准菜单）。

- **menu_foreground.png**: owner draw菜单树中光标选中部分的图像。

  可以省略（此时显示标准菜单）。

- **menu_sidebar.png**: 可添加到owner draw菜单树左侧的图像。

  只有宽度取决于图像的宽度。

  可以省略。

所有图像和文字颜色等设置，均通过shell的[descript.txt](../descript/shell/index.md)或[SHIORI Resource](../list/shiori-resource/index.md)进行。

通过SHIORI Resource进行设置时，可以用于让具有角色轮换或模式切换等功能的ghost根据状态更改菜单显示。

如果同时在shell侧的descript.txt和SHIORI Resource中进行设置，则SHIORI Resource的设置优先。

另外，各图像的文件名不一定要与上例相同（可以任意命名）。

详细信息也请参阅[owner draw菜单的设置](../dev/ownerdraw.md)页面。

菜单图像超出边界的部分会以边缘颜色填充为纯色。

如果未指定，则显示普通弹出菜单。
