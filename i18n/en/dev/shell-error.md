# Resolving Error Messages

## Resolving Error Messages

During development, you may occasionally encounter bug reports saying that SSP produced an error like this.<br />
This page lists some information that may help resolve error messages.<br />
This is not a manual for completely resolving every issue, but it may provide a few helpful hints.

## 目次

1. [～ Does not exist.](shell-error.md#-存在していません)
2. [Messages about old and new definitions](shell-error.md#旧定義新定義がどうこう言われた)

## ～ Does not exist.

This is the error that appears most often. In most cases, it is caused by a typo in an animation ID or a missing definition, and is easy to fix, but some cases can be difficult to handle.

### \[GHOST\]default(master) shell does not exist.

Under the Ukagaka specifications, the shell/master folder is required, and omitting it causes compatibility issues.<br />
However, if you really do not want to create a master shell, you can work around this with the following definition.

[seriko.defaultsurfacedirectoryname](../descript/ghost/descript-txt/seriko.defaultsurfacedirectoryname.md)

### \[SERIKO\]Surface=0(or 10) does not exist.

Under the Ukagaka specifications, surfaces 0 and 10 are treated specially and serve as the "default surfaces" displayed when, for example, a nonexistent number is specified with the `\s` tag.<br />
You may have reasons not to create surface 10, even if you create surface 0, so try adding the following definitions.

[sakura.seriko.defaultsurface](../descript/ghost/descript-txt/sakura.seriko.defaultsurface.md)

[kero.seriko.defaultsurface](../descript/ghost/descript-txt/kero.seriko.defaultsurface.md)

[char\*.seriko.defaultsurface](../descript/ghost/descript-txt/char-star-.seriko.defaultsurface.md)

## Messages about old and new definitions

"An old definition is being used, but the new definition method is in use."<br />
"A new definition is being used, but the old definition method is in use."<br />
If you encounter an error message like these, check the following.

[descript - version](../descript/shell-surfaces/descript-brace/version.md)

[About old and new SERIKO definitions](../descript/shell-surfaces/surface-brace/caption_seriko-redefine.md)

In some cases, adding the following to the top of surfaces.txt may make the error go away.

```
descript
{
version,1
}
```
