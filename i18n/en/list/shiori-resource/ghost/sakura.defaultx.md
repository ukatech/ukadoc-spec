# sakura.defaultx

**カテゴリ:** Ghost information

The default X coordinate of the main character (`\0`). The surface's reference point (usually the bottom center of the surface) is placed at this position.<br />
The default position is used when the display position has not been saved (such as on first launch or after resetting the display position). If none of these settings are specified, the character is placed at the bottom right of the primary monitor's work area.<br />
The unit is pixels, in screen coordinates with the top-left of the primary monitor as the origin (on a multi-monitor setup, the position is relative to the entire virtual desktop).<br />
A negative value specifies the distance from the right edge of the primary monitor's work area. -0 is the right edge itself.\[2.9.13\]<br />
To specify a negative coordinate itself, such as a monitor to the left of the primary monitor, prefix - twice, as in --100 (this example is X coordinate -100).\[2.9.13\]<br />
If [sakura.defaultleft](sakura.defaultleft.md) is also specified for the same axis, this setting (defaultx) takes precedence.<br />
The same item can also be specified in the descript.txt of the [ghost](../../../descript/ghost/descript-txt/sakura.defaultx.md) or [shell](../../../descript/shell/descript-txt/sakura.defaultx.md)\[2.9.13\]. The SHIORI resource takes precedence.<br />
This setting is ignored when configured to display along the left or right edge of the desktop, because the X coordinate is determined by that setting.

**対応:** SSP
