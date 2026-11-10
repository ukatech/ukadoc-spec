# `\![set,balloonmarker,マーカー表示文字列]`

**カテゴリ:** balloon, text command

Displays the marker string shown when receiving SSTP.<br />
The display destination is the balloon belonging to the current scope.<br />
The display string is optional. To clear it, omit the argument or leave it blank.

It remains in effect until the ghost ends or a feature that normally uses this part, such as receiving SSTP, is activated.

Clearing means “cancel the string specified with this tag”; it does not hide the marker itself. If cleared while playing a script received via SSTP, the default sender display (from sender) is restored.<br />
Also, if a marker string is specified in the Marker header of SSTP or SHIORI, that takes precedence, and the value specified by this tag is not displayed.<br />
To omit the marker when outputting an image, use --hide=balloonmarker with [`\![execute,dumpballoon]`](../misc/bang-execute-dumpballoon-ID-prefix-ID.md).

**対応:** SSP 2.6.67
