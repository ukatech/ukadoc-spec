# `\![open,timeinput,ID,表示時間,時,分,秒,オプション]`

**カテゴリ:** 開啟命令

開啟時間輸入 InputBox。<br />
時、分、秒為初始值，使用 24 小時制。<br />
輸入值會以逗號分隔的「時、分、秒」形式放入 OnUserInput 的 Reference1。<br />
可使用 --option=○○ 的形式指定[※選項](bang-close-textareabox-ID.note.md)。

<br />
其他動作與[inputbox](bang-open-inputbox-ID.md)相同。

**対応:** SSP

## 記述例

```sakurascript
\![open,timeinput,時間入力テスト,30000,23,45,12]初期値が23時45分12秒の時間入力InputBoxを開く。30秒でタイムアウトする。
```

```sakurascript
\![open,timeinput,時間入力テスト,--timeout=30000,--text="23,45,12"] 上記と同じ(新オプション指定)
```
