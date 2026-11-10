# `\![execute,dumpsurface,ディレクトリ,スコープID,サーフェスリスト,prefix,イベントID,ゼロ位置切り出し,アニメーションID]`

**カテゴリ:** 未分類コマンド

将合成后的 surface 图像输出到指定目录。<br />
未指定事件ID时，脚本执行会暂停，直到处理完成。<br />
スコープID : 指定与 `\s` 标签中相同的ID。该指定会改变换装状态等依赖于 scope 的处理。<br />
サーフェスリスト : 使用与[surface ID指定](../../../descript/shell-surfaces/surface-brace/caption_surfacebraceid.md)相同的格式，或指定以下内容。<br />
\_\_system_surface_all\_\_ : 输出所有作为 shell 有效的 surface<br />
\_\_system_surface_defined\_\_ : 仅输出 surfaces.txt 中定义的所有 surface<br />
参考：如果要在 Sakura Script 的方括号参数中指定逗号，建议用 " " 括起来。<br />
prefix : (可省略) 添加到输出文件名开头的字符串。省略时为 surface。<br />
イベントID : (可省略) 指定后，会在继续执行 Sakura Script 的同时继续输出，并在完成时触发指定事件。Reference0中会存储成功输出的文件数。<br />
ゼロ位置切り出し : 指定1时，无论动画定义如何，都会始终从0,0开始转储，并忽略负坐标部分。<br />
アニメーションID : (可省略) 指定后，会在每个 surface 的常规图像(prefix+サーフェス番号.png)之后，像 `\i[ID]` 一样播放该动画，并将每次图案切换时的图像从 prefix+サーフェス番号\_0000.png 开始，以从0起始的4位连续编号输出。只能指定一个ID。详情与启动选项 --dump-animation 相同。事件的Reference0中会包含连续编号图像在内的文件数。\[2.9.05\]<br />
出于安全考虑，输出位置限制在 SSP 管理的文件夹（ghost文件夹、balloon文件夹等由“文件夹”设置指定的位置）之下。<br />
此外，该限制可能会适时加强，因此最好将输出位置限制在存放 ghost 自身数据的文件夹之下。<br />
如果输出位置超出限制范围，则不会输出任何内容，并会记录到错误日志中。

\[2.9.08\] 也可以使用以下格式指定。以--开头的参数顺序不限，也可以与上述各参数的指定混用（不以--开头的参数则按出现顺序分别视为目录、スコープID、サーフェスリスト、prefix、イベントID、ゼロ位置切り出し、アニメーションID）。<br />
除目录外的参数均可省略；省略スコープID时为0。

- **--dir=ディレクトリ**: 输出目标目录。
- **--scope=スコープID**: scope ID。
- **--surface=サーフェスリスト**: surface 列表。包含逗号时，应将整个参数用双引号括起来，例如"--surface=0,10"。
- **--prefix=prefix**: 添加到输出文件名开头的字符串。
- **--event=イベントID**: 事件ID。--async=也相同。
- **--fromzero=真偽値**: 零位置裁切。
- **--animation=アニメーションID**: 动画ID。

**対応:** SSP \[2.5.98\]

## 記述例

```sakurascript
\0のサーフェス0～9をdumpフォルダに出力する。\![execute,dumpsurface,--dir=dump,--scope=0,"--surface=0-9"]
```
