# `\![set,wallpaper,ファイル名,オプション]`

**カテゴリ:** Event command

Set the specified file as the wallpaper.<br />
In addition to absolute paths, relative paths can also be used as the file name. Relative paths are searched in this order: \[the folder of the ghost that executed the command\]/ghost/master, \[the folder of the ghost that executed the command\], and the SSP folder.<br />
If the path starts with !, it is treated as a relative path from the SSP folder. If it starts with \\ or /, it is treated as a relative path from the root of the drive containing SSP.<br />
If no file name is specified or it is empty, the wallpaper setting is cleared (leaving only the background color, with no wallpaper).<br />
The available options are as follows.

- **center**: Display centered (default if omitted)
- **tile**: Display tiled.
- **stretch**: Stretch to fill the monitor, ignoring the image's aspect ratio.
- **stretch-x**: Scale the image, preserving its aspect ratio, to fit the width of the monitor. Windows 7 and later only.
- **stretch-y**: Scale the image, preserving its aspect ratio, to fit the height of the monitor. Windows 7 and later only.
- **fit**: Scale the image, preserving its aspect ratio, so the entire image fits on the monitor. The background color is shown in the margins.
- **fill**: Scale the image, preserving its aspect ratio, to cover the entire monitor. Parts that extend beyond the edges are not displayed.
- **span**: In a multi-monitor environment, scale the image to span all monitors. Windows 10 and later only.

\[2.8.93\] The following format can also be used. Arguments beginning with -- can appear in any order and can be mixed with the file name and options specified above (arguments not beginning with -- are treated as a file name or option, in the order they appear).

- **--file=ファイル名**: The file to use as the wallpaper. Same as the file name above.
- **--position=配置**: Image placement. Specify one of the option values above. Defaults to center if omitted.
- **--color=色指定**: Background color (used for image margins or as the solid background color when no image is specified). The R,G,B, R%,G%,B%, hexadecimal color code, and predefined keyword formats described in [How to specify text colors](../choice-marker/note-1.md#形状指定の方法) can be used.<br />
  For formats containing commas, such as R,G,B, enclose the entire argument in double quotes, as in "--color=255,128,0".<br />
  If the specified value cannot be interpreted as a color, this tag does nothing.

\[2.8.93\] The behavior depends on whether a file name and --color are specified, as follows.

- **ファイル名のみ**: Set the image as the wallpaper. The background color is not changed.
- **ファイル名と--color**: Set the image as the wallpaper and change the background color.
- **--colorのみ**: Set a solid background of the specified color, with no image.
- **どちらもなし**: Clear the wallpaper setting (remove the wallpaper, leaving only the background color. The background color is not changed).

\[2.8.93\] While running in window mode, this changes the background of the window-mode window displaying the ghost, without changing the OS wallpaper (if all ghosts share one window, the background of all ghosts changes).<br />
The background setting is treated as “Background - Image” and is retained after SSP exits.<br />
For placement, span is treated the same as fill. If --color is omitted, the background color is set to the image's dominant color.<br />
If neither a file name nor --color is specified, the background is restored to “Background - Desktop” (the setting that reproduces the OS wallpaper).<br />
Changing the wallpaper by dragging and dropping an image file likewise changes the window-mode background.

**対応:** SSP / Ninix

## 記述例

```sakurascript
Emily/Phase4.5のサムネイルを壁紙にする。\![set,wallpaper,ghost/emily4/thumbnail.png]
```

```sakurascript
画像全体が収まるように表示し、余白を紺色にする。\![set,wallpaper,--file=ghost/emily4/thumbnail.png,--position=fit,--color=navy]
```

```sakurascript
画像なしの単色背景にする。\![set,wallpaper,"--color=32,64,96"]
```
