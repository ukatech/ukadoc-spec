# `\![sound,cdplay,トラックNo.]`

**カテゴリ:** 音效指令

由 SSP 播放音樂 CD。若未放入音樂 CD，則會忽略此指令。<br />
即使正在播放，`\_V` 也會被忽略。播放期間使用 `\![sound,cdplay,トラックNo.]` 指定其他曲目，也會被忽略。請先使用 `\![sound,stop]` 停止播放，再指定下一首曲目。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![sound,play,test.wav][実行したゴーストのフォルダ]/ghost/masterフォルダにあるtest.wavを再生する。
```
