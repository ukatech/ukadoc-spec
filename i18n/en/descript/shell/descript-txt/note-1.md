# Notes

## Surface positioning

- **top**: Display attached to the top.
- **bottom**: Display attached to the bottom.
- **free**: Free movement.
- **osuwari,Options,…**: \[SSP 2.9.33\] Follows the rectangle of another window or the screen (sitting). Specify the options as comma-separated `--name=value` entries, as with [`\![set,alignmenttodesktop,osuwari,…]`](../../../list/sakura-script/surface/bang-set-alignmenttodesktop.note.md). Example: `sakura.seriko.alignmenttodesktop,osuwari,--target=active,--origin=tr,--x=-20,--y=-90,--xmove,--area=workarea,--side=bottom`

## Balloon positioning

- **none**: Automatic adjustment; displayed on the right if the shell's Y coordinate is left of the screen center, and on the left if it is right of the center.
- **left**: Always displayed on the left.
- **right**: Always displayed on the right.

## Menu image positioning

Specify in the form of one of the alignment directions + repeat (tiling) options.<br />
Example: lefttop<br />
Example: leftbottom+repeat-x+repeat-y

- **lefttop**: Align to the upper-left corner of \[background/foreground\].
- **centertop**: Align to the top center of \[background/foreground\]. \[SSP\]
- **righttop**: Align to the upper-right corner of \[background/foreground\].
- **leftbottom**: Align to the lower-left corner of \[background/foreground\]. \[SSP\]
- **centerbottom**: Align to the bottom center of \[background/foreground\]. \[SSP\]
- **rightbottom**: Align to the lower-right corner of \[background/foreground\]. \[SSP\]

- **top**: Align to the top of \[sidebar\].
- **bottom**: Align to the bottom of \[sidebar\].

- **+repeat-x**: Display the image repeated (tiled) horizontally for \[background/foreground\]. \[SSP 2.5.39\]
- **+repeat-y**: Display the image repeated (tiled) vertically for \[background/foreground/sidebar\]. \[SSP 2.5.39\]

## Adjusting icon frame color brightness

The color specified by sakura(kero/char\*).icon.frame.color.(r/g/b) is not used as-is for the frame color of the backlog (dialog history) window.<br />
It is displayed after applying calculations that increase or decrease its brightness to match the window's UI color scheme, such as dark or light mode.<br />
Therefore, it is best to specify a value as close as possible to a pure, unmixed primary color. (Example: to make it red, use RGB＝255,0,0)
