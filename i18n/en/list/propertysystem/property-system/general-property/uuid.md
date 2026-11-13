# uuid

**カテゴリ:** Property system \> General property names

The target's UUID. SSP calculates it from locally available information using the procedure in [metainfo-standard](https://github.com/ukatech/metainfo-standard). It does not access the network.

1. Select a `uuidvalue`.
   - If there is a metainfo folder, use its URL: the value of [metainfo](../../../../descript/ghost/descript-txt/metainfo.md) in descript.txt, or, if absent, the URL derived from [githubrepo](../../../../descript/ghost/descript-txt/githubrepo.md) (assuming `master` is the default branch).
   - Otherwise, use [homeurl](../../../../descript/ghost/descript-txt/homeurl.md) in descript.txt (without URL conversion). Unlike the `homeurl` property, this does not use values obtained from var.txt or SHIORI. This avoids using the network or another process and ensures that the value does not change over time.
   - If neither is available, use the name (`name`).
2. If descript.txt contains [uuid_base](../../../../descript/ghost/descript-txt/uuid_base.md), append its contents to `uuidvalue`.
3. Encode `uuidvalue` as UTF-8 (without appending a newline), calculate its MD5 hash, and encode the resulting binary as base64.

For example, the UUID generated from `https://raw.githubusercontent.com/Taromati2/Taromati2/master/.ukagaka/` is `R5dVNluBvKjtQqjP0dAuoA==`.

The metainfo folder is not read, so relocations via `jump_to.txt` and past UUIDs are not reflected.<br />
Retrieval fails if `uuidvalue` is empty (there is no name either).

This UUID can be specified in parentheses in [ghostlist](../ghostlist.md), [balloonlist](../balloonlist.md), and [activeghostlist](../activeghostlist.md) instead of the name. It can also be used to specify an SSTP destination ([ReceiverGhostUUID](../../../../spec/sstp/req_res.md), [IfGhost](../../../../spec/sstp/method_send.md)).

A UUID can also be specified instead of a name in Sakura Script commands that accept ghost, balloon, shell, or plugin names (`\![change,ghost,...]`, `\![call,ghost,...]`, `\![change,shell,...]`, `\![change,balloon,...]`, `\![raiseother,...]`, `\![notifyother,...]`, `\![raiseplugin,...]`, `\![notifyplugin,...]`, `\![timerraiseother,...]`, `\![timernotifyother,...]`, `\![timerraiseplugin,...]`, `\![timernotifyplugin,...]`), and in the `--ghost` startup option. If the value does not match a name or similar identifier, it is checked against UUIDs only if it has the UUID format (22 base64 characters followed by `==`).

In the property system, a UUID can also be specified in parentheses in `history.ghost`, `history.balloon`, `history.plugin`, and `rateofuselist`, in addition to `ghostlist`, `balloonlist`, `activeghostlist`, and `pluginlist`. History and usage statistics are recorded internally by name or path, not by UUID (the storage format is unchanged). When queried by UUID, the UUID is resolved to an installed ghost or other item before its records are retrieved.

A UUID can also be specified instead of a name in `balloon` and `recommended.balloon` in a ghost's descript.txt, and in `recommended.ghost` in a balloon's descript.txt.

Plugins have both an `id` in descript.txt (a GUID chosen by the plugin itself, matched as an ID as before) and this `uuid`. They are distinct, and `id` is not replaced by `uuid`.

**対応:** SSP 2.9.35
