# githubrepo,URL

**カテゴリ:** descript.txt

ゴーストの GitHub プロジェクトの URL。[metainfo-standard](https://github.com/ukatech/metainfo-standard) で、ゴースト側の descript.txt にも書くことを推奨されているエントリのひとつ。<br />
[metainfo](metainfo.md) と同じ効果を持ち、同時に書いてもよい。両方あるときは `metainfo` を優先する。

```txt
githubrepo,https://github.com/Taromati2/Taromati2
```

metainfo-standard では、`githubrepo` だけが書かれたゴーストの metainfo フォルダは `https://github.com/<owner>/<repo>/tree/<default-branch>/.ukagaka` にあるものとして扱う。<br />
SSP は既定ブランチを調べるためのネットワークアクセスをしないので、[UUID の計算](../../../list/propertysystem/property-system/general-property/uuid.md)では既定ブランチを `master` とみなし、`https://raw.githubusercontent.com/<owner>/<repo>/master/.ukagaka/` を metainfo フォルダの URL として使う。<br />
既定ブランチが `master` でないリポジトリでは、SSP が計算した UUID と、アプリケーションが求める UUID が一致しないことがある。そのようなゴーストは `metainfo` も書いておくとよい。

値はプロパティシステムの [githubrepo](../../../list/propertysystem/property-system/general-property/githubrepo.md) で取得できる。

**既定値:** 値なし

**対応:** SSP 2.9.35
