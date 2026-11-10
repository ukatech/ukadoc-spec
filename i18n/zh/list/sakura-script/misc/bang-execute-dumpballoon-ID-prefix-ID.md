# `\![execute,dumpballoon,ディレクトリ,スコープID,prefix,イベントID]`

**カテゴリ:** 未分類命令

将指定 scope 的 balloon 当前绘制内容作为图像输出到指定目录。<br />
与 surface 不同，无法指定状态重新绘制；输出的是该时刻 balloon 上绘制的内容。输出图像为应用缩放及半透明（包括淡入淡出）之前的原始尺寸图像。<br />
即使 balloon 不可见，只要绘制内容仍然存在，就会输出。<br />
输出文件名为 prefix+scope ID+.png（例如：balloon0.png）。<br />
scope ID：指定与 `\s` 标签相同的 ID。<br />
prefix：（可省略）添加到输出文件名开头的字符串。省略时为 balloon。<br />
事件ID：（可省略）输出完成后触发指定事件。Reference0 中包含成功输出的文件数（0 或 1）。<br />
输出目标的限制与 `\![execute,dumpsurface]` 相同。超出限制范围时不会输出任何内容，并会记录到错误日志中。

\[2.9.08\] 也可以使用以下格式指定。以 -- 开头的参数不分顺序，且可与上述各参数的指定方式混用（不以 -- 开头的参数按出现顺序视为目录、scope ID、prefix、事件ID）。<br />
除目录外的参数均可省略；省略 scope ID 时为 0。

- **--dir=目录**：输出目标目录。
- **--scope=scope ID**：scope ID。
- **--prefix=prefix**：添加到输出文件名开头的字符串。
- **--event=事件ID**：事件ID。--async=也相同。
- **--hide=项目**：不绘制指定项目，并输出重新绘制后的图像。不会影响正在显示的 balloon。指定多个项目时，用逗号分隔，例如 "--hide=balloonmarker,balloonnum"，并将整个参数用双引号括起来。<br />
  balloonmarker：SSTP 标记（显示 `\![set,balloonmarker]` 的内容，以及通过 SSTP 接收的脚本的发送方信息）<br />
  balloonnum：显示 `\![set,balloonnum]` 的内容<br />
  指定此项时，输出的是根据该时刻的状态重新绘制的内容，而不是该时刻的绘制内容（即使处于 `\![lock,balloonrepaint]` 状态也会重新绘制）。

**対応:** SSP 2.9.02

## 記述例

```sakurascript
SSTPマーカーとballoonnumを除いて、\0のバルーンをdumpフォルダに出力する。\![execute,dumpballoon,--dir=dump,--scope=0,"--hide=balloonmarker,balloonnum"]
```
