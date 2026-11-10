# `\![set,wallpaper,ファイル名,オプション]`

**カテゴリ:** Event command

Set the specified file as the wallpaper.<br />
The file name can be an absolute or relative path. Relative paths are searched in this order: \[executing ghost's folder\]/ghost/master, \[executing ghost's folder\], then the SSP folder.<br />
If the path starts with !, it is treated as a relative path from the SSP folder; if it starts with \\ or /, it is treated as a relative path from the root of the drive containing SSP.<br />
If no file name is specified or it is empty, the wallpaper setting is cleared (leaving a background color without a wallpaper).<br />
The options are as follows.

- **center**: Display in the center (default if omitted)
- **tile**: Display tiled.
- **stretch**: Enlarge to fill the monitor, ignoring the image's aspect ratio.
- **stretch-x**: Enlarge the image while maintaining its aspect ratio, fitting its width to the full width of the monitor. Windows 7 and later only.
- **stretch-y**: Enlarge the image while maintaining its aspect ratio, fitting its height to the full height of the monitor. Windows 7 and later only.
- **fit**: Scale the image while maintaining its aspect ratio so that the entire image fits on the monitor. The background color is shown in the empty areas.
- **fill**: Scale the image while maintaining its aspect ratio so that it covers the entire monitor. Parts that extend beyond the monitor are not displayed.
- **span**: In a multi-monitor environment, enlarge the image so that it spans all monitors. Windows 10 and later only.

\[2.8.93\] The following format can also be used. Arguments beginning with -- can be specified in any order and mixed with the file name and options above (arguments not beginning with -- are treated as the file name and options in the order they appear).

- **--file=ファイル名**: File to use as the wallpaper. Same as the file name described above.
- **--position=配置**: Image position. Specify one of the same values as the options above. Defaults to center if omitted.
- **--color=色指定**: Background color (used for empty areas around the image or as a solid background when no image is specified). Of the [methods for specifying text color](../choice-marker/note-1.md#形状指定の方法), R,G,B, R%,G%,B%, hexadecimal color codes, and predefined keywords can be used.<br />
  For formats containing commas, such as R,G,B, enclose the entire argument in double quotation marks, as in "--color=255,128,0".<br />
  If a value that cannot be interpreted as a color is specified, this tag does nothing.

\[2.8.93\] Behavior depends on whether a file name and --color are specified, as follows.

- **ファイル名のみ**: Set the image as the wallpaper. The background color is not changed.
- **ファイル名と--color**: Set the image as the wallpaper and change the background color.
- **--colorのみ**: Set a solid background of the specified color, without an image.
- **どちらもなし**: Clear the wallpaper setting (remove the wallpaper, leaving only the background color. The background color is not changed).

\[2.8.93\] While running in window mode, this changes the background of the window displaying the ghost in window mode instead of changing the OS wallpaper (if all ghosts share one window, the backgrounds of all ghosts change).<br />
The background setting is treated as "Background - Image" and persists after SSP exits.<br />
The span position is treated the same as fill. If --color is omitted, the background color is set to the image's dominant color.<br />
If neither a file name nor --color is specified, the background is restored to "Background - Desktop" (a setting that reproduces the OS wallpaper).<br />
Changing the wallpaper by dragging and dropping an image file also changes the window mode background in the same way.

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
