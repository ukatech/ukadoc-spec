# sakura.balloon.offsetx,coordinate

**カテゴリ:** descript.txt

The X coordinate of the main character's balloon position.<br />
Appending a single character indicating direction to offsetx / offsety allows different values to be used depending on where the balloon is displayed (SSP only).

- **offsetx / offsety**: No direction specified. The default value used when the settings below are not specified.
- **offsetxl / offsetyl**: When the balloon is displayed to the left of the shell.
- **offsetxr / offsetyr**: When the balloon is displayed to the right of the shell.
- **offsetxc / offsetyc**: When the balloon is displayed above or below the shell. Used for both centered positions.
- **offsetxb / offsetyb**: When the balloon is displayed below the shell. Used to specify different values for above and below.

The values used when settings are omitted are as follows. The X and Y coordinates are determined independently.

- **When offsetxb is absent**: Look for offsetxc, then offsetx.
- **When offsetxc / offsetxl / offsetxr is absent**: Use offsetx.

The display position is determined by [windowposition.x](../../balloon/descript-txt/windowposition.x.md) in the balloon's descript.txt, [sakura.balloon.alignment](sakura.balloon.alignment.md) in the shell, and [`\![set,balloonalign,ID]`](../../../list/sakura-script/balloon-text/bang-set-balloonalign-ID.md) in Sakura Script.

**Pay attention to the sign.** A positive X coordinate always points toward the shell: rightward when displayed on the left, and **leftward** when displayed on the right (rightward is positive for above and below). A positive Y coordinate always points downward.<br />
However, the zero position (reference point) differs by direction. For left and right, it is where the top of the balloon aligns with the top of the shell image; for above, where the bottom of the balloon touches the top of the shell image; and for below, where the top of the balloon touches the bottom of the shell image.

This can also be specified in the ghost's descript.txt. If specified in the shell, the shell's value takes precedence; otherwise, the ghost's value is used.

**既定値:** No value

**対応:** Materia / SSP / CROW
