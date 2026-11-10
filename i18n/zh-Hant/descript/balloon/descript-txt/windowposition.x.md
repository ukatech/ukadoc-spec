# windowposition.x,coordinate

**カテゴリ:** descript.txt

Adjusts the balloon's position in the x-coordinate direction relative to its default position.<br />
Specify a numeric value in pixels or use a keyword.<br />
For numeric values, **right is always +**, regardless of whether the balloon appears on the left or right. Note that unlike the shell's [balloon.offsetx](../../shell/descript-txt/sakura.balloon.offsetx.md), the sign is not reversed when the balloon appears on the right.<br />
center (top has the same effect in SSP only) fixes the balloon to the top center of the shell.<br />
bottom (SSP only) fixes it to the bottom center of the shell.<br />
Other strings (left, right, free, etc.) are not accepted and are treated as 0. SSP outputs a warning to the error log.<br />
SSP also allows this to be specified in descript.txt.

**既定値:** 0

**対応:** Materia / SSP / CROW
