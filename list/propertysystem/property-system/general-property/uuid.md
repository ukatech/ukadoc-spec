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

[ghostlist](../ghostlist.md)・[balloonlist](../balloonlist.md)・[activeghostlist](../activeghostlist.md)の括弧の中には、名前の代わりにこのUUIDを書ける。SSTPの宛先指定にも使える([ReceiverGhostUUID](../../../../spec/sstp/req_res.md)、[IfGhost](../../../../spec/sstp/method_send.md))。

ゴースト・バルーン・シェル・プラグインの名前を受け取るさくらスクリプト(`\![change,ghost,...]`、`\![call,ghost,...]`、`\![change,shell,...]`、`\![change,balloon,...]`、`\![raiseother,...]`、`\![notifyother,...]`、`\![raiseplugin,...]`、`\![notifyplugin,...]`、`\![timerraiseother,...]`、`\![timernotifyother,...]`、`\![timerraiseplugin,...]`、`\![timernotifyplugin,...]`)と、起動オプションの`--ghost`でも、名前の代わりにUUIDを書ける。名前などと一致しないときに、UUIDの形(base64の22文字と`==`)のものだけを照合する。

プロパティシステムでは、`ghostlist`・`balloonlist`・`activeghostlist`・`pluginlist`のほか、`history.ghost`・`history.balloon`・`history.plugin`と`rateofuselist`の括弧の中にも書ける。履歴と利用統計は、内部では名前やパスで記録していて、UUIDで記録しているわけではない(保存の形式は変わらない)。UUIDで引くと、導入されているゴーストなどに引き当ててから、その記録を引く。

ゴーストのdescript.txtの`balloon`・`recommended.balloon`と、バルーンのdescript.txtの`recommended.ghost`にも、名前の代わりにUUIDを書ける。

プラグインには、descript.txtの`id`(プラグイン自身が決めるGUID。これまでどおり、IDとして一致を見る)と、この`uuid`の両方がある。別のものであり、`id`は`uuid`に置き換わらない。

**対応:** SSP 2.9.35
