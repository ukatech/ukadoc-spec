# sakura.balloon.offsetx,coordinates

**カテゴリ:** surface brace

The X coordinate of the main character's balloon position for this surface only.<br />
Appending one character indicating direction to offsetx / offsety allows different values to be used depending on where the balloon is displayed (SSP only).

- **offsetx / offsety**: No direction specified. The default values used when the entries below are not specified.
- **offsetxl / offsetyl**: When displaying the balloon to the left of the shell.
- **offsetxr / offsetyr**: When displaying the balloon to the right of the shell.
- **offsetxc / offsetyc**: When displaying the balloon above the shell or at its feet. Used for both positions, which are centered.
- **offsetxb / offsetyb**: When displaying the balloon at the feet of the shell. Use this when you want different values for above the head and at the feet.

If offsetxb is not specified, offsetxc is used; if that is also not specified, offsetx is used. If offsetxc / offsetxl / offsetxr are not specified, offsetx is used. The X and Y coordinates are determined independently.<br />
The values written here take precedence over values with the same name written in the shell's [descript.txt](../../shell/descript-txt/sakura.balloon.offsetx.md).

The sign convention is the same as for [sakura.balloon.offsetx in descript.txt](../../shell/descript-txt/sakura.balloon.offsetx.md).

**既定値:** When displayed on the left or right: position where the balloon's left or right edge aligns with the surface's right or left edge<br />
When displayed above the head or at the feet: center of the surface

**対応:** Materia / SSP / CROW
