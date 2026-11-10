# `\![open,dateinput,ID,表示時間,年,月,日,オプション]`

**カテゴリ:** Open command

Open a year/month/day input InputBox.<br />
Specify the display duration in milliseconds.<br />
The year, month, and day are the initial values.<br />
When input is confirmed, the SHIORI event [OnUserInput](../../shiori-event/inputbox/OnUserInput.md) is triggered, and Reference1 contains "year,month,day" as a comma-separated string.<br />
If the display duration expires (times out), or the box is closed with the close button, [OnUserInputCancel](../../shiori-event/inputbox/OnUserInputCancel.md) is triggered.<br />
Options can be specified in the form --option=○○; see [※options](bang-close-textareabox-ID.note.md).<br />
Other behavior is the same as for [inputbox](bang-open-inputbox-ID.md).

**対応:** SSP

## 記述例

```sakurascript
\![open,dateinput,日付入力テスト,30000,2012,12,23]初期値が2012年12月23日の年月日入力InputBoxを開く。30秒でタイムアウトする。
```

```sakurascript
\![open,dateinput,日付入力テスト,--timeout=30000,--text="2012,12,23"] 上記と同じ(新オプション指定)
```
