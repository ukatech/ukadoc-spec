# metainfo,URL

**カテゴリ:** descript.txt

存放 ghost 信息的 metainfo 文件夹的 URL。[metainfo-standard](https://github.com/ukatech/metainfo-standard) 建议也将此条目写入 ghost 的 descript.txt。<br />
有 metainfo 文件夹的 ghost 应在此填写 URL，以便应用程序从该 ghost 找到 metainfo 文件夹，并[在没有网络的情况下计算 UUID](../../../list/propertysystem/property-system/general-property/uuid.md)。<br />
UUID 由 URL 字符串本身生成。末尾是否有 `/` 或 URL 被改写都会导致 UUID 变化。

```txt
metainfo,https://raw.githubusercontent.com/Taromati2/Taromati2/master/.ukagaka/
```

可以与 [githubrepo](githubrepo.md) 同时填写。两者都存在时优先使用 `metainfo`。<br />
SSP 不会访问 metainfo 文件夹，只会保留填写的值。可通过属性系统的 [metainfo](../../../list/propertysystem/property-system/general-property/metainfo.md) 获取该值。

**既定値:** 无值

**対応:** SSP 2.9.35
