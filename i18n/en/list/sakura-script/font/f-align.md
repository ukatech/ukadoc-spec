# `\f[align,寄せる側]`

**カテゴリ:** Text formatting command

Sets text to right-aligned (`\f[align,right]`), centered (`\f[align,center]`), or left-aligned (`\f[align,left]`).<br />
This setting remains in effect until an "intentional line break" such as `\n` or `\_l` occurs.<br />
If this command is run while text or other content is being added, it also moves text already added on the same line.<br />
When the `\_l` tag is encountered, alignment returns to left.<br />
If centered alignment is set with the `\f[align]` tag after moving with the `\_l` tag, centering is performed as if the text had been indented by the `\_l` tag's X coordinate.<br />
In vertical writing mode, left means top-aligned, right means bottom-aligned, and center means vertically centered.

**対応:** SSP 2.5.31

## 記述例

```sakurascript
\f[align,center]これは中央揃え。\n\f[align,right]これは右揃え。\n\f[align,left]左揃えのつもりが\w9\w9\f[align,right]右揃えに。
```
