# metainfo,URL

**カテゴリ:** descript.txt

存放 ghost 資訊的 metainfo 資料夾 URL。[metainfo-standard](https://github.com/ukatech/metainfo-standard) 建議也將此項目寫入 ghost 的 descript.txt 中。<br />
具有 metainfo 資料夾的 ghost 應在此填寫 URL，讓應用程式能從該 ghost 找到 metainfo 資料夾，並[在沒有網路的情況下計算 UUID](../../../list/propertysystem/property-system/general-property/uuid.md)。<br />
UUID 由 URL 字串本身產生。結尾是否有 `/` 或改寫 URL，都會使 UUID 改變。

```txt
metainfo,https://raw.githubusercontent.com/Taromati2/Taromati2/master/.ukagaka/
```

也可以與 [githubrepo](githubrepo.md) 同時填寫。兩者皆存在時，優先使用 `metainfo`。<br />
SSP 不會存取 metainfo 資料夾，只會保留填寫的值。可透過屬性系統的 [metainfo](../../../list/propertysystem/property-system/general-property/metainfo.md) 取得此值。

**既定値:** 無值

**対応:** SSP 2.9.35
