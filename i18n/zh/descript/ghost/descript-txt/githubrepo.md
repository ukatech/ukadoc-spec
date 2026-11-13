# githubrepo,URL

**カテゴリ:** descript.txt

ghost 的 GitHub 项目 URL。[metainfo-standard](https://github.com/ukatech/metainfo-standard) 建议也在 ghost 的 descript.txt 中填写的条目之一。<br />
与 [metainfo](metainfo.md) 具有相同效果，可以同时填写。两者都存在时优先使用 `metainfo`。

```txt
githubrepo,https://github.com/Taromati2/Taromati2
```

在 metainfo-standard 中，仅填写了 `githubrepo` 的 ghost 的 metainfo 文件夹被视为位于 `https://github.com/<owner>/<repo>/tree/<default-branch>/.ukagaka`。<br />
SSP 不会通过网络访问查询默认分支，因此在[计算 UUID](../../../list/propertysystem/property-system/general-property/uuid.md) 时，将默认分支视为 `master`，并使用 `https://raw.githubusercontent.com/<owner>/<repo>/master/.ukagaka/` 作为 metainfo 文件夹的 URL。<br />
对于默认分支不是 `master` 的仓库，SSP 计算的 UUID 可能与应用程序求得的 UUID 不一致。此类 ghost 最好也填写 `metainfo`。

可通过属性系统的 [githubrepo](../../../list/propertysystem/property-system/general-property/githubrepo.md) 获取该值。

**既定値:** 无值

**対応:** SSP 2.9.35
