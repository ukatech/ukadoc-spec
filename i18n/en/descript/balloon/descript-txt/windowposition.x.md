# windowposition.x,coordinate

**カテゴリ:** descript.txt

Adjusts the balloon's position along the x-axis from its default position.<br />
Specify a numeric value in pixels or a keyword.<br />
For numeric values, **positive is always to the right, regardless of whether the balloon appears on the left or right**. Note that unlike the shell's [balloon.offsetx](../../shell/descript-txt/sakura.balloon.offsetx.md), the sign is not reversed when the balloon appears on the right.<br />
center (top has the same effect in SSP only) fixes the balloon to the top center of the shell.<br />
bottom (SSP only) fixes the balloon to the bottom center of the shell.<br />
Other strings (such as left, right, and free) are not accepted and are treated as 0. In SSP, a warning is written to the error log.<br />
Also, only in SSP, this can be specified in descript.txt.

**既定値:** 0

**対応:** Materia / SSP / CROW
