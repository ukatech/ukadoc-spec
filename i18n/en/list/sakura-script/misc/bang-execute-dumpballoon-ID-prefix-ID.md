# `\![execute,dumpballoon,ディレクトリ,スコープID,prefix,イベントID]`

**カテゴリ:** Uncategorized command

Output the current drawing contents of the balloon for the specified scope as an image in the specified directory.<br />
Unlike a surface, it cannot be redrawn by specifying a state; the contents drawn in the balloon at that point are output as-is. The image is output at its original size, before scaling or applying transparency (including fades).<br />
The image is output even if the balloon is hidden, as long as drawing contents remain.<br />
The output filename is prefix+scope ID+.png (e.g. : balloon0.png).<br />
scope ID : Specify the same ID used for the `\s` tag.<br />
prefix : (optional) The string to prepend to the output filename. If omitted, balloon is used.<br />
event ID : (optional) Raise the specified event when output completes. The number of files successfully output (0 or 1) is stored in Reference0.<br />
The output destination restrictions are the same as for `\![execute,dumpsurface]`. If the destination is outside the allowed range, nothing is output and an error is recorded in the log.

\[2.9.08\] The command can also be specified in the following format. Arguments beginning with -- can be in any order and may be mixed with the specifications using the arguments above (arguments not beginning with -- are treated, in order of appearance, as directory, scope ID, prefix, and event ID).<br />
All arguments except the directory can be omitted; if the scope ID is omitted, it defaults to 0.

- **--dir=ディレクトリ**: Output directory.
- **--scope=スコープID**: Scope ID.
- **--prefix=prefix**: String to prepend to the output filename.
- **--event=イベントID**: Event ID. The same applies to --async=.
- **--hide=項目**: Output a redraw that omits the specified items. This does not affect the displayed balloon. To specify multiple items, separate them with commas, as in "--hide=balloonmarker,balloonnum", and enclose the entire argument in double quotes.<br />
  balloonmarker : SSTP marker (the display of `\![set,balloonmarker]` and the sender display for scripts received via SSTP)<br />
  balloonnum : Display of `\![set,balloonnum]`<br />
  When this option is specified, the output is redrawn from the state at that point, rather than using the drawing contents at that point (it is also redrawn while `\![lock,balloonrepaint]` is active).

**対応:** SSP 2.9.02

## 記述例

```sakurascript
SSTPマーカーとballoonnumを除いて、\0のバルーンをdumpフォルダに出力する。\![execute,dumpballoon,--dir=dump,--scope=0,"--hide=balloonmarker,balloonnum"]
```
