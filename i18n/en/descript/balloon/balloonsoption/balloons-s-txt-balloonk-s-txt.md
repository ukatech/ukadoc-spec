# balloons\*s.txt/balloonk\*s.txt

## Overview

Individual settings files for each balloon surface (balloons0.png, balloonk0.png, ...) and input box.<br />
Settings in descript.txt are treated as the default settings. If the same item is set here, only that item is overridden.

One file can be provided for each surface (for example, balloons0s.txt for balloons0.png; note the s at the end of the filename).

Basically, all items can be configured, but name, type, craftman, craftmanurl, id, homeurl, and readme, which apply to the balloon as a whole, cannot be configured (they have no effect).<br />
Additionally, windowposition.x and windowposition.y are available to adjust the display position relative to the shell's surfaces (SSP also allows these to be configured in descript.txt).

For the multiple-line input box balloonc5.png (SSP 2.9.10), the range specified by communicatebox.x/y/width/height in balloonc5s.txt covers both the input field and the row of buttons beneath it.<br />
This range does not inherit the values in descript.txt (for a one-line input box). If not specified in balloonc5s.txt, the range is inset 8 pixels from each edge of the image.<br />
The text size follows font.height in balloonc5s.txt (or font.height in descript.txt if omitted); the typeface and colors follow communicatebox.font.name/font.color/background.color.

**対応:** Materia / SSP / CROW
