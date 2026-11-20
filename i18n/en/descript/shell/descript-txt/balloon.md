# balloon,balloon name

**カテゴリ:** descript.txt

The name of this shell's default balloon. When the user has not explicitly switched balloons, switching to this shell automatically switches to this balloon.<br />
A balloon explicitly selected by the user takes precedence. The ghost's [recommended.balloon](../../ghost/recommended-balloon/recommended.balloon.md) (recommended balloon), if specified, also takes precedence.<br />
This can also be specified in the ghost's descript.txt as [balloon](../../ghost/recommended-balloon/balloon.md) (default balloon). The shell's setting takes precedence if specified; otherwise, the ghost's value is used.<br />
An automatic switch based on the default does not count as an explicit switch by the user. Therefore, switching to another shell switches the balloon again according to that shell's definition.<br />
If multiple balloons are specified, the first one found is used (the [default.balloon.path](default.balloon.path.md) setting is checked first).

**既定値:** The ghost's descript setting

**対応:** SSP
