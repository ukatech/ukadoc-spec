# 补充

## surface 的位置信息

- **top**: 固定显示在顶部。
- **bottom**: 固定显示在底部。
- **free**: 自由移动。
- **osuwari,选项,…**: \[SSP 2.9.33\] 跟随其他窗口或屏幕的矩形区域（坐下）。选项使用与[`\![set,alignmenttodesktop,osuwari,…]`](../../../list/sakura-script/surface/bang-set-alignmenttodesktop.note.md)相同的`--名称=值`，并以逗号分隔排列。例如：`sakura.seriko.alignmenttodesktop,osuwari,--target=active,--origin=tr,--x=-20,--y=-90,--xmove,--area=workarea,--side=bottom`

## balloon 的位置信息

- **none**: 自动调整；如果 shell 的 Y 坐标位于屏幕中央左侧，则显示在右侧；如果在右侧，则显示在左侧。
- **left**: 始终显示在左侧。
- **right**: 始终显示在右侧。

## 菜单图像的位置指定

指定格式为：对齐方向之一+重复（平铺）设置。<br />
例如：lefttop<br />
例如：leftbottom+repeat-x+repeat-y

- **lefttop**: \[background/foreground\]对齐左上角。
- **centertop**: \[background/foreground\]对齐上边缘中央。 \[SSP\]
- **righttop**: \[background/foreground\]对齐右上角。
- **leftbottom**: \[background/foreground\]对齐左下角。 \[SSP\]
- **centerbottom**: \[background/foreground\]对齐下边缘中央。 \[SSP\]
- **rightbottom**: \[background/foreground\]对齐右下角。 \[SSP\]

- **top**: \[sidebar\]对齐上边缘。
- **bottom**: \[sidebar\]对齐下边缘。

- **+repeat-x**: \[background/foreground\]沿水平方向重复（平铺）显示图像。 \[SSP 2.5.39\]
- **+repeat-y**: \[background/foreground/sidebar\]沿垂直方向重复（平铺）显示图像。 \[SSP 2.5.39\]

## 关于图标边框颜色的亮度调整

通过sakura(kero/char\*).icon.frame.color.(r/g/b)指定的颜色，不会原样用作回放记录（发言历史）窗口的边框颜色。<br />
显示时会根据窗口的UI配色（例如深色模式/浅色模式），进行提高或降低亮度的运算。<br />
因此，最好指定尽可能接近纯色、没有杂色的值。（例如：想要红色时，指定RGB＝255,0,0等）
