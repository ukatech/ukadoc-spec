# `\![execute,dumpsurface,ディレクトリ,スコープID,サーフェスリスト,prefix,イベントID,ゼロ位置切り出し,アニメーションID]`

**カテゴリ:** Uncategorized command

Outputs the composited surface images to the specified directory.<br />
If no event ID is specified, script execution stops until processing is complete.<br />
Scope ID: Specify the same ID as the one specified in the `\s` tag. This setting changes processing that depends on the scope, such as dressup state.<br />
Surface list: Use the same format as [specifying surface IDs](../../../descript/shell-surfaces/surface-brace/caption_surfacebraceid.md), or specify one of the following.<br />
\_\_system_surface_all\_\_ : Outputs all surfaces enabled for the shell<br />
\_\_system_surface_defined\_\_ : Outputs all surfaces defined in surfaces.txt only<br />
Note: To specify commas inside Sakura Script square-bracket parameters, enclose them in " ".<br />
prefix: (Optional) The string to prepend to the output filenames. Defaults to surface.<br />
Event ID: (Optional) When specified, output continues while Sakura Script execution proceeds, and the specified event is triggered when output is complete. Reference0 contains the number of files successfully output.<br />
Zero-position cropping: If 1 is specified, always dump from 0,0 regardless of the animation definition, and ignore negative coordinates.<br />
Animation ID: (Optional) When specified, after outputting each surface's normal image (prefix+surface number.png), play the animation as with `\i[ID]` and output an image for each pattern as it advances, using a zero-based, 4-digit sequential number starting at prefix+surface number\_0000.png. Only one ID can be specified. For details, see the startup option --dump-animation. Reference0 for the event contains the number of files, including the sequential images.\[2.9.05\]<br />
For security reasons, the output destination is restricted to locations under folders managed by SSP (such as the ghost and balloon folders and locations specified by the "Folders" setting).<br />
Also, since this restriction may be strengthened as needed, it is safest to limit the destination to a location under the folder containing the ghost's own data.<br />
If the output destination is outside the permitted area, nothing is output and an error is recorded in the log.

\[2.9.08\] The following format can also be used. Arguments starting with -- can appear in any order and can be mixed with the arguments above (arguments not starting with -- are interpreted in order of appearance as directory, scope ID, surface list, prefix, event ID, zero-position cropping, and animation ID).<br />
Arguments other than the directory can be omitted; if the scope ID is omitted, it defaults to 0.

- **--dir=ディレクトリ**: Output destination directory.
- **--scope=スコープID**: Scope ID.
- **--surface=サーフェスリスト**: Surface list. If it contains commas, enclose the entire argument in double quotes, as in "--surface=0,10".
- **--prefix=prefix**: String to prepend to the output filenames.
- **--event=イベントID**: Event ID. The same applies to --async=.
- **--fromzero=真偽値**: Zero-position cropping.
- **--animation=アニメーションID**: Animation ID.

**対応:** SSP \[2.5.98\]

## 記述例

```sakurascript
\0のサーフェス0～9をdumpフォルダに出力する。\![execute,dumpsurface,--dir=dump,--scope=0,"--surface=0-9"]
```
