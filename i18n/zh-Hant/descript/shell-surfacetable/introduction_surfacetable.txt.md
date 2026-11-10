# surfacetable.txt

## 概要

這是定義 surface 內容的檔案，供 SSP 開發用調色盤的「サーフィステスト」功能，以及其他 shell 製作輔助工具使用。

## 基本格式

記述例

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

以 // 開頭的行會視為註解，並完全忽略。

可以使用半形空格和定位字元縮排。
