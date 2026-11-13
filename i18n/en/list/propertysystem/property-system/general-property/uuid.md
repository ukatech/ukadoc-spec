# uuid

**カテゴリ:** Property system \> General property name

The target's UUID. SSP calculates it using only locally available information, following the [metainfo-standard](https://github.com/ukatech/metainfo-standard) procedure. It does not access the network.

1. Select `uuidvalue`.
   - If there is a metainfo folder, use its URL: the value of [metainfo](../../../../descript/ghost/descript-txt/metainfo.md) in descript.txt, or, if absent, the URL derived from [githubrepo](../../../../descript/ghost/descript-txt/githubrepo.md) (assuming the default branch is `master`).
   - Otherwise, use [homeurl](../../../../descript/ghost/descript-txt/homeurl.md) in descript.txt (without URL conversion). Unlike the `homeurl` property, values obtained from var.txt or SHIORI are not used. This avoids using the network or another process and keeps the value from changing over time.
   - If that is also absent, use the name (`name`).
2. If [uuid_base](../../../../descript/ghost/descript-txt/uuid_base.md) is present in descript.txt, append its contents to `uuidvalue`.
3. Encode `uuidvalue` as UTF-8 (without adding a trailing newline), calculate its MD5 hash, and encode the resulting binary in base64.

For example, the UUID generated from `https://raw.githubusercontent.com/Taromati2/Taromati2/master/.ukagaka/` is `R5dVNluBvKjtQqjP0dAuoA==`.

The metainfo folder is not read, so relocations via `jump_to.txt` and past UUIDs are not reflected.<br />
If `uuidvalue` is empty (there is no name either), retrieval fails.

In the parentheses of [ghostlist](../ghostlist.md), [balloonlist](../balloonlist.md), and [activeghostlist](../activeghostlist.md), this UUID can be specified instead of a name. It can also be used to specify an SSTP recipient ([ReceiverGhostUUID](../../../../spec/sstp/req_res.md), [IfGhost](../../../../spec/sstp/method_send.md)).

**対応:** SSP 2.9.35
