# `\![open,timeinput,ID,表示時間,時,分,秒,オプション]`

**カテゴリ:** Open command

Open a time-input InputBox.<br />
時,分,秒 are the initial values, using 24-hour time.<br />
The input value is placed in Reference1 of OnUserInput as a comma-separated “hour,minute,second” string.<br />
Options can be specified in the form --option=○○ via [※options](bang-close-textareabox-ID.note.md).

<br />
Other behavior is the same as [inputbox](bang-open-inputbox-ID.md).

**対応:** SSP

## 記述例

```sakurascript
\![open,timeinput,時間入力テスト,30000,23,45,12]初期値が23時45分12秒の時間入力InputBoxを開く。30秒でタイムアウトする。
```

```sakurascript
\![open,timeinput,時間入力テスト,--timeout=30000,--text="23,45,12"] 上記と同じ(新オプション指定)
```
