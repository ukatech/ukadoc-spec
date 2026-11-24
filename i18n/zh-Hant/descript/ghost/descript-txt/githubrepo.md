# githubrepo,URL

**カテゴリ:** descript.txt

ghost 的 GitHub 專案 URL。這是 [metainfo-standard](https://github.com/ukatech/metainfo-standard) 建議也寫入 ghost 的 descript.txt 的項目之一。<br />
與 [metainfo](metainfo.md) 具有相同效果，也可以同時填寫。兩者皆有時，優先使用 `metainfo`。

```txt
githubrepo,https://github.com/Taromati2/Taromati2
```

在 metainfo-standard 中，僅填寫 `githubrepo` 的 ghost，其 metainfo 資料夾被視為位於 `https://github.com/<owner>/<repo>/tree/<default-branch>/.ukagaka`。<br />
SSP 不會透過網路查詢預設分支，因此在[計算 UUID](../../../list/propertysystem/property-system/general-property/uuid.md) 時，會將預設分支視為 `master`，並使用 `https://raw.githubusercontent.com/<owner>/<repo>/master/.ukagaka/` 作為 metainfo 資料夾的 URL。<br />
若儲存庫的預設分支不是 `master`，SSP 計算的 UUID 可能與應用程式計算的 UUID 不一致。這類 ghost 建議也填寫 `metainfo`。

可透過屬性系統的 [githubrepo](../../../list/propertysystem/property-system/general-property/githubrepo.md) 取得此值。

**既定値:** 無值

**対応:** SSP 2.9.35
