# `\![set,alignmenttodesktop,方向]`

**カテゴリ:** surface command

將目前 scope 側的 surface 吸附到桌面指定的方向。方向可指定如下。

- **top**: 吸附到上方。
- **bottom**: 吸附到下方。
- **left**: 吸附到左側。
- **right**: 吸附到右側。
- **free**: 不吸附。
- **osuwari,選項,…**: \[SSP 2.9.33\] 追隨其他視窗（最前面的視窗或指定的視窗）或螢幕的矩形區域（坐下）。選項格式為`--名稱=值`，可用選項有`--target=` `--origin=` `--target-origin=` `--x=` `--y=` `--interval=` `--xmove` `--ymove` `--noclip` `--area=` `--side=` `--margin=` `--zorder=`。所有選項都可省略。詳情請參閱[關於 `\![set,alignmenttodesktop,osuwari]`](bang-set-alignmenttodesktop.note.md)。
- **default**: 恢復 ghost 的預設設定。

吸附到上方或下方時，將無法向上下方向拖曳移動。<br />
吸附到左側或右側時，將無法向左右方向拖曳移動。

在 ghost 結束前有效。

※上述設定也可寫成alignment*on*desktop。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\1\![set,alignmenttodesktop,top]相方側がデスクトップ上部にくっつく。\![set,alignmenttodesktop,default]相方側の吸着が標準設定に戻る。
```

```sakurascript
\0\![set,alignmenttodesktop,osuwari,--target=active,--target-origin=center.top,--xmove,--area=workarea,--side=bottom]前面のウインドウの上端の中央に腰かける（横にだけ動かせる）。座れないときは、ワークエリアの下端に座る。\![set,alignmenttodesktop,default]
```
