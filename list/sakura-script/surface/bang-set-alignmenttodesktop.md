# `\![set,alignmenttodesktop,方向]`

**カテゴリ:** サーフェスコマンド

現スコープ側サーフェスをデスクトップの指定した方向に吸着。方向は以下の方法が指定可能。

- **top**: 上部に吸着。
- **bottom**: 下部に吸着。
- **left**: 左部に吸着。
- **right**: 右部に吸着。
- **free**: 吸着なし。
- **osuwari,オプション,…**: \[SSP 2.9.33\] 他のウインドウ（前面のウインドウ・指定したウインドウ）や画面の矩形に追尾する（お座り）。オプションは`--名前=値`の形で、`--target=` `--origin=` `--target-origin=` `--x=` `--y=` `--interval=` `--xmove` `--ymove` `--noclip` `--area=` `--side=` `--margin=` `--zorder=`がある。すべて省略できる。詳しくは[`\![set,alignmenttodesktop,osuwari]`について](bang-set-alignmenttodesktop.note.md)。
- **default**: ゴーストのデフォルト設定に戻す。

上または下に吸着した場合、上下方向へのドラッグ移動ができなくなる。<br />
左または右に吸着した場合、左右方向へのドラッグ移動ができなくなる。

ゴースト終了まで有効。

※上記はalignment*on*desktopと書いても有効。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\1\![set,alignmenttodesktop,top]相方側がデスクトップ上部にくっつく。\![set,alignmenttodesktop,default]相方側の吸着が標準設定に戻る。
```

```sakurascript
\0\![set,alignmenttodesktop,osuwari,--target=active,--target-origin=center.top,--xmove,--area=workarea,--side=bottom]前面のウインドウの上端の中央に腰かける（横にだけ動かせる）。座れないときは、ワークエリアの下端に座る。\![set,alignmenttodesktop,default]
```
