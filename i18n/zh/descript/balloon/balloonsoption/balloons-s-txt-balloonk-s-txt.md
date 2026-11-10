# balloons\*s.txt/balloonk\*s.txt

## Overview

Individual configuration files for each balloon surface (balloons0.png, balloonk0.png, ...) and the input box.<br />
Settings in descript.txt are treated as the defaults. If the same item is set here, only that item is overridden.

One file can be provided for each surface (for example, balloons0s.txt for balloons0.png. Note the s at the end of the filename).

Basically, all items can be configured, but name, type, craftman, craftmanurl, id, homeurl, and readme, which apply to the balloon as a whole, cannot be set (they have no effect).<br />
Also, windowposition.x and windowposition.y are additional settings for adjusting the display position relative to the shell surface (only SSP also allows these to be set in descript.txt).

For balloonc5.png (SSP 2.9.10), used for multiline input boxes, communicatebox.x/y/width/height in balloonc5s.txt define the area containing both the input field and the row of buttons beneath it.<br />
This area does not inherit values from descript.txt (which are intended for single-line input boxes). If not specified in balloonc5s.txt, the area is inset 8 pixels from each edge of the image.<br />
The font size follows font.height in balloonc5s.txt (or font.height in descript.txt if omitted), while the typeface and colors follow communicatebox.font.name/font.color/background.color.

**対応:** Materia / SSP / CROW
