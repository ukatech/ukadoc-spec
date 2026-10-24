# `\![open,communicatebox]`

**カテゴリ:** オープンコマンド

CommunicateBoxを開く。<br />
入力決定後は[OnCommunicate](../../shiori-event/inputbox/OnCommunicate.md)が発生する。閉じると[OnCommunicateInputCancel](../../shiori-event/inputbox/OnCommunicateInputCancel.md)が発生する。<br />
SSPのみ、続けてデフォルトのテキストを指定できる(`\![open,communicatebox,テキスト]`の形)。<br />
SSPのみ、--option=○○の形で[※オプション](notes_inputbox-option.md)指定可能。省略可。

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
\![open,communicatebox,テスト]CommunicateBoxを開く。最初から「テスト」の文字が入っている。
```

```sakurascript
\![open,communicatebox,--text=テスト]上記と同じ(オプション指定の書き方)
```
