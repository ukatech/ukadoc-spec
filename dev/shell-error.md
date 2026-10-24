# エラーメッセージの解消

## エラーメッセージの解消

開発をしていると、時々SSPがこんなエラーを吐いた、というバグ報告に出くわすことがあります。<br />
ここでは、エラーメッセージの解消方法について、いくつか参考になる情報を列挙しています。<br />
完全に解決するためのマニュアルではありませんが、ちょっとしたヒントになるとは思います。

## 目次

1. [～ 存在していません。](shell-error.md#-存在していません)
2. [旧定義/新定義がどうこう言われた](shell-error.md#旧定義新定義がどうこう言われた)

## ～ 存在していません。

最もよく表示されがちなエラーです。だいたいの場合はアニメーションIDの誤記とか、定義を書き損ねたとか、簡単に修正できる場合が多いのですが、一部対処に悩むものもあります。

### \[GHOST\]default(master) shell 存在していません。

伺かの仕様上、shell/masterフォルダは必ず必要で、無いと互換性の問題が発生します。<br />
ただし、どうしてもmasterシェルを作りたくない場合は、以下の定義で回避できます。

[seriko.defaultsurfacedirectoryname](../descript/ghost/descript-txt/seriko.defaultsurfacedirectoryname.md)

### \[SERIKO\]Surface=0(または10) 存在していません。

伺かの仕様では、0番と10番サーフェスは特殊な扱いで、存在しない番号を`\s`タグで指定した時などに代わりに表示する「デフォルトサーフェス」となります。<br />
0番はともかくとしても、10番を作りたくない場合はそれなりにあると思うので、以下の定義を追加してみてください。

[sakura.seriko.defaultsurface](../descript/ghost/descript-txt/sakura.seriko.defaultsurface.md)

[kero.seriko.defaultsurface](../descript/ghost/descript-txt/kero.seriko.defaultsurface.md)

[char\*.seriko.defaultsurface](../descript/ghost/descript-txt/char-star-.seriko.defaultsurface.md)

## 旧定義/新定義がどうこう言われた

「旧定義を使用しているのに、新しい定義方法が使われている」<br />
「新定義を使用しているのに、旧い定義方法が使われている」<br />
などのようなエラーメッセージに出くわした場合、以下を見てみてください。

[descript - version](../descript/shell-surfaces/descript-brace/version.md)

[SERIKOの旧定義と新定義について](../descript/shell-surfaces/surface-brace/caption_seriko-redefine.md)

場合によっては、以下をsurfaces.txtの一番上に追加するだけでエラーが出なくなる時もあります。

```
descript
{
version,1
}
```
