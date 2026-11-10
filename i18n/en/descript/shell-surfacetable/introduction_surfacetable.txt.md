# surfacetable.txt

## Overview

A surface definition file intended for use with the “Surface Test” feature in the SSP development palette and other shell-authoring utilities.

## Basic syntax

Example

```
charset,Shift_JIS
version,1
option,DisableNoDefineSurfaces

//==========パーツ==========
group,__disabled
{
	19,__parts
}

//==========クー==========
group,[空]平日
{
	scope,0
	
	0,素
	1,照れ
	3,不安
	4,はぅー
	5,笑
}
```

Lines beginning with // are treated as comments and ignored completely.

Indentation with spaces or tabs is allowed.
