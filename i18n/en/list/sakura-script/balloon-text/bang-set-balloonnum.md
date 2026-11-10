# `\![set,balloonnum,ファイル名,現在の数,最大数]`

**カテゴリ:** Balloon, text command

Displays the data format shown when receiving a file.<br />
The display target is the balloon belonging to the current scope.<br />
All arguments are optional. To clear the display, omit all arguments or leave them empty.<br />
Since 2.6.67, this can also be displayed in the `\1`-side balloon and beyond.

It remains in effect until the ghost terminates or a feature that normally uses this area, such as a network update, is triggered.

**対応:** SSP

## 記述例

```sakurascript
\![set,balloonnum,テスト表示,1,5]ファイル受信時の表示テスト。\![set,balloonnum,,,]表示内容削除。
```
