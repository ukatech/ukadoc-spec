# `\![open,dateinput,ID,表示時間,年,月,日,オプション]`

**カテゴリ:** 开放命令

打开年月日输入 InputBox。<br />
显示时间以毫秒为单位指定。<br />
年、月、日为初始值。<br />
确认输入时会触发 SHIORI 事件 [OnUserInput](../../shiori-event/inputbox/OnUserInput.md)，Reference1 中会以逗号分隔的形式存放“年,月,日”。<br />
超过显示时间（超时）或按下关闭按钮关闭时，会触发 [OnUserInputCancel](../../shiori-event/inputbox/OnUserInputCancel.md)。<br />
可以通过 --option=○○ 的形式指定[※选项](bang-close-textareabox-ID.note.md)。<br />
其他行为与 [inputbox](bang-open-inputbox-ID.md) 相同。

**対応:** SSP

## 記述例

```sakurascript
\![open,dateinput,日付入力テスト,30000,2012,12,23]初期値が2012年12月23日の年月日入力InputBoxを開く。30秒でタイムアウトする。
```

```sakurascript
\![open,dateinput,日付入力テスト,--timeout=30000,--text="2012,12,23"] 上記と同じ(新オプション指定)
```
