# `\![open,sliderinput,ID,表示時間,現在値,最小,最大,オプション]`

**カテゴリ:** Open command

Open a slider-style InputBox.<br />
When input is confirmed, the SHIORI event [OnUserInput](../../shiori-event/inputbox/OnUserInput.md) occurs, and the input value is placed in Reference1.<br />
Options can be specified in the form --option=○○ [※オプション](bang-close-textareabox-ID.note.md).<br />
Other behavior is the same as [inputbox](bang-open-inputbox-ID.md).<br />
The minimum allowed value is -2147483648 and the maximum is 2147483647.

**対応:** SSP

## 記述例

```sakurascript
\![open,sliderinput,スライダーテスト,30000,50,0,100]初期値が50、最小値が0、最大が100のスライダー型InputBoxを開く。30秒でタイムアウトする。
```

```sakurascript
\![open,sliderinput,スライダーテスト,--timeout=30000,--text="50,0,100"] 上記と同じ(新オプション指定)
```
