# `\![sound,stop,ファイル名]`

**カテゴリ:** Sound commands

Completely stops playback. Unlike pause, this releases the audio data and stops playback completely. In some cases, another audio file cannot be played unless this command is used to stop playback.<br />
If the filename is omitted, stops all currently playing sounds.

**対応:** SSP

## 記述例

```sakurascript
\![sound,loop,test.wav][実行したゴーストのフォルダ]/ghost/masterフォルダにあるtest.wavを再生する。\![sound,stop]再生を完全に停止する。
```
