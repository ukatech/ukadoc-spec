# `\![open,dateinput,ID,表示時間,年,月,日,オプション]`

**カテゴリ:** 開啟命令

開啟年月日輸入 InputBox。<br />
顯示時間以毫秒指定。<br />
年、月、日為初始值。<br />
輸入確定時會觸發 SHIORI 事件 [OnUserInput](../../shiori-event/inputbox/OnUserInput.md)，並在 Reference1 中以逗號分隔的「年,月,日」格式放入內容。<br />
超過顯示時間（逾時）或按下關閉按鈕關閉時，會觸發 [OnUserInputCancel](../../shiori-event/inputbox/OnUserInputCancel.md)。<br />
可使用 --option=○○ 的形式指定[※選項](bang-close-textareabox-ID.note.md)。<br />
其他行為與 [inputbox](bang-open-inputbox-ID.md) 相同。

**対応:** SSP

## 記述例

```sakurascript
\![open,dateinput,日付入力テスト,30000,2012,12,23]初期値が2012年12月23日の年月日入力InputBoxを開く。30秒でタイムアウトする。
```

```sakurascript
\![open,dateinput,日付入力テスト,--timeout=30000,--text="2012,12,23"] 上記と同じ(新オプション指定)
```
