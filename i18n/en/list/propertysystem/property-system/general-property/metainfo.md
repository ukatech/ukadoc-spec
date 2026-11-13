# metainfo

**カテゴリ:** Property system \> General property names

The value of [metainfo](../../../../descript/ghost/descript-txt/metainfo.md) in the target's descript.txt (the URL of the metainfo folder). Returns the string as written.<br />
Because the value is read from descript.txt, it is available when the ghost and balloon lists are loaded (it is not loaded lazily).<br />
Retrieval fails if it is not specified in descript.txt. Retrieving `metainfo` also fails if only `githubrepo` is specified.

**対応:** SSP 2.9.35
