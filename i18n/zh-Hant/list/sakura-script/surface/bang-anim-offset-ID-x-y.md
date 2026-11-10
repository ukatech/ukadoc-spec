# `\![anim,offset,ID,x座標,y座標]`

**カテゴリ:** Surface command

Offset the surface animation with the specified ID by the specified coordinates.<br />
Dressup items can also be shifted.

This remains in effect until the surface changes (execution of `\s[ID]`).

**対応:** SSP

## 記述例

```sakurascript
\s[0]\i[300]長いアニメーションを再生中。\![anim,offset,300,40,50]ここで、アニメーションを右に40pixel下に50pixelずらす。
```
