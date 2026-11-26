# `\![set,tasktrayicon,ファイル名.ico,テキスト(,--duration=待機時間(,--runcount=繰り返し回数)(,--interval=再生間隔))]`

**カテゴリ:** 事件命令

将指定的图标文件应用为通知区域（任务托盘）的图标。<br />
文件名可以使用相对于\[执行该命令的 ghost 的文件夹\]或\[执行该命令的 ghost 的文件夹\]/ghost/master 的路径。<br />
文本在鼠标悬停于图标上时显示，可以省略。默认为“SSP/Emily/Phase4.5”等，即 SSP/\[运行中的 ghost 名称\]。<br />
指定 --duration=等待时间(ms) 可以使图标播放动画。此时，若指定文件名.ico，则会按后缀数字顺序读取文件名00.ico、文件名01.ico…等多个文件，并按指定的等待时间（毫秒）播放动画。 \[SSP 2.5.58～\]<br />
进一步指定 --runcount 可以设置动画的重复次数。未指定时无限重复。 \[SSP 2.5.59～\]

## 指定动画图像

文件名除 .ico 外，还可以指定动画图像（ANI、GIF、APNG、WebP）或静态图像（PNG 等）。无需准备连续编号的 .ico 文件，只用一个图像文件即可播放动画。 \[SSP 2.9.40～\]

- 动画图像按照文件中各帧的等待时间和循环次数播放。无需指定 --duration。
- 指定 --duration=等待时间(ms) 时，用该值覆盖所有帧的等待时间（下限为50毫秒）。
- 帧图像缩小至通知区域图标的大小（16px见方）后使用。非正方形图像保持比例并居中放置。
- .ico（包括连续编号的文件）与以往一样，仅在指定 --duration 时播放动画。
- 此功能仅可在 SSP 中使用。其他 baseware 只能读取 .ico。

## 播放方式

通过 --interval=播放间隔 可以指定动画的播放时机（仅限 SSP）。可用值与 surfaces.txt 的[动画间隔](../../../descript/shell-surfaces/surface-brace/h-animationinterval/introduction_animationinterval.md)相同。 \[SSP 2.9.40～\]

| 播放间隔 | 动作 |
| --- | --- |
| always | 不停止地无限重复。忽略文件中的循环次数。 |
| runonce | 播放1次后停止。 |
| runcount,N | 播放N次后停止。与 --runcount=N 相同。 |
| never | 不播放。停在第1帧。 |
| rarely | 每秒以四分之一的概率播放1次。 |
| sometimes | 每秒以二分之一的概率播放1次。 |
| random,N | 每秒以N分之一的概率播放1次。省略N时为2。 |
| periodic,N | 播放结束后每隔N秒播放1次。省略N时为1。 |

- 所有模式在播放结束后都停在最后一帧（与 surfaces.txt 的动画相同）。random、periodic、rarely、sometimes 最初停在第1帧，每次播放都从第1帧开始。若希望播放后恢复到首帧图像，应将最后一帧设为与首帧相同的图像。
- 未指定 --interval 时，若指定了 --runcount 则遵循该值，否则遵循文件中的循环次数（ANI 为无限循环；GIF 若没有 NETSCAPE 扩展则播放1次后停止）。连续编号的 .ico 无限循环。
- 同时指定 --interval 和 --runcount 时，--interval 优先。但在 random、periodic、rarely、sometimes 中，--runcount 用作每次播放的重复次数（未指定时为1次）。
- 可以像 `--interval=random,5` 一样用逗号分隔（也可写成 `--interval=random:5`）。
- 指定的 --duration、--runcount、--interval 在 ghost 最小化和恢复后仍会保留。要将图标恢复为默认值，将文件名留空并执行 `\![set,tasktrayicon,]`。

descript.txt 的[icon](../../../descript/ghost/descript-txt/icon.md)和[icon.minimize](../../../descript/ghost/descript-txt/icon.minimize.md)指定的图标也可以同样播放动画（播放方式通过[icon.interval](../../../descript/ghost/descript-txt/icon.interval.md)和[icon.minimize.interval](../../../descript/ghost/descript-txt/icon.minimize.interval.md)指定）。

**対応:** SSP

## 記述例

```sakurascript
\![set,tasktrayicon,normal.ico,ゴースト/通常モード]アイコンを[実行したゴーストのフォルダ]/ghost/masterにあるnormal.icoにし、マウスオン時のメッセージを「ゴースト/通常モード」に変更する。
```

```sakurascript
\![set,tasktrayicon,alert.gif,通知あり,--interval=periodic,10]アイコンを alert.gif のアニメーションにし、再生が終わるたびに10秒待ってからもう一度再生する。
```
