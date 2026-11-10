# `\![set,wallpaper,ファイル名,オプション]`

**カテゴリ:** Event command

Set the specified file as the wallpaper.<br />
The file name can be an absolute or relative path. Relative paths are searched in this order: \[the executing ghost's folder\]/ghost/master, \[the executing ghost's folder\], and the SSP folder.<br />
If the path starts with !, it is treated as a relative path from the SSP folder. If it starts with \\ or /, it is treated as a relative path from the root of the drive containing SSP.<br />
If no file name is specified, or it is empty, the wallpaper setting is cleared (leaving a background with only a background color and no wallpaper).<br />
The options are as follows.

- **center**: Display centered (default if omitted)
- **tile**: Display tiled
- **stretch**: Enlarge to fill the monitor, ignoring the image's aspect ratio.
- **stretch-x**: Enlarge the image, preserving its aspect ratio, to fit the monitor width. Windows 7 or later only.
- **stretch-y**: Enlarge the image, preserving its aspect ratio, to fit the monitor height. Windows 7 or later only.
- **fit**: Scale the image, preserving its aspect ratio, so the whole image fits on the monitor. The background color appears in the margins.
- **fill**: Scale the image, preserving its aspect ratio, to cover the entire monitor. Any parts that extend beyond the monitor are not displayed.
- **span**: In a multi-monitor environment, enlarge the image to span all monitors. Windows 10 or later only.

\[2.8.93\] The following format can also be used. Arguments beginning with -- can be given in any order, and may be mixed with the file name and options specified above (arguments not beginning with -- are treated as a file name or option in the order they appear).

- **--file=ファイル名**: The file to use as the wallpaper. Same as the file name above.
- **--position=配置**: Image placement. Specify one of the option values above. Defaults to center if omitted.
- **--color=色指定**: Background color (used for image margins, or as the solid background color when no image is specified). Of the [methods for specifying text colors](../choice-marker/note-1.md#形状指定の方法), R,G,B, R%,G%,B%, hexadecimal color codes, and predefined keywords can be used.<br />
  For formats containing commas, such as R,G,B, enclose the entire argument in double quotes, as in "--color=255,128,0".<br />
  If a value that cannot be interpreted as a color is specified, this tag does nothing.

\[2.8.93\] The behavior is as follows, depending on whether a file name and --color are specified.

- **File name only**: Set the image as the wallpaper. The background color is not changed.
- **File name and --color**: Set the image as the wallpaper and change the background color.
- **--color only**: Set a solid background in the specified color, without an image.
- **Neither**: Clear the wallpaper setting (remove the wallpaper, leaving only the background color. The background color is not changed).

\[2.8.93\] When running in window mode, this changes the background of the window-mode window displaying the ghost, rather than changing the OS wallpaper (if all ghosts share one window, the background of all ghosts changes).<br />
The background setting is treated as "Background - Image" and is retained after SSP exits.<br />
Only span is treated the same as fill for placement. If --color is omitted, the background color is set to the image's dominant color.<br />
If neither a file name nor --color is specified, the background is restored to "Background - Desktop" (the setting that reproduces the OS wallpaper).<br />
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
