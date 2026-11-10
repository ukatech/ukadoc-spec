# `\__v[オプション]`

**カテゴリ:** Balloon, text command

Adjusts how speech synthesis voices the text up to the next `\__v`.<br />
`\__v[disable]`: Disables speech synthesis<br />
`\__v[alternate,文字列]`: Specifies the correct spoken text for words with an ambiguous pronunciation. Hiragana is recommended to avoid misrecognition.

\[SSP only\] This also affects whether the text is recorded in the backlog (speech history).<br />
Text within a `\__v[disable]` section is neither spoken by speech synthesis nor recorded in the backlog.<br />
Text within a `\__v[alternate,文字列]` section is recorded in the backlog as the specified string instead of the original text, regardless of whether speech synthesis is enabled.

**対応:** SSP 2.4

## 記述例

```sakurascript
\1\__v[disable]この文章は音声合成機能でしゃべらない。\__v
```
