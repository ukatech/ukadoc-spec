# `\![set,alignmenttodesktop,方向]`

**カテゴリ:** Surface command

Snap the current scope's surface to the specified side of the desktop. The direction can be specified using one of the following options.

- **top**: Snap to the top.
- **bottom**: Snap to the bottom.
- **left**: Snap to the left.
- **right**: Snap to the right.
- **free**: Do not snap.
- **osuwari,オプション,…**: \[SSP 2.9.33\] Follow another window (the foreground window or a specified window) or the screen rectangle (sit down). Options take the form `--name=value`; available options are `--target=` `--origin=` `--target-origin=` `--x=` `--y=` `--interval=` `--xmove` `--ymove` `--noclip` `--area=` `--side=` `--margin=` `--zorder=`. All options are optional. See [about `\![set,alignmenttodesktop,osuwari]`](bang-set-alignmenttodesktop.note.md).
- **default**: Restore the ghost's default setting.

When snapped to the top or bottom, dragging in the vertical direction is disabled.<br />
When snapped to the left or right, dragging in the horizontal direction is disabled.

Effective until the ghost ends.

※The above also works when written as alignment*on*desktop.

**対応:** SSP / Ninix

## 記述例

```sakurascript
\1\![set,alignmenttodesktop,top]相方側がデスクトップ上部にくっつく。\![set,alignmenttodesktop,default]相方側の吸着が標準設定に戻る。
```

```sakurascript
\0\![set,alignmenttodesktop,osuwari,--target=active,--target-origin=center.top,--xmove,--area=workarea,--side=bottom]前面のウインドウの上端の中央に腰かける（横にだけ動かせる）。座れないときは、ワークエリアの下端に座る。\![set,alignmenttodesktop,default]
```
