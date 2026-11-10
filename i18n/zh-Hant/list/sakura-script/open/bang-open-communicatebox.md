# `\![open,communicatebox]`

**カテゴリ:** 開啟命令

開啟 CommunicateBox。<br />
輸入確定後會觸發 [OnCommunicate](../../shiori-event/inputbox/OnCommunicate.md)。關閉時會觸發 [OnCommunicateInputCancel](../../shiori-event/inputbox/OnCommunicateInputCancel.md)。<br />
只有 SSP 可以接著指定預設文字（形式為 `\![open,communicatebox,テキスト]`）。<br />
只有 SSP 可以使用 --option=○○ 的形式指定[※選項](bang-close-textareabox-ID.note.md)。可省略。

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
\![open,communicatebox,テスト]CommunicateBoxを開く。最初から「テスト」の文字が入っている。
```

```sakurascript
\![open,communicatebox,--text=テスト]上記と同じ(オプション指定の書き方)
```
