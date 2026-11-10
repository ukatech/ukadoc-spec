# windowposition.x,坐标

**カテゴリ:** descript.txt

相对于气球基本位置沿x坐标方向调整位置。<br />
以像素为单位用数值或关键字指定。<br />
指定数值时，**无论气球显示在左右哪侧，始终以右方为+**。请注意，这与shell的[balloon.offsetx](../../shell/descript-txt/sakura.balloon.offsetx.md)不同，即使气球显示在右侧，符号也不会反转。<br />
指定center时（仅限SSP，top也相同），固定在shell中央上方。<br />
指定bottom时（仅限SSP），固定在shell中央下方。<br />
不接受上述以外的字符串（例如left、right、free），这些值会按0处理。SSP会在错误日志中显示警告。<br />
此外，仅限SSP，也可以写在descript.txt中。

**既定値:** 0

**対応:** Materia / SSP / CROW
