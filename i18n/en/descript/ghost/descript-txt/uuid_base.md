# uuid_base,string

**カテゴリ:** descript.txt

A base string used to prevent UUID collisions. [metainfo-standard](https://github.com/ukatech/metainfo-standard) recommends that ghosts specifying `uuid_base` in the metainfo folder's descript.txt also specify the same value in the ghost's descript.txt.<br />
This string is appended as-is to the string used to generate the UUID, such as the metainfo URL. Specify it in the ghost's descript.txt as well so the UUID can be calculated without network access.

```txt
uuid_base,sample-ghost-1
```

The value can be retrieved through [uuid_base](../../../list/propertysystem/property-system/general-property/uuid_base.md) in the property system.

**既定値:** No value

**対応:** SSP 2.9.35
