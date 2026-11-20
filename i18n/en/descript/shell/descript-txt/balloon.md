# balloon,Balloon name

**カテゴリ:** descript.txt

The name of this shell's default balloon. It is a candidate for use when switching to this shell.<br />
The balloon to switch to is determined in the following order, with higher entries taking precedence.

1. The balloon the user last selected while using this shell, if any
2. The ghost's [recommended.balloon](../../ghost/recommended-balloon/recommended.balloon.md) (recommended balloon)
3. This shell's default balloon (this entry)
4. The ghost's [balloon](../../ghost/recommended-balloon/balloon.md) (default balloon)

If none is specified, the balloon does not change when switching shells.<br />
If the balloon determined by entries 2–4 differs from the one currently in use, it is selected.<br />
The history in entry 1 is stored separately for each shell. Switches made through menus or with `\![change,balloon,...]` are recorded. Automatic switches based on default or recommended settings are not recorded, nor are balloon reloads or settings resets (resetting settings clears the history).<br />
If multiple balloons are specified, the first one found is used (the [default.balloon.path](default.balloon.path.md) setting is checked first).

**既定値:** ghost's descript setting

**対応:** SSP
