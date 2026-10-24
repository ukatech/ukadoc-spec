# `\![open,timeinput,ID,表示時間,時,分,秒,オプション]`

**カテゴリ:** オープンコマンド

時間入力InputBoxを開く。<br />
時,分,秒は初期値。24時間表記。<br />
入力値はOnUserInputのReference1にカンマ区切りで「時,分,秒」と入る。<br />
--option=○○の形で[※オプション](notes_inputbox-option.md)指定可能。

<br />
その他の動作は[inputbox](bang-open-inputbox-ID.md)と同じ。

**対応:** SSP

## 記述例

```sakurascript
\![open,timeinput,時間入力テスト,30000,23,45,12]初期値が23時45分12秒の時間入力InputBoxを開く。30秒でタイムアウトする。
```

```sakurascript
\![open,timeinput,時間入力テスト,--timeout=30000,--text="23,45,12"] 上記と同じ(新オプション指定)
```
