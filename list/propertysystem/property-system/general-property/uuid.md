# uuid

**カテゴリ:** プロパティシステム \> 汎用プロパティ名

対象の UUID。[metainfo-standard](https://github.com/ukatech/metainfo-standard) の手順で、SSP が手元の情報だけから計算する。ネットワークアクセスはしない。

1. `uuidvalue` を選ぶ。
   - metainfo フォルダがあれば、その URL。descript.txt の [metainfo](../../../../descript/ghost/descript-txt/metainfo.md) の値、なければ [githubrepo](../../../../descript/ghost/descript-txt/githubrepo.md) から導いた URL(既定ブランチは `master` とみなす)。
   - なければ、descript.txt の [homeurl](../../../../descript/ghost/descript-txt/homeurl.md)(URL の変換はかけない)。`homeurl` プロパティと違い、var.txt や SHIORI から取った値は使わない。ネットワークや別プロセスを使わず、時間がたっても値が変わらないようにするため。
   - それもなければ、名前(`name`)。
2. descript.txt に [uuid_base](../../../../descript/ghost/descript-txt/uuid_base.md) があれば、その内容を `uuidvalue` の後ろに足す。
3. `uuidvalue` を UTF-8(末尾に改行を足さない)にして MD5 をとり、得られたバイナリを base64 にする。

例えば、`https://raw.githubusercontent.com/Taromati2/Taromati2/master/.ukagaka/` から作られる UUID は `R5dVNluBvKjtQqjP0dAuoA==` である。

metainfo フォルダは読みに行かないので、`jump_to.txt` による移転や、過去の UUID は反映されない。<br />
`uuidvalue` が空になる(名前もない)ときは、取得に失敗する。

**対応:** SSP 2.9.35
