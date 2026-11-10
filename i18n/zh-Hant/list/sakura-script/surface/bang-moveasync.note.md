# About `\![move]` and `\![moveasync]`

New specification: (SSP 2.3.85 and later)

`\![move(async),--X=X座標,--Y=Y座標,--time=移動時間,--base=移動基準,--base-offset=基準とするキャラ基準位置,--move-offset=動かすキャラ基準位置,--option=オプション]`

All parameters are optional. Their order may also be changed. The case of parameter names is ignored (for example, you may write --x=10)

Old specification:

`\![move(async),X座標,Y座標,移動時間,移動基準,基準とするキャラ基準位置,動かすキャラ基準位置]`

Parameters from the move duration onward are optional.

*X coordinate and Y coordinate* specify the destination coordinates.<br />
Negative values are also allowed.<br />
If either is omitted or specified as "fix", that coordinate is kept.<br />
Default: "fix"

*Move duration* is in milliseconds.<br />
If the move duration is omitted or specified as 0, the move is instantaneous.<br />
Default: 0

*Reference position* is the character or other element used as the origin for the move (the origin of relative coordinates).<br />
Specify it as follows.<br />
Default: screen

- **screen**: Coordinates with the top-left corner of the monitor containing the current character window as the origin. Default value
- **primaryscreen**: Coordinates with the top-left corner of the primary monitor (ID=1) as the origin.
- **ID**: Relative coordinates to the character in the scope with the specified ID, such as 0 or 1 (corresponding to the number of `\0`, `\1`, `\p[2]`, etc.)
- **本体側名/ID**: Relative coordinates to the character in the scope with the specified ID of another ghost, specified by its baseware-side name (sakura name, `\0` name)
- **me**: Relative coordinates to the character being moved
- **primaryscreen**: Coordinates with the top-left corner of the primary monitor as the origin
- **global**: System coordinate system (the same as primaryscreen on windows)

*Character reference position* specifies which point is used as the origin when a character or screen is specified as the move reference.<br />
Specify it in the form X reference.Y reference, combining one of the following four values for each:<br />
X reference: left,right,base,center<br />
Y reference: top,bottom,base,center<br />
Combine the values, for example, as right.base.<br />
Note that base follows the point.basepos setting in surfaces.txt.<br />
Default: left.top

For screen, base cannot be used; for global, right,bottom,center cannot be used.

*Moving character reference position* is specified in the same way as the character reference position.

*Options* can be specified multiple times. Specify them as follows. Only the new specification format is supported.

- **ignore-sticky-window**: Move independently, ignoring the linked settings for `\![set,sticky-window]`
