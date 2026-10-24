# `\![open,ipinput,ID,表示時間,IP1桁目,IP2桁目,IP3桁目,IP4桁目,オプション]`

**カテゴリ:** オープンコマンド

IPアドレス入力InputBoxを開く。<br />
Windows上では入力ボックスの制限のため、IPv4アドレスのみ受け入れ可能。<br />
--option=○○の形で[※オプション](notes_inputbox-option.md)指定可能。

<br />
その他の動作は[inputbox](bang-open-inputbox-ID.md)と同じ。

**対応:** SSP

## 記述例

```sakurascript
\![open,ipinput,IP入力テスト,30000,192,168,0,1]
```

```sakurascript
\![open,ipinput,IP入力テスト,--timeout=30000,--text="192,168,0,1"]
```
