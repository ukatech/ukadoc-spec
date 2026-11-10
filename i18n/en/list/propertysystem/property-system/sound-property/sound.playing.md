# playing

**カテゴリ:** Property System \> Sound Property Names

1 if the target media is playing, or 0 otherwise.<br />
This remains 1 while paused, so combine it with [pause](sound.pause.md) if necessary.<br />
*\[SET enabled\]*Setting 1 has the same effect as [`\![sound,play,～]`](../../../sakura-script/sound/bang-sound-play.md), and setting 0 has the same effect as [`\![sound,stop,～]`](../../../sakura-script/sound/bang-sound-stop.md).<br />
When setting 1 to start playback, the target media's current loop settings and similar options are preserved.

**対応:** SSP 2.8.72
