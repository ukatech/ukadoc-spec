# uuid_base,字串

**カテゴリ:** descript.txt

用來防止 UUID 衝突的基礎字串。[metainfo-standard](https://github.com/ukatech/metainfo-standard) 建議，在 metainfo 資料夾的 descript.txt 中填寫了 `uuid_base` 的 ghost，也在 ghost 的 descript.txt 中填寫相同的值。<br />
此字串會原樣附加到作為 UUID 來源的字串（例如 metainfo 的 URL）之後。為了能在沒有網路的情況下計算 UUID，也應在 ghost 中填寫此值。

```txt
uuid_base,sample-ghost-1
```

可透過屬性系統的 [uuid_base](../../../list/propertysystem/property-system/general-property/uuid_base.md) 取得此值。

**既定値:** 無值

**対応:** SSP 2.9.35
