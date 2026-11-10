# `\![open,communicatebox]`

**カテゴリ:** Open command

Open CommunicateBox.<br />
After input is confirmed, [OnCommunicate](../../shiori-event/inputbox/OnCommunicate.md) is triggered. When it is closed, [OnCommunicateInputCancel](../../shiori-event/inputbox/OnCommunicateInputCancel.md) is triggered.<br />
SSP only: default text can be specified after the command (in the form `\![open,communicatebox,テキスト]`).<br />
SSP only: options can be specified in the form --option=○○; see [※options](bang-close-textareabox-ID.note.md). Optional.

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
\![open,communicatebox,テスト]CommunicateBoxを開く。最初から「テスト」の文字が入っている。
```

```sakurascript
\![open,communicatebox,--text=テスト]上記と同じ(オプション指定の書き方)
```
