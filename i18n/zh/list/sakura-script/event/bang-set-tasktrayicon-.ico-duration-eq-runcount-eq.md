# `\![set,tasktrayicon,ファイル名.ico,テキスト(,--duration=待機時間(,--runcount=繰り返し回数)(,--interval=再生間隔))]`

**カテゴリ:** 事件命令

将指定的图标文件应用于通知区域（任务托盘）的图标。<br />
文件名可使用相对于\[执行该命令的 ghost 文件夹\]或\[执行该命令的 ghost 文件夹\]/ghost/master 的路径。<br />
文本在鼠标悬停于图标上时显示，可以省略。默认为「SSP/Emily/Phase4.5」等，即 SSP/\[运行中的 ghost 名称\]。<br />
指定 --duration=等待时间(ms) 可使图标播放动画。此时，指定ファイル名.ico 后，会按照末尾数字的顺序加载ファイル名00.ico、ファイル名01.ico 等多个文件，并以指定的等待时间（毫秒）为间隔播放动画。 \[SSP 2.5.58～\]<br />
进一步指定 --runcount 可设置动画的重复次数。未指定时无限重复。 \[SSP 2.5.59～\]

## 指定动画图像

文件名除 .ico 外，还可指定动画图像（ANI、GIF、APNG、WebP）或静态图像（如 PNG）。无需准备连续编号的 .ico，只用一个图像文件即可播放动画。 \[SSP 2.9.40～\]

- 动画图像按照文件中各帧的等待时间和循环次数播放。无需指定 --duration。
- 指定 --duration=等待时间(ms) 后，所有帧的等待时间都会被该值覆盖（下限为50毫秒）。
- 帧图像会缩小至通知区域图标的大小后使用（显示缩放为100%时为16px见方，150%时为24px见方，200%时为32px见方。显示缩放改变时，会按新尺寸重新生成）。非正方形图像会保持比例并居中显示。
- .ico（包括连续编号的文件）仍与以往一样，仅在指定 --duration 时播放动画。
- 此功能仅 SSP 支持。其他 baseware 只能读取 .ico。

## 播放方式

可通过 --interval=播放间隔 指定动画播放的时机（仅 SSP 支持）。取值与 surfaces.txt 的[动画间隔](../../../descript/shell-surfaces/surface-brace/h-animationinterval/introduction_animationinterval.md)相同。 \[SSP 2.9.40～\]

| 播放间隔 | 行为 |
| --- | --- |
| always | 不停止，无限重复。忽略文件中的循环次数。 |
| runonce | 播放1次后停止。 |
| runcount,N | 播放N次后停止。与 --runcount=N 相同。 |
| never | 不播放。停留在第1帧。 |
| rarely | 每秒以四分之一的概率播放1次。 |
| sometimes | 每秒以二分之一的概率播放1次。 |
| random,N | 每秒以N分之一的概率播放1次。省略N时为2。 |
| periodic,N | 每次播放结束后等待N秒，再播放1次。省略N时为1。 |

- 所有方式在播放结束后都会停留在最后一帧（与 surfaces.txt 的动画相同）。random、periodic、rarely、sometimes 最初停留在第1帧，每次播放都从第1帧开始。如需在播放后恢复到第一帧的图像，请将最后一帧设为与第一帧相同的图像。
- 未指定 --interval 时，如果指定了 --runcount，则按其设置播放；否则按文件中的循环次数播放（ANI 为无限循环；GIF 如果没有 NETSCAPE 扩展，则播放1次后停止）。连续编号的 .ico 为无限循环。
- 同时指定 --interval 和 --runcount 时，--interval 优先。但对于 random、periodic、rarely、sometimes，--runcount 用作每次播放的重复次数（未指定时为1次）。
- 可以像 `--interval=random,5` 一样用逗号分隔（也可以写成 `--interval=random:5`）。
- 指定的 --duration、--runcount、--interval 在 ghost 最小化和恢复后仍然保留。要将图标恢复为默认值，请将文件名留空并执行 `\![set,tasktrayicon,]`（文本不会恢复）。要连同文本一起恢复，请使用下方的 `--reset`。

## 取消所有指定（--reset）

像 `\![set,tasktrayicon,--reset]` 一样，用 --reset 代替文件名，即可取消通过此标签指定的所有设置，恢复为 descript.txt 中的设置。 \[SSP 2.9.40～\]

- 文件名、文本、--duration、--runcount、--interval 都会被取消。
- 图标恢复为 descript.txt 中的 [icon](../../../descript/ghost/descript-txt/icon.md)（最小化时为 [icon.minimize](../../../descript/ghost/descript-txt/icon.minimize.md)），文本恢复为默认的「SSP/\[运行中的 ghost 名称\]」（最小化时为「SSP\[Minimize\]/\[运行中的 ghost 名称\]」）。
- --reset 后面的参数会被忽略。
- 将文件名留空的 `\![set,tasktrayicon,]` 只会恢复图标，通过此标签指定的文本会保留。

通过 descript.txt 的 [icon](../../../descript/ghost/descript-txt/icon.md) 和 [icon.minimize](../../../descript/ghost/descript-txt/icon.minimize.md) 指定的图标也可以同样播放动画（播放方式通过 [icon.interval](../../../descript/ghost/descript-txt/icon.interval.md) 和 [icon.minimize.interval](../../../descript/ghost/descript-txt/icon.minimize.interval.md) 指定）。

**対応:** SSP

## 記述例

```sakurascript
\![set,tasktrayicon,normal.ico,ゴースト/通常モード]アイコンを[実行したゴーストのフォルダ]/ghost/masterにあるnormal.icoにし、マウスオン時のメッセージを「ゴースト/通常モード」に変更する。
```

```sakurascript
\![set,tasktrayicon,alert.gif,通知あり,--interval=periodic,10]アイコンを alert.gif のアニメーションにし、再生が終わるたびに10秒待ってからもう一度再生する。
```

```sakurascript
\![set,tasktrayicon,--reset]このタグで指定したアイコンとテキストをすべて取り消して、descript.txtの指定に戻す。
```
