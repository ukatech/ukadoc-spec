# `\![open,sliderinput,ID,表示時間,現在値,最小,最大,オプション]`

**カテゴリ:** 開啟命令

開啟滑桿調整型的 InputBox。<br />
確定輸入時會觸發 SHIORI 事件[OnUserInput](../../shiori-event/inputbox/OnUserInput.md)，並將輸入值放入 Reference1。<br />
可使用 --option=○○ 的形式指定[※選項](bang-close-textareabox-ID.note.md)。<br />
其他動作與[inputbox](bang-open-inputbox-ID.md)相同。<br />
允許的最小值為 -2147483648，最大值為 2147483647。

**対応:** SSP

## 記述例

```sakurascript
\![open,sliderinput,スライダーテスト,30000,50,0,100]初期値が50、最小値が0、最大が100のスライダー型InputBoxを開く。30秒でタイムアウトする。
```

```sakurascript
\![open,sliderinput,スライダーテスト,--timeout=30000,--text="50,0,100"] 上記と同じ(新オプション指定)
```
