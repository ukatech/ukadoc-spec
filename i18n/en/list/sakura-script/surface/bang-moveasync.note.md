# About `\![move]` and `\![moveasync]`

New syntax: (SSP 2.3.85 and later)

`\![move(async),--X=X座標,--Y=Y座標,--time=移動時間,--base=移動基準,--base-offset=基準とするキャラ基準位置,--move-offset=動かすキャラ基準位置,--option=オプション]`

All parameters are optional. Their order can also be changed. The specified names are case-insensitive (for example, you can write --x=10)

Old syntax:

`\![move(async),X座標,Y座標,移動時間,移動基準,基準とするキャラ基準位置,動かすキャラ基準位置]`

Parameters from the move time onward are optional.

*X coordinate and Y coordinate* specify the destination coordinates.<br />
Negative values can also be specified.<br />
If either coordinate is omitted or set to "fix", that coordinate is kept.<br />
Default: "fix"

*Move time* is in milliseconds.<br />
If move time is omitted or set to 0, the character moves instantly.<br />
Default: 0

*Reference position* is the character or other reference point for the movement (the origin of the relative coordinates).<br />
Specify it as follows.<br />
Default: screen

- **screen**: Coordinates with the top left of the monitor containing the current character window as the origin. Default value
- **primaryscreen**: Coordinates with the top left of the main monitor (ID=1) as the origin.
- **ID**: Relative coordinates to the character in the scope with the specified ID (corresponding to the number of `\0`, `\1`, `\p[2]`, etc.)
- **host-side name/ID**: Relative coordinates to the character in the scope with the specified ID of another ghost, specified by its host-side name (sakura name, `\0` name)
- **me**: Relative coordinates to the character being moved
- **primaryscreen**: Coordinates with the top left of the primary monitor as the origin
- **global**: System coordinate system (the same as primaryscreen on Windows)

*Reference character anchor position* specifies which point to use as the origin when a character or screen is specified as the movement reference.<br />
Specify it in the form X anchor.Y anchor, combining one of the following four values for each:<br />
X anchor: left,right,base,center<br />
Y anchor: top,bottom,base,center<br />
For example, write right.base.<br />
base follows the point.basepos setting in surfaces.txt.<br />
Default: left.top

For screen, base cannot be used; for global, right,bottom,center cannot be used.

*Moving character anchor position* is specified in the same way as the reference character anchor position.

*Options* can be specified multiple times. Specify them as follows. Only the new syntax supports options.

- **ignore-sticky-window**: Move independently, ignoring the linkage settings from `\![set,sticky-window]`
