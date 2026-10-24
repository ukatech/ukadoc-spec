# `\![enter,selectmode,モード(rect),左,上,右,下]\![enter,selectmode,モード(rect),当たり判定名]\![enter,selectmode,モード(rect)]`

**カテゴリ:** 未分類コマンド

選択モードを開始する。実行すると透明部分も表示され、マウスをドラッグすると領域を指定することができる。<br />
実行後、[OnSelectModeBegin](../../shiori-event/select-region-mode/OnSelectModeBegin.md)が実行される。その他OnSelectModeMouseUp、OnSelectModeMouseDown、OnSelectModeCancel、OnSelectModeCompleteも参照。<br />
現在のところ、矩形選択モードを示す "rect" のみを指定可能。また、無指定の場合はrectを指定したのと同じ扱いになる。<br />
モード以降に選択の初期位置を指定可能。座標か、同じ大きさに設定したい当たり判定名を入れる。<br />
このモード中、サーフェスは再描画されない。さくらスクリプト(`\s[ID]`)や着せ替えを行っても描画は変化しないが、反映はされており、`\![leave,selectmode]`時に描画される。

ゴースト終了まで有効。

**対応:** SSP

## 記述例

```sakurascript
\![enter,selectmode,rect,head]セレクトモードを開始する。判定名headの範囲が初期選択されている。
```
