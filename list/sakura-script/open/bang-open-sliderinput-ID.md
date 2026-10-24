# `\![open,sliderinput,ID,表示時間,現在値,最小,最大,オプション]`

**カテゴリ:** オープンコマンド

スライダー調節型のInputBoxを開く。<br />
入力決定時にSHIORIイベント[OnUserInput](../../shiori-event/inputbox/OnUserInput.md)が発生し、Reference1に入力値が入る。<br />
--option=○○の形で[※オプション](notes_inputbox-option.md)指定可能。<br />
その他の動作は[inputbox](bang-open-inputbox-ID.md)と同じ。<br />
許容最小値は-2147483648、最大値は2147483647です。

**対応:** SSP

## 記述例

```sakurascript
\![open,sliderinput,スライダーテスト,30000,50,0,100]初期値が50、最小値が0、最大が100のスライダー型InputBoxを開く。30秒でタイムアウトする。
```

```sakurascript
\![open,sliderinput,スライダーテスト,--timeout=30000,--text="50,0,100"] 上記と同じ(新オプション指定)
```
