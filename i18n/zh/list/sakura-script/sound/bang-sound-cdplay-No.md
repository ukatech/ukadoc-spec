# `\![sound,cdplay,トラックNo.]`

**カテゴリ:** 声音命令

由 SSP 播放音乐 CD。若未插入音乐 CD，则忽略此命令。<br />
即使正在播放，`\_V` 也会被忽略。播放期间通过 `\![sound,cdplay,トラックNo.]` 指定其他音轨也会被忽略。请先通过 `\![sound,stop]` 停止播放，再指定下一音轨。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![sound,play,test.wav][実行したゴーストのフォルダ]/ghost/masterフォルダにあるtest.wavを再生する。
```
