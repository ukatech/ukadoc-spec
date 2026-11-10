# Notes

## How to specify the shape

- **square**: Display a rectangle.
- **underline**: Display an underline.
- **square+underline**: Display a rectangle and an underline.
- **none**: Do not display.
- **default**: Return to the balloon setting's default.

## How to specify the text color

This is basically similar to how colors are represented in HTML and CSS.<br />
\[2.8.93\] Values that do not match any of the following (such as non-numeric R,G,B values or color codes containing non-hexadecimal characters) are ignored. Previously, they could be treated as black.

- **R,G,B**: Represent the brightness of the three primary colors, red, green, and blue, respectively, as decimal values from 0 to 255, separated by commas.<br />
  0,0,0 is black; 255,255,255 is white.
- **R%,G%,B%**: Represent the brightness of the three primary colors, red, green, and blue, respectively, as percentages from 0% to 100%, separated by commas.<br />
  0%,0%,0% is black; 100%,100%,100% is white.
- **Hexadecimal color code**: Join the brightness values of the three primary colors, red, green, and blue, expressed in *hexadecimal* after a "#", as in #07f.<br />
  Each color can be represented using either two digits, for a total of six, or one digit, for a total of three.<br />
  Hexadecimal letters may be uppercase or lowercase.<br />
  #000000 or #000 is black; #ffffff or #fff is white.
- **Predefined keywords**: Specify a color using a keyword representing its name, such as red, white, or black (all lowercase).<br />
  For colors whose definitions differ between X11 color and W3C color (such as green and gray), the W3C color definition is used.<br />
  Color samples: [CSS Color Module Level 3 Extended color keywords](http://www.w3.org/TR/css3-color/#svg-color)(external link)
- **default**: Writing default in the color specification sets the specified text to its default color.<br />
  The default color is defined in the balloon's descript.txt, among other places (black if undefined).
- **disable**: Writing disable in the color specification sets the color to that used for disabled display.
- **default.anchor**: Specifying default.anchor in the color specification changes the specified text color to the default text color of an anchor when selected.<br />
  \[2.5.76 - Became available for ordinary text\]
- **default.anchornotselect**: Specifying default.anchornotselect in the color specification changes the specified text color to the default text color of an anchor when not selected.<br />
  \[2.5.76 - Became available for ordinary text\]
- **default.anchorvisited**: Specifying default.anchorvisited in the color specification changes the specified text color to the default text color of a visited anchor.<br />
  \[2.5.76 - Became available for ordinary text\]
- **default.cursor**: *※Can only be specified for the text color of choices and anchors*.<br />
  Specifying default.cursor in the color specification changes the specified text color to the default text color of a choice when selected.
- **default.cursornotselect**: *※Can only be specified for the text color of choices and anchors*.<br />
  Specifying default.anchor in the color specification changes the specified text color to the default text color of a choice when not selected.
- **default.plain**: *※Can only be specified for the text color of choices and anchors*.<br />
  Specifying default.plain in the color specification changes the specified text color to the default text color of ordinary text.
