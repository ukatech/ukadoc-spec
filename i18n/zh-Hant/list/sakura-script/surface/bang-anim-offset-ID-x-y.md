# `\![anim,offset,ID,x座標,y座標]`

**カテゴリ:** surface 指令

將 ID 編號的 surface 動畫位置偏移指定的座標。<br />
dressup 也可以一起偏移。

此設定會持續生效，直到變更 surface（執行 `\s[ID]`）為止。

**対応:** SSP

## 記述例

```sakurascript
\s[0]\i[300]長いアニメーションを再生中。\![anim,offset,300,40,50]ここで、アニメーションを右に40pixel下に50pixelずらす。
```
