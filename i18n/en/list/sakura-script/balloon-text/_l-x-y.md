# `\_l[x,y]`

**カテゴリ:** Balloon, text command

Move the cursor for the current scope to the specified XY coordinates. X and Y can be specified as follows.<br />
Note that immediately after `\_l` is executed, alignment is reset to left alignment to prevent problems. Specify it again as needed.

- **Number**: Coordinates in pixels from the balloon's text drawing origin (the position of [origin](../../../descript/balloon/descript-txt/origin.x.md); the top-left of the text drawing area for horizontal writing)
- **(omitted)**: Do not move. Omitting both X and Y has no effect.
- **centerx / centery**: Writing centerx for X or centery for Y moves the cursor to the center of the balloon image (half its width or height). Unlike other values, this is relative to the balloon image itself, not the text drawing origin.
- **XXem**: Appending em specifies coordinates relative to the text height. 1em is the text height at the time the tag is written. Decimal values are allowed.
- **XXlh**: Appending lh specifies coordinates relative to the line height. 1lh = 1em + line spacing. Decimal values are allowed.
- **XX%**: Appending % specifies coordinates relative to the text height. 100% is the text height at the time the tag is written. Decimal values are allowed.
- **@XX**: Specifies coordinates relative to the current text drawing position. Negative X values go left, and negative Y values go up. Can be used together with em or % values.

Even in a [vertical-writing balloon](../../../descript/balloon/descript-txt/vertical.md), the coordinate axes are those of the balloon image: positive X is to the right, and positive Y is downward.<br />
However, the text drawing origin is at the *top right* of the text drawing area, and columns advance from there to the left, so a negative X value is needed to move to the next column. Y follows the text progression direction (top to bottom), so it can be used just as in horizontal writing.<br />
For example, `\_l[@-1lh,0]` means “go to the start of the column one column to the left” (equivalent to `\_l[0,@1lh]` in horizontal writing), and `\_l[,@1em]` means “advance the text by one character.”

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
\_l[30,5em]「座標X=30pixel、座標Y=5文字分高さ」に表示。\_l[@-1650%,100]「座標X=最後の文字から文字高さ1650%分左、座標Y=100pixel」に表示。\_l[,@-100]「座標X=変更なし、座標Y=最後の文字から100pixel上」に表示。
```
