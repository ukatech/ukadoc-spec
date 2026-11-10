# `\![set,alignmenttodesktop,方向]`

**カテゴリ:** surface 命令

将当前 scope 一侧的 surface 吸附到桌面的指定方向。方向可按以下方式指定。

- **top**: 吸附到顶部。
- **bottom**: 吸附到底部。
- **left**: 吸附到左侧。
- **right**: 吸附到右侧。
- **free**: 不吸附。
- **osuwari,オプション,…**: \[SSP 2.9.33\] 跟随其他窗口（前景窗口或指定窗口）或屏幕矩形（坐靠）。选项采用`--名称=值`的形式，可用选项有`--target=` `--origin=` `--target-origin=` `--x=` `--y=` `--interval=` `--xmove` `--ymove` `--noclip` `--area=` `--side=` `--margin=` `--zorder=`。所有选项都可以省略。详情请参阅[关于`\![set,alignmenttodesktop,osuwari]`](bang-set-alignmenttodesktop.note.md)。
- **default**: 恢复 ghost 的默认设置。

吸附到顶部或底部时，无法向上下方向拖动。<br />
吸附到左侧或右侧时，无法向左右方向拖动。

在 ghost 结束前有效。

※也可以写作alignment*on*desktop，效果相同。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\1\![set,alignmenttodesktop,top]相方側がデスクトップ上部にくっつく。\![set,alignmenttodesktop,default]相方側の吸着が標準設定に戻る。
```

```sakurascript
\0\![set,alignmenttodesktop,osuwari,--target=active,--target-origin=center.top,--xmove,--area=workarea,--side=bottom]前面のウインドウの上端の中央に腰かける（横にだけ動かせる）。座れないときは、ワークエリアの下端に座る。\![set,alignmenttodesktop,default]
```
