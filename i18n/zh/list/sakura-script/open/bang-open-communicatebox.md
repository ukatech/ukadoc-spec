# `\![open,communicatebox]`

**カテゴリ:** 开放命令

打开 CommunicateBox。<br />
确认输入后会触发 [OnCommunicate](../../shiori-event/inputbox/OnCommunicate.md)。关闭时会触发 [OnCommunicateInputCancel](../../shiori-event/inputbox/OnCommunicateInputCancel.md)。<br />
仅 SSP 可继续指定默认文本（形式为 `\![open,communicatebox,テキスト]`）。<br />
仅 SSP 可通过 --option=○○ 的形式指定[※选项](bang-close-textareabox-ID.note.md)，也可以省略。

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
\![open,communicatebox,テスト]CommunicateBoxを開く。最初から「テスト」の文字が入っている。
```

```sakurascript
\![open,communicatebox,--text=テスト]上記と同じ(オプション指定の書き方)
```
