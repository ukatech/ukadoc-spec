# uuid

**カテゴリ:** Property system \> General property names

The UUID of the target. SSP calculates it from locally available information using the [metainfo-standard](https://github.com/ukatech/metainfo-standard) procedure. It does not access the network.

1. Select `uuidvalue`.
   - If there is a metainfo folder, use its URL: the value of [metainfo](../../../../descript/ghost/descript-txt/metainfo.md) in descript.txt, or, if absent, the URL derived from [githubrepo](../../../../descript/ghost/descript-txt/githubrepo.md) (assuming `master` as the default branch).
   - Otherwise, use [homeurl](../../../../descript/ghost/descript-txt/homeurl.md) in descript.txt (without URL conversion). Unlike the `homeurl` property, values obtained from var.txt or SHIORI are not used. This avoids using the network or another process and keeps the value stable over time.
   - If that is also absent, use the name (`name`).
2. If [uuid_base](../../../../descript/ghost/descript-txt/uuid_base.md) is present in descript.txt, append its content to `uuidvalue`.
3. Encode `uuidvalue` as UTF-8 (without adding a trailing newline), compute its MD5 hash, and encode the resulting binary as base64.

For example, the UUID generated from `https://raw.githubusercontent.com/Taromati2/Taromati2/master/.ukagaka/` is `R5dVNluBvKjtQqjP0dAuoA==`.

The metainfo folder is not read, so relocations specified by `jump_to.txt` and past UUIDs are not reflected.<br />
Retrieval fails if `uuidvalue` is empty (the name is also absent).

**対応:** SSP 2.9.35
