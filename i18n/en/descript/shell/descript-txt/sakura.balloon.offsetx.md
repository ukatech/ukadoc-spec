# sakura.balloon.offsetx,Coordinate

**カテゴリ:** descript.txt

X coordinate of the baseware-side balloon position.<br />
Appending one character indicating direction to offsetx / offsety lets you use different values depending on where the balloon is displayed (SSP only).

- **offsetx / offsety**: No direction specified. The default values used when the following entries are not specified.
- **offsetxl / offsetyl**: When displaying the balloon to the left of the shell.
- **offsetxr / offsetyr**: When displaying the balloon to the right of the shell.
- **offsetxc / offsetyc**: When displaying the balloon above or below the shell. Shared by both cases, which are centered.
- **offsetxb / offsetyb**: When displaying the balloon below the shell. Use these when you want different values for above and below.

The following values are used when an entry is not specified. The X and Y coordinates are determined independently.

- **When offsetxb is not specified**: Look for offsetxc, then offsetx.
- **When offsetxc / offsetxl / offsetxr are not specified**: Use offsetx.

Where the balloon is displayed is determined by the balloon's descript.txt [windowposition.x](../../balloon/descript-txt/windowposition.x.md), the shell's [sakura.balloon.alignment](sakura.balloon.alignment.md), and Sakura Script's [`\![set,balloonalign,ID]`](../../../list/sakura-script/balloon-text/bang-set-balloonalign-ID.md).

**Note the sign.**For the X coordinate, + always points toward the shell: to the right when displaying the balloon on the left, and to the **left** when displaying it on the right (+ points right when the balloon is above or below). For the Y coordinate, + always points down.<br />
However, the zero position (reference point) differs by direction. On the left and right, the top of the balloon aligns with the top of the shell image; above the shell, the bottom of the balloon touches the top of the shell image; below the shell, the top of the balloon touches the bottom of the shell image.

**既定値:** ghost's descript settings

**対応:** Materia / SSP / CROW
