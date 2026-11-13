# githubrepo,URL

**カテゴリ:** descript.txt

The URL of the ghost's GitHub project. This is one of the entries that [metainfo-standard](https://github.com/ukatech/metainfo-standard) recommends adding to the ghost's descript.txt as well.<br />
It has the same effect as [metainfo](metainfo.md), and both may be specified. If both are present, `metainfo` takes precedence.

```txt
githubrepo,https://github.com/Taromati2/Taromati2
```

In metainfo-standard, the metainfo folder of a ghost that specifies only `githubrepo` is assumed to be at `https://github.com/<owner>/<repo>/tree/<default-branch>/.ukagaka`.<br />
SSP does not make a network request to determine the default branch, so when [calculating the UUID](../../../list/propertysystem/property-system/general-property/uuid.md), it assumes the default branch is `master` and uses `https://raw.githubusercontent.com/<owner>/<repo>/master/.ukagaka/` as the metainfo folder URL.<br />
For repositories whose default branch is not `master`, the UUID calculated by SSP may differ from the UUID expected by an application. Such ghosts should also specify `metainfo`.

The value can be retrieved through the property system's [githubrepo](../../../list/propertysystem/property-system/general-property/githubrepo.md) property.

**既定値:** No value

**対応:** SSP 2.9.35
