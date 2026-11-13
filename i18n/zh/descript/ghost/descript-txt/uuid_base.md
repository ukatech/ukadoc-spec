# uuid_base,字符串

**カテゴリ:** descript.txt

用于防止 UUID 冲突的基础字符串。[metainfo-standard](https://github.com/ukatech/metainfo-standard) 建议在 metainfo 文件夹的 descript.txt 中填写了 `uuid_base` 的 ghost，也在 ghost 的 descript.txt 中填写相同的值。<br />
该字符串会原样追加到生成 UUID 的源字符串（如 metainfo 的 URL）之后。为了能够在没有网络的情况下计算 UUID，也应在 ghost 中填写该值。

```txt
uuid_base,sample-ghost-1
```

可通过属性系统的 [uuid_base](../../../list/propertysystem/property-system/general-property/uuid_base.md) 获取该值。

**既定値:** 无值

**対応:** SSP 2.9.35
