# `\![execute,dumpsurface,ディレクトリ,スコープID,サーフェスリスト,prefix,イベントID,ゼロ位置切り出し,アニメーションID]`

**カテゴリ:** Uncategorized command

Output the composited surface images to the specified directory.<br />
If no event ID is specified, script execution stops until processing is complete.<br />
Scope ID: Specify the same ID as the one used for the `\s` tag. This setting changes scope-dependent processing, such as the dressup state.<br />
Surface list: Use the same format as [surface ID specification](../../../descript/shell-surfaces/surface-brace/caption_surfacebraceid.md), or specify one of the following.<br />
\_\_system_surface_all\_\_ : Output all surfaces available to the shell<br />
\_\_system_surface_defined\_\_ : Output all surfaces defined in surfaces.txt only<br />
Note: To specify commas inside Sakura Script bracket parameters, enclose them in " ".<br />
prefix: (Optional) The string to prepend to the output file names. Defaults to surface.<br />
Event ID: (Optional) If specified, output continues while the rest of the Sakura Script runs, and the specified event is raised when output is complete. Reference0 contains the number of files successfully output.<br />
Zero-origin crop: If 1 is specified, always dump from 0,0 regardless of the animation definition, ignoring parts with negative coordinates.<br />
Animation ID: (Optional) If specified, after the normal image for each surface (prefix+surface number.png), play the animation in the same way as `\i[ID]`, and output an image for each pattern as it advances, using sequential, zero-based, four-digit numbers starting from prefix+surface number\_0000.png. Only one ID can be specified. For details, see the startup option --dump-animation. Reference0 for the event contains the number of files, including the sequential images.\[2.9.05\]<br />
For security reasons, output is restricted to locations under folders managed by SSP (such as the ghost and balloon folders, specified in the "Folders" settings).<br />
Since this restriction may be strengthened as needed, it is safest to limit output to locations under the folder containing the ghost's own data.<br />
If the output location is outside the permitted range, nothing is output and an error is logged.

\[2.9.08\] The following format can also be used. Arguments beginning with -- can be in any order and may be mixed with the specifications above. (Arguments not beginning with -- are treated in order as directory, scope ID, surface list, prefix, event ID, zero-origin crop, and animation ID.)<br />
All arguments except the directory are optional. If the scope ID is omitted, it defaults to 0.

- **--dir=ディレクトリ**: Output directory.
- **--scope=スコープID**: Scope ID.
- **--surface=サーフェスリスト**: Surface list. If it contains commas, enclose the entire argument in double quotes, as in "--surface=0,10".
- **--prefix=prefix**: String to prepend to the output file names.
- **--event=イベントID**: Event ID. The same as --async=.
- **--fromzero=真偽値**: Zero-origin crop.
- **--animation=アニメーションID**: Animation ID.

**対応:** SSP \[2.5.98\]

## 記述例

```sakurascript
\0のサーフェス0～9をdumpフォルダに出力する。\![execute,dumpsurface,--dir=dump,--scope=0,"--surface=0-9"]
```
