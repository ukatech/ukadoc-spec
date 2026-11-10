# `\![set,balloonmarker,标记显示文本]`

**カテゴリ:** 气球、文本命令

显示接收 SSTP 时显示的标记文本。<br />
显示位置为当前 scope 所属的气球。<br />
显示文本可以省略。要清除时，请省略参数或将参数留空。

此设置会一直有效，直到 ghost 结束，或启动 SSTP 接收等原本会使用此区域的功能。

清除的含义是“取消通过此标签指定的文本”，而不是隐藏标记本身。在播放通过 SSTP 接收的脚本时清除标记，将恢复为默认的发送方显示（from 发送方）。<br />
此外，如果 SSTP 或 SHIORI 的 Marker 头指定了标记文本，则优先使用该文本，不会显示此标签指定的内容。<br />
如果要在输出为图像时排除标记，请对[`\![execute,dumpballoon]`](../misc/bang-execute-dumpballoon-ID-prefix-ID.md)使用--hide=balloonmarker。

**対応:** SSP 2.6.67
