# playing

**カテゴリ:** 屬性系統 \> 聲音屬性名稱

目標媒體正在播放時為 1，否則為 0。<br />
暫停時仍會維持為 1，因此必要時請搭配[pause](sound.pause.md)使用。<br />
*\[SET 有效\]*將 1 設為 SET 時，效果與[`\![sound,play,～]`](../../../sakura-script/sound/bang-sound-play.md)相同；將 0 設為 SET 時，效果與[`\![sound,stop,～]`](../../../sakura-script/sound/bang-sound-stop.md)相同。<br />
將 1 設為 SET 以開始播放時，目標媒體目前的循環設定等會維持不變。

**対応:** SSP 2.8.72
