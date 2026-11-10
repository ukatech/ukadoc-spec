# surfacetable.txt

## 概要

用于 SSP 开发用调色板的“surface 测试”功能及其他 shell 创建辅助工具的 surface 内容定义文件。

## 基本格式

记述示例

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

以 // 开头的行会被视为注释并完全忽略。

可以使用半角空格和制表符缩进。
