# metainfo,URL

**カテゴリ:** descript.txt

The URL of the metainfo folder containing information about the ghost. This is one of the entries that [metainfo-standard](https://github.com/ukatech/metainfo-standard) recommends including in the ghost's descript.txt.<br />
A ghost with a metainfo folder should specify its URL here so that applications can find the folder from the ghost and [calculate its UUID without network access](../../../list/propertysystem/property-system/general-property/uuid.md).<br />
The UUID is generated from the URL string itself. Changing the URL, including adding or removing the trailing `/`, changes the UUID.

```txt
metainfo,https://raw.githubusercontent.com/Taromati2/Taromati2/master/.ukagaka/
```

It may be specified together with [githubrepo](githubrepo.md). If both are present, `metainfo` takes precedence.<br />
SSP does not access the metainfo folder; it only retains the specified value. The value can be retrieved from [metainfo](../../../list/propertysystem/property-system/general-property/metainfo.md) in the property system.

**既定値:** No value

**対応:** SSP 2.9.35
