# 補充

## surface 位置資訊

- **top**: 貼齊上方顯示。
- **bottom**: 貼齊下方顯示。
- **free**: 自由移動。
- **osuwari,選項,…**: \[SSP 2.9.33\] 追蹤其他視窗或螢幕的矩形區域（坐下）。選項與[`\![set,alignmenttodesktop,osuwari,…]`](../../../list/sakura-script/surface/bang-set-alignmenttodesktop.note.md)相同，以逗號分隔排列`--名稱=值`。例：`sakura.seriko.alignmenttodesktop,osuwari,--target=active,--origin=tr,--x=-20,--y=-90,--xmove,--area=workarea,--side=bottom`

## balloon 位置資訊

- **none**: 自動調整；若 shell 的 Y 座標位於螢幕中央左側，則顯示於右側，若位於右側，則顯示於左側。
- **left**: 一律顯示於左側。
- **right**: 一律顯示於右側。

## 選單圖片的位置指定

以靠齊方向之一，加上重複（平鋪）指定的形式指定。<br />
例：lefttop<br />
例：leftbottom+repeat-x+repeat-y

- **lefttop**: \[background/foreground\]靠齊左上角。
- **centertop**: \[background/foreground\]靠齊上緣中央。 \[SSP\]
- **righttop**: \[background/foreground\]靠齊右上角。
- **leftbottom**: \[background/foreground\]靠齊左下角。 \[SSP\]
- **centerbottom**: \[background/foreground\]靠齊下緣中央。 \[SSP\]
- **rightbottom**: \[background/foreground\]靠齊右下角。 \[SSP\]

- **top**: \[sidebar\]靠齊上緣。
- **bottom**: \[sidebar\]靠齊下緣。

- **+repeat-x**: \[background/foreground\]沿水平方向重複（平鋪）顯示圖片。 \[SSP 2.5.39\]
- **+repeat-y**: \[background/foreground/sidebar\]沿垂直方向重複（平鋪）顯示圖片。 \[SSP 2.5.39\]

## 圖示框線色的亮度調整

sakura(kero/char\*).icon.frame.color.(r/g/b)指定的顏色不會直接用作對話記錄（發言歷史）視窗的框線色。<br />
顯示前會根據視窗 UI 配色（例如深色模式／淺色模式）進行運算，提高或降低亮度。<br />
因此，建議盡量指定接近純色的值。（例：若要設為紅色，RGB＝255,0,0）
