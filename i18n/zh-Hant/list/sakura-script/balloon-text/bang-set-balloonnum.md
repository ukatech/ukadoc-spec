# `\![set,balloonnum,ファイル名,現在の数,最大数]`

**カテゴリ:** balloon、文字指令

顯示接收檔案時顯示的資料格式。<br />
顯示位置為目前 scope 所屬的 balloon。<br />
各引數皆可省略。要清除時，請省略所有引數或留空。<br />
從 2.6.67 起，也能顯示在 `\1` 側 balloon 及其後的 balloon。

持續有效直到 ghost 結束，或網路更新等原本會使用此區域的功能啟動。

**対応:** SSP

## 記述例

```sakurascript
\![set,balloonnum,テスト表示,1,5]ファイル受信時の表示テスト。\![set,balloonnum,,,]表示内容削除。
```
