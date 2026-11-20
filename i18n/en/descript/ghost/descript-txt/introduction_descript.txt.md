# descript.txt (ghost)

## Overview

The ghost's basic configuration file.<br />
It can configure various information, including the ghost and author names, SHIORI settings, default balloon positions, and icons.

!!! note "Settings that can be overridden by the shell's descript.txt"
    Settings shared with the shell's `descript.txt` (`sakura.name` / `kero.name`, owner draw menu images and colors, balloon and character positions, surface position information, mouse cursors, `don't need ...`, `shiori.logo.*`, etc.) can also be written in the ghost's `descript.txt`.<br />
    Settings in the ghost file become defaults for the entire ghost. If the same setting exists in the shell's `descript.txt`, the shell setting takes precedence and overrides it.<br />
    These settings are listed under [Shell settings](../../shell/descript-txt/index.md), not on this page. Applicable settings are marked as also available in the ghost's descript.txt.

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

type, name, sakuraname, keroname, craftman, and craftmanw are required (some may be omitted in SSP).

When using a SHIORI such as Satori whose DLL is not named "shiori.dll", remember to specify the DLL name in shiori.

In addition to writing homeurl in descript.txt, it can be set by returning it in response to a [SHIORI Resource](../../../list/shiori-resource/ghost/homeurl.md) request from the baseware (the method depends on the SHIORI and is omitted here).<br />
Generally, specifying it in either place is sufficient. If it is specified in both, take care not to forget to update one of them when the site moves.

Strings beginning with \\ or % are treated as Sakura Script or environment variable tags and discarded due to security risks. To include them as literal characters, escape them as \\\\ or \\%, respectively.
