# `\__v[オプション]`

**カテゴリ:** Balloon, text commands

Adjusts how text between this tag and the next `\__v` is spoken by the speech synthesis function.<br />
`\__v[disable]`: Disables speech synthesis<br />
`\__v[alternate,文字列]`: Specifies the correct spoken text for words with different pronunciations. Hiragana is preferred to avoid misrecognition.

\[SSP only\] This effect also applies to entries in the backlog (utterance history).<br />
Text within a `\__v[disable]` section is neither spoken by speech synthesis nor recorded in the backlog.<br />
Text within a `\__v[alternate,文字列]` section is recorded in the backlog using the specified text instead of the regular text, regardless of whether speech synthesis is enabled.

**対応:** SSP 2.4

## 記述例

```sakurascript
\1\__v[disable]この文章は音声合成機能でしゃべらない。\__v
```
