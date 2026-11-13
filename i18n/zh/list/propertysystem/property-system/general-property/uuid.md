# uuid

**カテゴリ:** 属性系统 \> 通用属性名

对象的UUID。SSP按照[metainfo-standard](https://github.com/ukatech/metainfo-standard)的步骤，仅根据本地信息计算。不访问网络。

1. 选择`uuidvalue`。
   - 如果有metainfo文件夹，则使用其URL。即descript.txt中的[metainfo](../../../../descript/ghost/descript-txt/metainfo.md)的值；如果没有，则使用从[githubrepo](../../../../descript/ghost/descript-txt/githubrepo.md)导出的URL（默认分支视为`master`）。
   - 如果没有，则使用descript.txt中的[homeurl](../../../../descript/ghost/descript-txt/homeurl.md)（不对URL进行转换）。与`homeurl`属性不同，不使用从var.txt或SHIORI获取的值。这是为了避免使用网络或其他进程，并使值不随时间改变。
   - 如果也没有，则使用名称（`name`）。
2. 如果descript.txt中有[uuid_base](../../../../descript/ghost/descript-txt/uuid_base.md)，则将其内容追加到`uuidvalue`之后。
3. 将`uuidvalue`转换为UTF-8（末尾不添加换行），计算MD5，再将所得二进制数据转换为base64。

例如，从`https://raw.githubusercontent.com/Taromati2/Taromati2/master/.ukagaka/`生成的UUID为`R5dVNluBvKjtQqjP0dAuoA==`。

由于不会读取metainfo文件夹，因此不会反映通过`jump_to.txt`进行的迁移或过去的UUID。<br />
如果`uuidvalue`为空（也没有名称），则获取失败。

在[ghostlist](../ghostlist.md)、[balloonlist](../balloonlist.md)、[activeghostlist](../activeghostlist.md)的括号中，可以填写此UUID代替名称。也可用于指定SSTP的目标（[ReceiverGhostUUID](../../../../spec/sstp/req_res.md)、[IfGhost](../../../../spec/sstp/method_send.md)）。

接受ghost、balloon、shell、plugin名称的Sakura Script（`\![change,ghost,...]`、`\![call,ghost,...]`、`\![change,shell,...]`、`\![change,balloon,...]`、`\![raiseother,...]`、`\![notifyother,...]`、`\![raiseplugin,...]`、`\![notifyplugin,...]`、`\![timerraiseother,...]`、`\![timernotifyother,...]`、`\![timerraiseplugin,...]`、`\![timernotifyplugin,...]`）以及启动选项`--ghost`也可以填写UUID代替名称。当名称等不匹配时，仅对符合UUID形式（22个base64字符加`==`）的值进行匹配。

在属性系统中，除`ghostlist`、`balloonlist`、`activeghostlist`、`pluginlist`外，也可以填写在`history.ghost`、`history.balloon`、`history.plugin`和`rateofuselist`的括号中。历史记录和使用统计在内部按名称或路径记录，并非按UUID记录（保存格式不变）。使用UUID查询时，先将其匹配到已安装的ghost等对象，再查询其记录。

ghost的descript.txt中的`balloon`、`recommended.balloon`以及balloon的descript.txt中的`recommended.ghost`也可以填写UUID代替名称。

plugin同时具有descript.txt中的`id`（plugin自身决定的GUID，仍按以往方式作为ID进行匹配）和此`uuid`。两者不同，`id`不会被`uuid`替代。

**対応:** SSP 2.9.35
