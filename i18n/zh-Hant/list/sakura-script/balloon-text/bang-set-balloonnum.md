# `\![set,balloonnum,ファイル名,現在の数,最大数]`

**カテゴリ:** balloon, text command

Displays the data format shown when receiving a file.<br />
The display destination is the balloon belonging to the current scope.<br />
Each argument is optional. To clear it, omit all arguments or leave them blank.<br />
As of 2.6.67, this can also be displayed in the `\1`-side balloon and subsequent balloons.

It remains in effect until the ghost ends or a feature that normally uses this part, such as network update, is activated.

**対応:** SSP

## 記述例

```sakurascript
\![set,balloonnum,テスト表示,1,5]ファイル受信時の表示テスト。\![set,balloonnum,,,]表示内容削除。
```
