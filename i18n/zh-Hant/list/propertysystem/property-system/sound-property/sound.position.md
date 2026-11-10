# position

**カテゴリ:** Property system \> Sound property name

The current playback position of the target media, in milliseconds.<br />
Returns -1 for implementations or formats that cannot retrieve the position.<br />
*\[SET enabled\]* When SET, has the same effect as [`\![sound,option,～]`](../../../sakura-script/sound/bang-sound-option.md) [--seektime=](../../../sakura-script/sound/bang-sound-option.note.md).<br />
The value format is also the same as --seektime=. If it does not contain ":", it is interpreted as an integer in milliseconds; if it contains ":", it is interpreted as \[\[hour:\]minute:\]second\[.millisecond\]. Prefixing the value with @ specifies a position relative to the current playback position, and negative values can also be specified (e.g., @-5000 rewinds by 5 seconds).

**対応:** SSP 2.8.72
