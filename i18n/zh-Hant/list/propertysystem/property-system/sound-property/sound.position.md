# position

**カテゴリ:** 屬性系統 \> 聲音屬性名稱

目標媒體目前的播放位置，單位為毫秒。<br />
若實作或格式無法取得位置，則為 -1。<br />
*\[SET 有效\]*設為 SET 時，效果與[`\![sound,option,～]`](../../../sakura-script/sound/bang-sound-option.md)的[--seektime=](../../../sakura-script/sound/bang-sound-option.note.md)相同。<br />
值的格式也與 --seektime= 相同；不含「:」時會解讀為毫秒單位的整數，含「:」時則會解讀為\[\[時:\]分:\]秒\[.毫秒\]。開頭加上 @ 時，會指定相對於目前播放位置的位置，也可以指定負值（例如：@-5000 會倒轉 5 秒）。

**対応:** SSP 2.8.72
