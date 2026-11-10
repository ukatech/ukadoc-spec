# `\![execute,dumpballoon,ディレクトリ,スコープID,prefix,イベントID]`

**カテゴリ:** Uncategorized command

Outputs the current drawing contents of the balloon for the specified scope as an image in the specified directory.<br />
Unlike a surface, it cannot be redrawn with a specified state; the contents currently drawn in the balloon are output as-is. The image is output at its original size, before applying enlargement, reduction, or translucency (including fading).<br />
The contents are output if they remain drawn, even when the balloon is hidden.<br />
The output filename is prefix+scope ID+.png (for example: balloon0.png).<br />
Scope ID: Specify the same ID used with the `\s` tag.<br />
prefix: (Optional) The string to prepend to the output filename. If omitted, balloon is used.<br />
Event ID: (Optional) Triggers the specified event when output is complete. Reference0 contains the number of files successfully output (0 or 1).<br />
The restrictions on the output destination are the same as for `\![execute,dumpsurface]`. If the destination is outside the permitted area, nothing is output and an error is recorded in the log.

\[2.9.08\] The following format can also be used. Arguments beginning with -- can be specified in any order and can be mixed with the arguments described above (arguments not beginning with -- are treated in order as directory, scope ID, prefix, and event ID).<br />
Arguments other than the directory are optional; if the scope ID is omitted, it defaults to 0.

- **--dir=ディレクトリ**: Output directory.
- **--scope=スコープID**: Scope ID.
- **--prefix=prefix**: String to prepend to the output filename.
- **--event=イベントID**: Event ID. Same as --async=.
- **--hide=項目**: Outputs a redraw with the specified items hidden. This does not affect the displayed balloon. To specify multiple items, separate them with commas as in "--hide=balloonmarker,balloonnum" and enclose the entire argument in double quotes.<br />
  balloonmarker: SSTP marker (the display of `\![set,balloonmarker]` or the sender display for scripts received via SSTP)<br />
  balloonnum: The display of `\![set,balloonnum]`<br />
  When this option is specified, the output is not the contents currently drawn, but contents redrawn from the state at that time (redrawing also occurs while `\![lock,balloonrepaint]` is in effect).

**対応:** SSP 2.9.02

## 記述例

```sakurascript
SSTPマーカーとballoonnumを除いて、\0のバルーンをdumpフォルダに出力する。\![execute,dumpballoon,--dir=dump,--scope=0,"--hide=balloonmarker,balloonnum"]
```
