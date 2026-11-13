# uuid

**カテゴリ:** Property system \> General property names

The target's UUID. SSP calculates it using only locally available information, following the procedure in [metainfo-standard](https://github.com/ukatech/metainfo-standard). It does not access the network.

1. Select `uuidvalue`.
   - If there is a metainfo folder, use its URL: the value of [metainfo](../../../../descript/ghost/descript-txt/metainfo.md) in descript.txt, or, if absent, the URL derived from [githubrepo](../../../../descript/ghost/descript-txt/githubrepo.md) (the default branch is assumed to be `master`).
   - Otherwise, use homeurl. Resolve it in the same way as the `homeurl` property (descript.txt, var.txt, then SHIORI), without converting the URL.
   - If that is also absent, use the name (`name`).
2. If [uuid_base](../../../../descript/ghost/descript-txt/uuid_base.md) is present in descript.txt, append its contents to `uuidvalue`.
3. Encode `uuidvalue` as UTF-8 (without adding a trailing newline), compute its MD5 hash, and encode the resulting binary as base64.

For example, the UUID generated from `https://raw.githubusercontent.com/Taromati2/Taromati2/master/.ukagaka/` is `R5dVNluBvKjtQqjP0dAuoA==`.

Because the metainfo folder is not accessed, relocations via `jump_to.txt` and past UUIDs are not reflected.<br />
Retrieval fails if `uuidvalue` is empty (there is no name either).

**対応:** SSP 2.9.35
