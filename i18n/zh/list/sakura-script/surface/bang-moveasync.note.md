# About `\![move]` and `\![moveasync]`

New specification: (SSP 2.3.85 and later)

`\![move(async),--X=X座標,--Y=Y座標,--time=移動時間,--base=移動基準,--base-offset=基準とするキャラ基準位置,--move-offset=動かすキャラ基準位置,--option=オプション]`

All arguments are optional. Their order can also be changed. The specified names are case-insensitive (for example, --x=10 is also valid).

Old specification:

`\![move(async),X座標,Y座標,移動時間,移動基準,基準とするキャラ基準位置,動かすキャラ基準位置]`

Arguments after the movement time are optional.

*X coordinate, Y coordinate* specify the target coordinates.<br />
Negative values can also be specified.<br />
If either is omitted or set to "fix", that coordinate is retained.<br />
Default: "fix"

*Movement time* is in milliseconds.<br />
If the movement time is omitted or set to 0, movement is instantaneous.<br />
Default: 0

*Reference position* is the character or other reference used for movement (the origin of relative coordinates).<br />
The available values are as follows.<br />
Default: screen

- **screen**: Coordinates with the upper-left corner of the monitor containing the character window as the origin. Initial value
- **primaryscreen**: Coordinates with the upper-left corner of the main monitor (ID=1) as the origin.
- **ID**: Relative coordinates to the character in the scope with the specified ID, such as 0 or 1 (corresponding to the number in `\0`, `\1`, `\p[2]`, etc.)
- **Main-side name/ID**: Relative coordinates to the character in the scope with the specified ID of another ghost, specified by its main-side name (sakura name, `\0` name)
- **me**: Relative coordinates to the character being moved
- **primaryscreen**: Coordinates with the upper-left corner of the primary monitor as the origin
- **global**: System coordinate system (same as primaryscreen on Windows)

*Reference point on the character used as the reference* specifies which point is the origin when a character or screen is specified as the movement reference.<br />
Specify it as X reference.Y reference, combining the following four values:<br />
X reference: left, right, base, center<br />
Y reference: top, bottom, base, center<br />
Combine one from each, and write it like right.base.<br />
base follows the point.basepos specification in surfaces.txt.<br />
Default: left.top

For screen, base cannot be used; for global, right, bottom, and center cannot be used.

*Reference point on the character being moved* is specified in the same way as the reference point on the character used as the reference.

*Options* can be specified multiple times. They can be specified as follows. Only the new specification format can be used.

- **ignore-sticky-window**: Move independently, ignoring the coordination setting made with `\![set,sticky-window]`
