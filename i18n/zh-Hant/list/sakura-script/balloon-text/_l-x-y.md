# `\_l[x,y]`

**カテゴリ:** balloon, text command

Move the cursor position in the current scope to the specified XY coordinates. X and Y can be specified as follows.<br />
Note that immediately after `\_l` runs, line alignment is reset to left alignment to prevent problems. Set it again as needed.

- **number**: Coordinates in pixels from the start of text rendering in the balloon (the [origin](../../../descript/balloon/descript-txt/origin.x.md) position; the upper-left of the text-rendering area for horizontal text)
- **(omitted)**: Do not move. Omitting both X and Y has no effect.
- **centerx / centery**: If you write centerx for X and centery for Y, the cursor moves to the center of the balloon image (half its width / height). This is the only option based on the balloon image itself, rather than the start of text rendering.
- **XXem**: Add em at the end to specify coordinates based on the text height. 1em is the text height when the tag is written. Decimal values are allowed.
- **XXlh**: Add lh at the end to specify coordinates based on the line height. 1lh = 1em + line spacing. Decimal values are allowed.
- **XX%**: Add % at the end to specify coordinates based on the text height. 100% is the text height when the tag is written. Decimal values are allowed.
- **@XX**: Specifies relative coordinates from the current text-rendering position. A negative X value moves left; a negative Y value moves up. Can be combined with em and % specifications.

The coordinate axes remain the same as the balloon image in [vertical-text balloons](../../../descript/balloon/descript-txt/vertical.md), with positive X pointing right and positive Y pointing down.<br />
However, the start of text rendering is at the *upper right* of the text-rendering area, and columns advance to the left. Therefore, specify a negative X value to move to the next column. Y follows the direction of character progression (top to bottom), so it works the same way as for horizontal text.<br />
For example, `\_l[@-1lh,0]` means “move to the start of the column one column to the left” (equivalent to `\_l[0,@1lh]` in horizontal text), while `\_l[,@1em]` means “advance character progression by one character.”

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
\_l[30,5em]「座標X=30pixel、座標Y=5文字分高さ」に表示。\_l[@-1650%,100]「座標X=最後の文字から文字高さ1650%分左、座標Y=100pixel」に表示。\_l[,@-100]「座標X=変更なし、座標Y=最後の文字から100pixel上」に表示。
```
