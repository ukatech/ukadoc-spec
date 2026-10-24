# `\![sound,cdplay,トラックNo.]`

**カテゴリ:** サウンドコマンド

音楽CDをSSPが再生する。音楽CDがセットされていない場合は無視される。<br />
再生中でも、`\_V`は無視される。再生中に`\![sound,cdplay,トラックNo.]`で別トラックを指定しても無視される。`\![sound,stop]`で一旦停止してから次のトラックを指定すること。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![sound,play,test.wav][実行したゴーストのフォルダ]/ghost/masterフォルダにあるtest.wavを再生する。
```
