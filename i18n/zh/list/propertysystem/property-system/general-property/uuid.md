# uuid

**カテゴリ:** 属性系统 \> 通用属性名

目标的 UUID。SSP 按照 [metainfo-standard](https://github.com/ukatech/metainfo-standard) 的步骤，仅使用本地信息计算，不进行网络访问。

1. 选择`uuidvalue`。
   - 如果有 metainfo 文件夹，则使用其 URL。即 descript.txt 中 [metainfo](../../../../descript/ghost/descript-txt/metainfo.md) 的值；若不存在，则使用从 [githubrepo](../../../../descript/ghost/descript-txt/githubrepo.md) 导出的 URL（默认分支视为 `master`）。
   - 若不存在，则使用 descript.txt 中的 [homeurl](../../../../descript/ghost/descript-txt/homeurl.md)（不进行 URL 转换）。与`homeurl`属性不同，不使用从 var.txt 或 SHIORI 获取的值。这是为了不使用网络或其他进程，并确保值不会随时间变化。
   - 若仍不存在，则使用名称（`name`）。
2. 如果 descript.txt 中有 [uuid_base](../../../../descript/ghost/descript-txt/uuid_base.md)，则将其内容追加到`uuidvalue`之后。
3. 将`uuidvalue`编码为 UTF-8（末尾不添加换行符）并计算 MD5，再将所得二进制数据转换为 base64。

例如，由`https://raw.githubusercontent.com/Taromati2/Taromati2/master/.ukagaka/`生成的 UUID 是`R5dVNluBvKjtQqjP0dAuoA==`。

由于不会读取 metainfo 文件夹，因此不会反映通过`jump_to.txt`进行的迁移或过去的 UUID。<br />
如果`uuidvalue`为空（也没有名称），则获取失败。

在 [ghostlist](../ghostlist.md)、[balloonlist](../balloonlist.md) 和 [activeghostlist](../activeghostlist.md) 的括号中，可以用此 UUID 代替名称。也可用于指定 SSTP 目标（[ReceiverGhostUUID](../../../../spec/sstp/req_res.md)、[IfGhost](../../../../spec/sstp/method_send.md)）。

接收 ghost、balloon、shell 或 plugin 名称的 Sakura Script（`\![change,ghost,...]`、`\![call,ghost,...]`、`\![change,shell,...]`、`\![change,balloon,...]`、`\![raiseother,...]`、`\![notifyother,...]`、`\![raiseplugin,...]`、`\![notifyplugin,...]`、`\![timerraiseother,...]`、`\![timernotifyother,...]`、`\![timerraiseplugin,...]`、`\![timernotifyplugin,...]`）以及启动选项`--ghost`，也可以用 UUID 代替名称。与名称等不匹配时，仅对符合 UUID 格式（base64 的 22 个字符加`==`）的值进行匹配。

在属性系统中，除了`ghostlist`、`balloonlist`、`activeghostlist`和`pluginlist`，也可以写在`history.ghost`、`history.balloon`、`history.plugin`和`rateofuselist`的括号中。历史记录和使用统计在内部按名称或路径记录，并非按 UUID 记录（保存格式不变）。指定 UUID 时，会从已安装的 ghost 等对象中查找 UUID 匹配的对象，并获取其记录。

ghost 的 descript.txt 中的`balloon`、`recommended.balloon`以及 balloon 的 descript.txt 中的`recommended.ghost`，也可以用 UUID 代替名称。

plugin 同时具有 descript.txt 中的`id`（由 plugin 自行决定的 GUID，仍按以往方式作为 ID 进行匹配）和此`uuid`。两者不同，`id`不会被`uuid`取代。

**対応:** SSP 2.9.35
