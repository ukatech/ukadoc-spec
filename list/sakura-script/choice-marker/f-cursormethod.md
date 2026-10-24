# `\f[cursormethod,描画方法]`

**カテゴリ:** 選択肢マーカー変更コマンド

選択中マーカー描画方法を変更。形状がsquareまたはsquare+underlineの場合のみ有効。<br />
Win32APIのSetROP2関数で使用できる全オペレータが指定可能。<br />
defaultでバルーン設定の標準に戻る。<br />
参考：[SetROP2関数(外部サイト)](http://msdn.microsoft.com/ja-jp/library/cc428718.aspx)<br />
※指定は「R2\_」を含まず小文字のモード名。例：notmaskpen

**対応:** SSP

## 記述例

```sakurascript
\f[cursormethod,copypen]\f[cursorbrushcolor,red]\q[選択肢,OnTest]選択中の選択肢の、枠内の描画方法を変更する。copypenの場合、cursorbrushcolorの色がそのまま描画される。
```
