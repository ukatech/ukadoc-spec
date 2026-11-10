# Notes

## Surface positioning

- **top**: Display attached to the top.
- **bottom**: Display attached to the bottom.
- **free**: Free movement.
- **osuwari,オプション,…**: \[SSP 2.9.33\] Tracks the rectangle of another window or the screen (sitting). Specify the options as comma-separated `--name=value` pairs, as with [`\![set,alignmenttodesktop,osuwari,…]`](../../../list/sakura-script/surface/bang-set-alignmenttodesktop.note.md). Example: `sakura.seriko.alignmenttodesktop,osuwari,--target=active,--origin=tr,--x=-20,--y=-90,--xmove,--area=workarea,--side=bottom`

## Balloon positioning

- **none**: Adjusts automatically; displays on the right if the shell's Y coordinate is left of the screen center, and on the left if it is right of center.
- **left**: Always displays on the left.
- **right**: Always displays on the right.

## Menu image positioning

Specify in the form of one of the alignment directions, optionally followed by repeat (tiling) options.<br />
Example: lefttop<br />
Example: leftbottom+repeat-x+repeat-y

- **lefttop**: Align to the top-left corner of the \[background/foreground\].
- **centertop**: Align to the top center of the \[background/foreground\]. \[SSP\]
- **righttop**: Align to the top-right corner of the \[background/foreground\].
- **leftbottom**: Align to the bottom-left corner of the \[background/foreground\]. \[SSP\]
- **centerbottom**: Align to the bottom center of the \[background/foreground\]. \[SSP\]
- **rightbottom**: Align to the bottom-right corner of the \[background/foreground\]. \[SSP\]

- **top**: Align to the top of the \[sidebar\].
- **bottom**: Align to the bottom of the \[sidebar\].

- **+repeat-x**: Display the image repeated (tiled) horizontally for the \[background/foreground\]. \[SSP 2.5.39\]
- **+repeat-y**: Display the image repeated (tiled) vertically for the \[background/foreground/sidebar\]. \[SSP 2.5.39\]

## Adjusting the brightness of icon frame colors

The colors specified by sakura(kero/char\*).icon.frame.color.(r/g/b) are not used as-is for the frame color of the backlog (speech history) window.<br />
They are displayed after applying calculations to increase or decrease brightness to match the window's UI color scheme, such as dark or light mode.<br />
Therefore, it is preferable to specify values as close as possible to pure, unmixed colors. (For example, to use red, specify RGB=255,0,0.)
