# balloon,balloon name

**カテゴリ:** descript.txt

The name of this shell's default balloon. It is a candidate for the balloon to use when switching to this shell.<br />
The balloon to switch to is determined in the following order, with higher entries taking precedence.

1. If the user previously switched balloons while using this shell, that balloon
2. The ghost's [recommended.balloon](../../ghost/recommended-balloon/recommended.balloon.md) (recommended balloon)
3. This shell's default balloon (this entry)
4. The ghost's [balloon](../../ghost/recommended-balloon/balloon.md) (default balloon)

If none is specified, switching shells does not change the balloon.<br />
If the balloon selected by steps 2–4 differs from the current balloon, it is switched to that balloon.<br />
The history in step 1 is retained per shell. Switching via `\![change,balloon,...]` is recorded as well as switching through menus or similar controls. Automatic switches to the default or recommended balloon are not recorded, nor are balloon reloads or settings resets (resetting settings clears the history).<br />
If multiple balloons are specified, the first one found is used (the [default.balloon.path](default.balloon.path.md) specification is checked first).

**既定値:** The ghost's descript setting

**対応:** SSP
