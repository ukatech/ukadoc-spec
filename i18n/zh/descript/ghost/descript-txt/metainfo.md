# metainfo,URL

**カテゴリ:** descript.txt

存放 ghost 信息的 metainfo 文件夹的 URL。[metainfo-standard](https://github.com/ukatech/metainfo-standard) 建议在 ghost 的 descript.txt 中也填写此项。<br />
拥有 metainfo 文件夹的 ghost 应在此填写 URL，以便应用程序从该 ghost 找到 metainfo 文件夹，并[无需网络即可计算 UUID](../../../list/propertysystem/property-system/general-property/uuid.md)。<br />
UUID 由 URL 字符串本身生成。修改 URL，包括增删末尾的 `/`，都会改变 UUID。

```txt
metainfo,https://raw.githubusercontent.com/Taromati2/Taromati2/master/.ukagaka/
```

可以与 [githubrepo](githubrepo.md) 同时填写。两者都存在时优先使用 `metainfo`。<br />
SSP 不会访问 metainfo 文件夹，只会保留所填写的值。可通过属性系统的 [metainfo](../../../list/propertysystem/property-system/general-property/metainfo.md) 获取该值。

**既定値:** 无值

**対応:** SSP 2.9.35
