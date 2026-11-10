# descript.txt (for Ghost)

## 概要

The basic settings file for a ghost.<br />
It can be used to configure various information, including the ghost's name and author's name, SHIORI settings, the balloon's default position, and icons.

## 記述例 and basic usage

```
charset,Shift_JIS
type,ghost
name,凡例さん
sakura.name,凡例さん
kero.name,斑糲岩
homeurl,http://ssp.shillest.net/ukadoc/manual/hogehoge/example/

craftman,ukadog
craftmanw,うか犬
craftmanurl,http://ssp.shillest.net/ukadoc/manual/index.html

shiori,satori.dll
```

type, name, sakuraname, keroname, craftman, and craftmanw are required (some may be omitted when using SSP).

If using SHIORI with a DLL name other than "shiori.dll", such as Satori, be sure to specify the DLL name in shiori.

In addition to specifying homeurl in descript.txt, it can also be set by responding to a [SHIORI Resource](../../../list/shiori-resource/ghost/homeurl.md) request from the baseware (the method depends on SHIORI and is omitted here).<br />
Generally, specifying it in either one location is sufficient. If specifying it in both, take care not to forget to update one when moving the site, for example.

Strings beginning with \\ or % are treated as Sakura Script or environment variable tags and discarded for security reasons. To include them as literal characters, escape them as \\\\ or \\%, for example.
