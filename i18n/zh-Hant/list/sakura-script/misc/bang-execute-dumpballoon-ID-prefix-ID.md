# `\![execute,dumpballoon,ディレクトリ,スコープID,prefix,イベントID]`

**カテゴリ:** Uncategorized command

Export the current rendered contents of the balloon for the specified scope as an image to the specified directory.<br />
Unlike a surface, it cannot be redrawn by specifying a state; the contents drawn in the balloon at that time are exported as-is. The image is exported at its original size, before scaling or applying transparency (including fading).<br />
The contents are exported even if the balloon is hidden, as long as they remain rendered.<br />
The output filename is prefix+scope ID+.png (example: balloon0.png).<br />
Scope ID: Specify the same ID used for the `\s` tag.<br />
prefix: (Optional) The string to prepend to the output filename. If omitted, balloon is used.<br />
Event ID: (Optional) Trigger the specified event as soon as the export finishes. The number of files successfully exported (0 or 1) is set in Reference0.<br />
The output destination restrictions are the same as for `\![execute,dumpsurface]`. If the destination is outside the allowed range, nothing is exported and an error is recorded in the log.

\[2.9.08\] The following format can also be used. Arguments beginning with -- can be specified in any order and can be mixed with the arguments above (arguments not beginning with -- are treated, in order of appearance, as directory, scope ID, prefix, and event ID).<br />
Anything other than the directory can be omitted; if the scope ID is omitted, it defaults to 0.

- **--dir=ディレクトリ**: The output directory.
- **--scope=スコープID**: The scope ID.
- **--prefix=prefix**: The string to prepend to the output filename.
- **--event=イベントID**: The event ID. The same applies to --async=.
- **--hide=項目**: Export a redraw that omits the specified items. This does not affect the visible balloon. To specify multiple items, separate them with commas, as in "--hide=balloonmarker,balloonnum", and enclose the entire argument in double quotes.<br />
  balloonmarker: The SSTP marker (the display of `\![set,balloonmarker]` and the display of the sender of scripts received via SSTP)<br />
  balloonnum: The display of `\![set,balloonnum]`<br />
  When this option is specified, the exported image is redrawn from the state at that time, rather than using the contents currently rendered (it is redrawn even during `\![lock,balloonrepaint]`).

**対応:** SSP 2.9.02

## 記述例

```sakurascript
SSTPマーカーとballoonnumを除いて、\0のバルーンをdumpフォルダに出力する。\![execute,dumpballoon,--dir=dump,--scope=0,"--hide=balloonmarker,balloonnum"]
```
