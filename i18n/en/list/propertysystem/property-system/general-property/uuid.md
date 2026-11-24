# uuid

**カテゴリ:** Property system \> General property names

The UUID of the target. SSP calculates it from locally available information using the procedure in [metainfo-standard](https://github.com/ukatech/metainfo-standard). It does not access the network.

1. Choose `uuidvalue`.
   - If there is a metainfo folder, use its URL: the value of [metainfo](../../../../descript/ghost/descript-txt/metainfo.md) in descript.txt, or, if absent, the URL derived from [githubrepo](../../../../descript/ghost/descript-txt/githubrepo.md) (assuming `master` is the default branch).
   - Otherwise, use [homeurl](../../../../descript/ghost/descript-txt/homeurl.md) in descript.txt (without URL conversion). Unlike the `homeurl` property, values obtained from var.txt or SHIORI are not used. This avoids using the network or another process and keeps the value stable over time.
   - If that is also absent, use the name (`name`).
2. If descript.txt contains [uuid_base](../../../../descript/ghost/descript-txt/uuid_base.md), append its content to `uuidvalue`.
3. Encode `uuidvalue` as UTF-8 (without appending a newline), compute its MD5 hash, and encode the resulting binary as base64.

For example, the UUID generated from `https://raw.githubusercontent.com/Taromati2/Taromati2/master/.ukagaka/` is `R5dVNluBvKjtQqjP0dAuoA==`.

The metainfo folder is not read, so relocations specified by `jump_to.txt` and past UUIDs are not reflected.<br />
Retrieval fails if `uuidvalue` is empty (there is no name either).

This UUID can be specified instead of a name inside the parentheses of [ghostlist](../ghostlist.md), [balloonlist](../balloonlist.md), and [activeghostlist](../activeghostlist.md). It can also be used to specify an SSTP destination ([ReceiverGhostUUID](../../../../spec/sstp/req_res.md), [IfGhost](../../../../spec/sstp/method_send.md)).

A UUID can also be specified instead of a name in Sakura Script commands that accept ghost, balloon, shell, or plugin names (`\![change,ghost,...]`, `\![call,ghost,...]`, `\![change,shell,...]`, `\![change,balloon,...]`, `\![raiseother,...]`, `\![notifyother,...]`, `\![raiseplugin,...]`, `\![notifyplugin,...]`, `\![timerraiseother,...]`, `\![timernotifyother,...]`, `\![timerraiseplugin,...]`, `\![timernotifyplugin,...]`) and in the `--ghost` startup option. If the value does not match a name or other identifier, it is checked against UUIDs only if it has the UUID format (22 base64 characters followed by `==`).

In the property system, a UUID can also be specified inside the parentheses of `ghostlist`, `balloonlist`, `activeghostlist`, `pluginlist`, `history.ghost`, `history.balloon`, `history.plugin`, and `rateofuselist`. History and usage statistics are recorded internally by name or path, not by UUID (the storage format is unchanged). When a UUID is specified, the installed ghosts and other items are searched for a matching UUID, and that item's record is retrieved.

A UUID can also be specified instead of a name in `balloon` and `recommended.balloon` in a ghost's descript.txt, and `recommended.ghost` in a balloon's descript.txt.

Plugins have both an `id` in descript.txt (a GUID defined by the plugin itself and matched as an ID, as before) and this `uuid`. They are distinct; `id` is not replaced by `uuid`.

**対応:** SSP 2.9.35
