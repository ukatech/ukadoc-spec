# Resolving error messages

## Resolving error messages

During development, you may occasionally encounter a bug report saying that SSP produced an error.<br />
This page lists some useful information on resolving error messages.<br />
It is not a complete troubleshooting manual, but it may provide some helpful hints.

## 目次

1. [～ does not exist.](shell-error.md#-存在していません)
2. [Errors about old and new definitions](shell-error.md#旧定義新定義がどうこう言われた)

## ～ does not exist.

This is one of the most common errors. In most cases, it is easy to fix, such as when an animation ID is mistyped or a definition is missing, but some cases are harder to resolve.

### \[GHOST\]default(master) shell does not exist.

The Ukagaka specification requires a shell/master folder; its absence causes compatibility problems.<br />
However, if you do not want to create a master shell, you can work around this with the following definition.

[seriko.defaultsurfacedirectoryname](../descript/ghost/descript-txt/seriko.defaultsurfacedirectoryname.md)

### \[SERIKO\]Surface=0(or 10) does not exist.

In the Ukagaka specification, surfaces 0 and 10 are treated specially as default surfaces, displayed when, for example, a nonexistent number is specified with the `\s` tag.<br />
Although surface 0 is generally needed, you may not want to create surface 10. In that case, try adding the following definitions.

[sakura.seriko.defaultsurface](../descript/shell/descript-txt/sakura.seriko.defaultsurface.md)

[kero.seriko.defaultsurface](../descript/shell/descript-txt/kero.seriko.defaultsurface.md)

[char\*.seriko.defaultsurface](../descript/shell/descript-txt/char-star-.seriko.defaultsurface.md)

## Errors about old and new definitions

"The new definition format is being used while old definitions are in use."<br />
"The old definition format is being used while new definitions are in use."<br />
If you encounter an error message like these, see the following.

[descript - version](../descript/shell-surfaces/descript-brace/version.md)

[Old and new SERIKO definitions](../descript/shell-surfaces/surface-brace/caption_seriko-redefine.md)

In some cases, simply adding the following to the top of surfaces.txt will eliminate the error.

```
descript
{
version,1
}
```
