# uuid

**カテゴリ:** 属性系统 \> 通用属性名

对象的 UUID。SSP 按照 [metainfo-standard](https://github.com/ukatech/metainfo-standard) 的步骤，仅使用本地信息计算。不访问网络。

1. 选择 `uuidvalue`。
   - 如果有 metainfo 文件夹，则使用其 URL。即 descript.txt 中的 [metainfo](../../../../descript/ghost/descript-txt/metainfo.md) 的值；如果没有，则使用从 [githubrepo](../../../../descript/ghost/descript-txt/githubrepo.md) 推导出的 URL（默认分支视为 `master`）。
   - 如果没有，则使用 descript.txt 中的 [homeurl](../../../../descript/ghost/descript-txt/homeurl.md)（不进行 URL 转换）。与 `homeurl` 属性不同，不使用从 var.txt 或 SHIORI 获取的值。这是为了不使用网络或其他进程，并确保值不会随时间变化。
   - 如果仍然没有，则使用名称（`name`）。
2. 如果 descript.txt 中有 [uuid_base](../../../../descript/ghost/descript-txt/uuid_base.md)，则将其内容追加到 `uuidvalue` 之后。
3. 将 `uuidvalue` 转为 UTF-8（末尾不追加换行），计算 MD5，再将得到的二进制数据转换为 base64。

例如，从 `https://raw.githubusercontent.com/Taromati2/Taromati2/master/.ukagaka/` 生成的 UUID 为 `R5dVNluBvKjtQqjP0dAuoA==`。

由于不会读取 metainfo 文件夹，因此不会反映通过 `jump_to.txt` 进行的迁移或过去的 UUID。<br />
如果 `uuidvalue` 为空（也没有名称），则获取失败。

在[ghostlist](../ghostlist.md)、[balloonlist](../balloonlist.md)、[activeghostlist](../activeghostlist.md)的括号中，可以使用此UUID代替名称。也可以用于指定SSTP的接收目标（[ReceiverGhostUUID](../../../../spec/sstp/req_res.md)、[IfGhost](../../../../spec/sstp/method_send.md)）。

**対応:** SSP 2.9.35
