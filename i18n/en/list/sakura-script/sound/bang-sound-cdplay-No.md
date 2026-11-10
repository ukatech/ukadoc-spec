# `\![sound,cdplay,トラックNo.]`

**カテゴリ:** Sound command

SSP plays an audio CD. Ignored if no audio CD is loaded.<br />
While playback is in progress, `\_V` is ignored. Specifying another track with `\![sound,cdplay,トラックNo.]` during playback is also ignored. Stop playback with `\![sound,stop]` before specifying the next track.

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![sound,play,test.wav][実行したゴーストのフォルダ]/ghost/masterフォルダにあるtest.wavを再生する。
```
