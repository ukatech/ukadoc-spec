# sakura.defaultx

**カテゴリ:** Ghost information

The default X coordinate of the main character (`\0`). The surface's origin (normally the bottom center of the surface) is placed at this position.<br />
The default position is used when no display position has been saved, such as on first launch or after resetting the display position. If none of these settings is specified, the character is placed at the bottom right of the primary monitor's work area.<br />
The value is in pixels, using screen coordinates with the top-left of the primary monitor as the origin (in a multi-monitor setup, the position is relative to the entire virtual desktop).<br />
A negative value is the distance from the right edge of the primary monitor's work area. -0 is the right edge itself.\[2.9.13\]<br />
To specify a negative coordinate itself, such as a monitor to the left of the primary monitor, prefix the value with two hyphens, as in --100 (this example is X coordinate -100).\[2.9.13\]<br />
If [sakura.defaultleft](sakura.defaultleft.md) is also specified for the same axis, this setting (defaultx) takes precedence.<br />
The same item can also be specified in the descript.txt of a [ghost](../../../descript/ghost/descript-txt/sakura.defaultx.md) or [shell](../../../descript/shell/descript-txt/sakura.defaultx.md)\[2.9.13\]. The SHIORI Resource takes precedence.<br />
When configured to display along the left or right edge of the desktop, the X coordinate is determined by that setting and is ignored.

**対応:** SSP
