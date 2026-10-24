# `\![open,dateinput,ID,表示時間,年,月,日,オプション]`

**カテゴリ:** オープンコマンド

年月日入力InputBoxを開く。<br />
表示時間はミリ秒で指定。<br />
年,月,日は初期値。<br />
入力決定時にSHIORIイベント[OnUserInput](../../shiori-event/inputbox/OnUserInput.md)が発生し、Reference1にカンマ区切りで「年,月,日」と入る。<br />
表示時間を過ぎた(タイムアウトした)場合と、閉じるボタンを押して閉じた場合は、[OnUserInputCancel](../../shiori-event/inputbox/OnUserInputCancel.md)が発生する。<br />
--option=○○の形で[※オプション](notes_inputbox-option.md)指定可能。<br />
その他の動作は[inputbox](bang-open-inputbox-ID.md)と同じ。

**対応:** SSP

## 記述例

```sakurascript
\![open,dateinput,日付入力テスト,30000,2012,12,23]初期値が2012年12月23日の年月日入力InputBoxを開く。30秒でタイムアウトする。
```

```sakurascript
\![open,dateinput,日付入力テスト,--timeout=30000,--text="2012,12,23"] 上記と同じ(新オプション指定)
```
