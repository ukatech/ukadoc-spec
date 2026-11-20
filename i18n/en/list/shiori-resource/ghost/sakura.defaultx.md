# sakura.defaultx

**カテゴリ:** Ghost information

The X coordinate of the default position for the main character (`\0`). The surface's reference point (usually its bottom center) is placed at this position.<br />
The default position is used when no display position has been saved, such as on first startup or after resetting the display position. If none is specified, the character is placed at the bottom right of the primary monitor's work area.<br />
The value is in pixels, in screen coordinates with the origin at the top left of the primary monitor (the position within the entire virtual desktop in a multi-monitor setup).<br />
A negative value specifies the distance from the right edge of the primary monitor's work area. -0 is the right edge itself.\[2.9.13\]<br />
To specify a negative coordinate directly, such as for a monitor to the left of the primary monitor, use two consecutive minus signs, as in --100 (X coordinate -100 in this example).\[2.9.13\]<br />
If [sakura.defaultleft](sakura.defaultleft.md) is also specified for the same axis, this setting (defaultx) takes precedence.<br />
The same entry can also be specified in the [ghost](../../../descript/shell/descript-txt/sakura.defaultx.md) or [shell](../../../descript/shell/descript-txt/sakura.defaultx.md) descript.txt\[2.9.13\]. The SHIORI resource takes precedence.<br />
This setting has no effect when the character is configured to appear along the left or right edge of the desktop, because the X coordinate is determined by that setting.

**対応:** SSP
