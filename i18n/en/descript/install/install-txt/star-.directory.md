# \*.directory,directory name

**カテゴリ:** install.txt

The directory name to use after installing the included content. ASCII alphanumeric characters are recommended.<br />
For how to write the \* portion and number multiple items of the same type, see [“Simultaneous installation”](introduction_install_multi.md).<br />
Only a *single-level directory name* can be specified here; path separators are not allowed (they are replaced with “\_”).<br />
This works regardless of the archive's own [type](type.md), but in practice it is used with archives whose type is *ghost* or *shell*.

**既定値:** No behavior

**対応:** SSP
