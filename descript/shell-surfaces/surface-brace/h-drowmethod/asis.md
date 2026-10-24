# asis

**カテゴリ:** surfaceブレス \> 描画メソッド

[overlay](overlay.md)に近いが、*新規レイヤ*の透過（透過色および、pna・または[seriko.use_self_alpha](../../../shell/descript-txt/seriko.use_self_alpha.md)が設定されている場合は画像自体のアルファチャンネル）を無視して重ねる。<br />
着せ替え・elementでも使用できる。<br />
なおelement合成されたサーフェスを他のサーフェスのアニメーションパーツとしてasisメソッドで合成した場合の表示は未定義であるが、Windows上では普通、透過領域は画像本来の透過色に関係なく黒（#000000）で表示されるだろう。

**対応:** SSP
