# uuid

**カテゴリ:** 属性系统 \> 通用属性名

目标的 UUID。SSP 按照 [metainfo-standard](https://github.com/ukatech/metainfo-standard) 的步骤，仅使用本地信息计算。不进行网络访问。

1. 选择 `uuidvalue`。
   - 如果存在 metainfo 文件夹，则使用其 URL。即 descript.txt 中 [metainfo](../../../../descript/ghost/descript-txt/metainfo.md) 的值；如果没有，则使用从 [githubrepo](../../../../descript/ghost/descript-txt/githubrepo.md) 导出的 URL（默认分支视为 `master`）。
   - 如果没有，则使用 homeurl。采用与 `homeurl` 属性相同的解析方式（按 descript.txt、var.txt、SHIORI 的顺序），不转换 URL。
   - 如果仍没有，则使用名称（`name`）。
2. 如果 descript.txt 中有 [uuid_base](../../../../descript/ghost/descript-txt/uuid_base.md)，则将其内容追加到 `uuidvalue` 之后。
3. 将 `uuidvalue` 转为 UTF-8（末尾不添加换行）并计算 MD5，再将所得二进制数据转为 base64。

例如，从 `https://raw.githubusercontent.com/Taromati2/Taromati2/master/.ukagaka/` 生成的 UUID 为 `R5dVNluBvKjtQqjP0dAuoA==`。

由于不会读取 metainfo 文件夹，因此不会反映 `jump_to.txt` 指定的迁移或过去的 UUID。<br />
如果 `uuidvalue` 为空（也没有名称），则获取失败。

**対応:** SSP 2.9.35
