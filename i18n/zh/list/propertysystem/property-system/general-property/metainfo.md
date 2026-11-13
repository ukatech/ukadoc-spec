# metainfo

**カテゴリ:** 属性系统 \> 通用属性名

目标 descript.txt 中记载的 [metainfo](../../../../descript/ghost/descript-txt/metainfo.md) 的值（metainfo 文件夹的 URL）。原样返回记载的字符串。<br />
由于该值从 descript.txt 读取，因此加载 ghost、balloon 列表时即可获取（并非延迟读取）。<br />
如果 descript.txt 中未记载，则获取失败。即使只记载了 `githubrepo`，作为 `metainfo` 获取时仍会失败。

**対応:** SSP 2.9.35
