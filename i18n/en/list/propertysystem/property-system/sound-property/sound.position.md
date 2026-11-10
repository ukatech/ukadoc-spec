# position

**カテゴリ:** Property System \> Sound Property Names

The current playback position of the target media, in milliseconds.<br />
Returns -1 for implementations or formats that cannot retrieve the position.<br />
*\[SET enabled\]*Setting this has the same effect as [--seektime=](../../../sakura-script/sound/bang-sound-option.note.md) in [`\![sound,option,～]`](../../../sakura-script/sound/bang-sound-option.md).<br />
The value format is also the same as --seektime=: if it does not contain ":", it is interpreted as an integer in milliseconds; if it contains ":", it is interpreted as \[\[hours:\]minutes:\]seconds\[.milliseconds\]. Prefixing the value with @ makes it relative to the current playback position; negative values can also be specified (for example, @-5000 rewinds by 5 seconds).

**対応:** SSP 2.8.72
