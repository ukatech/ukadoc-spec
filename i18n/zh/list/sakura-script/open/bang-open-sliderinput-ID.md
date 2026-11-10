# `\![open,sliderinput,ID,表示時間,現在値,最小,最大,オプション]`

**カテゴリ:** 打开命令

打开滑块调节式 InputBox。<br />
确认输入时会触发 SHIORI 事件[OnUserInput](../../shiori-event/inputbox/OnUserInput.md)，输入值会放入 Reference1。<br />
可以使用--option=○○的形式指定[※选项](bang-close-textareabox-ID.note.md)。<br />
其他行为与[inputbox](bang-open-inputbox-ID.md)相同。<br />
允许的最小值为-2147483648，最大值为2147483647。

**対応:** SSP

## 記述例

```sakurascript
\![open,sliderinput,スライダーテスト,30000,50,0,100]初期値が50、最小値が0、最大が100のスライダー型InputBoxを開く。30秒でタイムアウトする。
```

```sakurascript
\![open,sliderinput,スライダーテスト,--timeout=30000,--text="50,0,100"] 上記と同じ(新オプション指定)
```
