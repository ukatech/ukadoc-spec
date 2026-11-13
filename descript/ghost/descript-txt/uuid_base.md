# uuid_base,文字列

**カテゴリ:** descript.txt

UUID の衝突を防ぐためのベース文字列。[metainfo-standard](https://github.com/ukatech/metainfo-standard) で、metainfo フォルダの descript.txt に `uuid_base` を書いたゴーストは、ゴースト側の descript.txt にも同じ値を書くことが推奨されている。<br />
UUID の元になる文字列(metainfo の URL など)の後ろに、この文字列がそのまま足される。ネットワークなしで UUID を計算できるように、ゴースト側にも書いておく。

```txt
uuid_base,sample-ghost-1
```

値はプロパティシステムの [uuid_base](../../../list/propertysystem/property-system/general-property/uuid_base.md) で取得できる。

**既定値:** 値なし

**対応:** SSP 2.9.35
