# `\![sound,cdplay,トラックNo.]`

**カテゴリ:** Sound command

SSP plays an audio CD. If no audio CD is loaded, the command is ignored.<br />
`\_V` is ignored during playback. Specifying another track with `\![sound,cdplay,トラックNo.]` during playback is also ignored. Stop playback with `\![sound,stop]` before specifying the next track.

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![sound,play,test.wav][実行したゴーストのフォルダ]/ghost/masterフォルダにあるtest.wavを再生する。
```
