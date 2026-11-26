# icon.interval,播放间隔

**カテゴリ:** descript.txt

[icon](icon.md)指定的动画图像（ANI、GIF、APNG、WebP）的播放时机。
可指定的值与[\![set,tasktrayicon]](../../../list/sakura-script/event/bang-set-tasktrayicon-.ico-duration-eq-runcount-eq.md)的 --interval 相同（always、runonce、runcount,N、never、rarely、sometimes、random,N、periodic,N）。在 descript.txt 中可以直接写成 `icon.interval,random,5`。

未指定时，遵循文件中的循环次数。播放结束后停在最后一帧。
不用于通过标签（`\![set,tasktrayicon]`）指定的图标（仅使用标签的 --interval）。

**既定値:** 无值（遵循文件中的循环次数）

**対応:** SSP 2.9.40
