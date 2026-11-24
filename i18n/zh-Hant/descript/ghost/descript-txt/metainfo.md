# metainfo,URL

**カテゴリ:** descript.txt

存放 ghost 資訊的 metainfo 資料夾 URL。這是 [metainfo-standard](https://github.com/ukatech/metainfo-standard) 建議也寫入 ghost 的 descript.txt 的項目之一。<br />
具有 metainfo 資料夾的 ghost 應在此填寫 URL，讓應用程式能從 ghost 找到 metainfo 資料夾，也能[在沒有網路的情況下計算 UUID](../../../list/propertysystem/property-system/general-property/uuid.md)。<br />
UUID 由 URL 字串本身產生。若改寫 URL，包括末尾是否有 `/`，UUID 也會改變。

```txt
metainfo,https://raw.githubusercontent.com/Taromati2/Taromati2/master/.ukagaka/
```

也可以與 [githubrepo](githubrepo.md) 同時填寫。兩者皆有時，優先使用 `metainfo`。<br />
SSP 不會存取 metainfo 資料夾，只會保留填寫的值。可透過屬性系統的 [metainfo](../../../list/propertysystem/property-system/general-property/metainfo.md) 取得此值。

**既定値:** 無值

**対応:** SSP 2.9.35
