# playing

**カテゴリ:** プロパティシステム \> サウンドプロパティ名

如果目标媒体正在播放，则为 1，否则为 0。<br />
暂停期间仍为 1，因此必要时请与[pause](sound.pause.md)配合使用。<br />
*\[SET 有效\]*将 1 写入 SET 时，效果与[`\![sound,play,～]`](../../../sakura-script/sound/bang-sound-play.md)相同；将 0 写入 SET 时，效果与[`\![sound,stop,～]`](../../../sakura-script/sound/bang-sound-stop.md)相同。<br />
将 1 写入 SET 并开始播放时，目标媒体当前的循环设置等会保持不变。

**対応:** SSP 2.8.72
