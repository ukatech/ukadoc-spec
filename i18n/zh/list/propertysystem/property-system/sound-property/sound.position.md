# position

**カテゴリ:** プロパティシステム \> サウンドプロパティ名

目标媒体当前的播放位置，单位为毫秒。<br />
如果实现或格式不支持获取位置，则为 -1。<br />
*\[SET 有效\]*写入 SET 时，效果与[`\![sound,option,～]`](../../../sakura-script/sound/bang-sound-option.md)的[--seektime=](../../../sakura-script/sound/bang-sound-option.note.md)相同。<br />
值的格式也与 --seektime= 相同：不含「:」时按毫秒整数处理，含「:」时按\[\[时:\]分:\]秒\[.毫秒\]处理。开头加 @ 时表示相对于当前播放位置的值，也可以指定负值（例如，@-5000 表示回退 5 秒）。

**対応:** SSP 2.8.72
