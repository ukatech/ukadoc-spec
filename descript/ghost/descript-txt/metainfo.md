# metainfo,URL

**カテゴリ:** descript.txt

ゴーストの情報を置いた metainfo フォルダの URL。[metainfo-standard](https://github.com/ukatech/metainfo-standard) で、ゴースト側の descript.txt にも書くことを推奨されているエントリのひとつ。<br />
metainfo フォルダを持つゴーストは、アプリケーションがこのゴーストから metainfo フォルダへたどり着けるように、また[ネットワークなしで UUID を計算できるように](../../../list/propertysystem/property-system/general-property/uuid.md)、ここに URL を書いておく。<br />
UUID は URL の文字列そのものから作られる。末尾の `/` の有無や、書き換えによって UUID が変わる。

```txt
metainfo,https://raw.githubusercontent.com/Taromati2/Taromati2/master/.ukagaka/
```

[githubrepo](githubrepo.md) と同時に書いてもよい。両方あるときは `metainfo` を優先する。<br />
SSP は metainfo フォルダへのアクセスはせず、書かれた値を保持するだけである。値はプロパティシステムの [metainfo](../../../list/propertysystem/property-system/general-property/metainfo.md) で取得できる。

**既定値:** 値なし

**対応:** SSP 2.9.35
