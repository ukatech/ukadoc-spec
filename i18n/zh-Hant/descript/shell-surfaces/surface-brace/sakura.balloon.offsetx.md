# sakura.balloon.offsetx,coordinates

**カテゴリ:** surface block

The X coordinate of the main-side balloon position for this surface only.<br />
Appending one direction character after offsetx / offsety allows different values to be used depending on where the balloon appears (SSP only).

- **offsetx / offsety**: No direction specified. Used as the default when the entries below are not written.
- **offsetxl / offsetyl**: When displaying the balloon to the left of the shell.
- **offsetxr / offsetyr**: When displaying the balloon to the right of the shell.
- **offsetxc / offsetyc**: When displaying the balloon above the head or at the feet of the shell. Shared by both centered positions.
- **offsetxb / offsetyb**: When displaying the balloon at the feet of the shell. Use these when different values are needed for above the head and at the feet.

If offsetxb is not specified, offsetxc is used; if that is also not specified, offsetx is used. If offsetxc / offsetxl / offsetxr are not specified, offsetx is used. The X and Y coordinates are determined independently.<br />
The value specified here takes precedence over the same-named value in the shell's [descript.txt](../../shell/descript-txt/sakura.balloon.offsetx.md).

The sign direction is the same as for [sakura.balloon.offsetx in descript.txt](../../shell/descript-txt/sakura.balloon.offsetx.md).

**既定値:** When displayed to the left or right: the position where the left or right edge of the balloon aligns with the right or left edge of the surface<br />
When displayed above the head or at the feet: the center of the surface

**対応:** Materia / SSP / CROW
