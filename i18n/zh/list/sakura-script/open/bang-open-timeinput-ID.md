# `\![open,timeinput,ID,表示時間,時,分,秒,オプション]`

**カテゴリ:** 打开命令

打开时间输入 InputBox。<br />
时、分、秒为初始值。使用 24 小时制。<br />
输入值会以逗号分隔的「时,分,秒」形式放入 OnUserInput 的 Reference1。<br />
可以使用--option=○○的形式指定[※选项](bang-close-textareabox-ID.note.md)。

<br />
其他行为与[inputbox](bang-open-inputbox-ID.md)相同。

**対応:** SSP

## 記述例

```sakurascript
\![open,timeinput,時間入力テスト,30000,23,45,12]初期値が23時45分12秒の時間入力InputBoxを開く。30秒でタイムアウトする。
```

```sakurascript
\![open,timeinput,時間入力テスト,--timeout=30000,--text="23,45,12"] 上記と同じ(新オプション指定)
```
