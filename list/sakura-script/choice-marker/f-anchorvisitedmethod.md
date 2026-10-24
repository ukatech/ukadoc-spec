# `\f[anchorvisitedmethod,描画方法]`

**カテゴリ:** 選択肢マーカー変更コマンド

訪問済みアンカーの描画方法を変更。形状がsquareまたはsquare+underlineの場合のみ有効。<br />
Win32APIのSetROP2関数で使用できる全オペレータが指定可能。<br />
defaultでバルーン設定の標準に戻る。<br />
参考：[SetROP2関数(外部サイト)](https://learn.microsoft.com/ja-jp/windows/win32/api/wingdi/nf-wingdi-setrop2)<br />
※指定は「R2\_」を含まず小文字のモード名。

**対応:** SSP

## 記述例

```sakurascript
\f[anchorvisitedmethod,copypen]\f[anchorvisitedbrushcolor,red]\_a[OnTest]アンカー\_a訪問済みのアンカーの、枠内の描画方法を変更する。copypenの場合、anchorvisitedbrushcolorの色がそのまま描画される。
```
