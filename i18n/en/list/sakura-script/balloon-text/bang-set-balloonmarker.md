# `\![set,balloonmarker,マーカー表示文字列]`

**カテゴリ:** Balloon, text command

Displays the marker string shown when receiving SSTP.<br />
The display target is the balloon belonging to the current scope.<br />
The display string is optional. To clear it, omit the argument or leave it empty.

It remains in effect until the ghost terminates or a feature that normally uses this area, such as receiving SSTP, is triggered.

Clearing means “cancel the string specified by this tag”; it does not hide the marker itself. If cleared while playing a script received via SSTP, the display reverts to the default sender display (from sender).<br />
Also, if a marker string is specified in the Marker header of SSTP or SHIORI, that value takes precedence and the value specified by this tag is not displayed.<br />
To omit the marker when outputting an image, use --hide=balloonmarker with [`\![execute,dumpballoon]`](../misc/bang-execute-dumpballoon-ID-prefix-ID.md).

**対応:** SSP 2.6.67
