# playing

**カテゴリ:** プロパティシステム \> サウンドプロパティ名

対象のメディアが再生中なら1、さもなくば0。<br />
一時停止中も1のままなので、必要なら[pause](sound.pause.md)と併用する。<br />
*\[SET有効\]*1をSETすると[`\![sound,play,～]`](../../../sakura-script/sound/bang-sound-play.md)、0をSETすると[`\![sound,stop,～]`](../../../sakura-script/sound/bang-sound-stop.md)と同じ効果。<br />
1をSETして再生を開始する場合、対象のメディアの現在のループ指定などはそのまま維持される。

**対応:** SSP 2.8.72
