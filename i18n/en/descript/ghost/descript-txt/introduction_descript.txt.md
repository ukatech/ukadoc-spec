# descript.txt (ghost)

## Overview

The ghost's basic configuration file.<br />
It can configure various information, including the ghost and author names, SHIORI settings, default balloon positions, and icons.

!!! note "Items that can be overridden by the shell's descript.txt"
    Items shared with the shell's `descript.txt` (such as `sakura.name` / `kero.name`, owner draw menu images and colors, balloon and character positions, surface positions, mouse cursors, `don't need ...`, and `shiori.logo.*`) can also be specified in the ghost's `descript.txt`.<br />
    Values specified on the ghost side become defaults for the entire ghost. If the same item is present in the shell's `descript.txt`, the shell's value takes precedence and overrides it.<br />
    These items are listed under [Shell settings](../../shell/descript-txt/index.md). The applicable items are marked as also available in the ghost's descript.txt.

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

type, name, sakuraname, keroname, craftman, and craftmanw are required (some can be omitted in SSP).

When using a SHIORI such as Satori whose DLL is not named "shiori.dll", be sure to specify the DLL name in shiori.

homeurl can be specified in descript.txt or returned in response to a [SHIORI Resource](../../../list/shiori-resource/ghost/homeurl.md) request from the baseware (the method depends on the SHIORI and is omitted here).<br />
Generally, specifying either one is sufficient. If both are specified, take care not to forget to update one when moving the site.

Strings beginning with \\ or % are treated as Sakura Script or environment variable tags and discarded due to security risks. To include them as literal characters, escape them as \\\\ or \\%, respectively.
