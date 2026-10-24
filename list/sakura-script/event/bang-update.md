# `\![update,更新対象(,オプション,オプション...)]`

**カテゴリ:** イベントコマンド

更新対象のネットワーク更新イベントを開始する。<br />
ghost、shell、balloonが指定可能で、同時に更新する場合それぞれを「+」で区切って指定できる。<br />
更新対象をallとすると、`\![updatebymyself]`と同義。<br />
`\![update,ghost+shell+balloon]`とした場合、`\![updatebymyself]`とは異なりSSP本体設定によらず強制的に更新が実行される。<br />
ghost以外の更新時、更新があればSHIORIイベント[OnUpdateOtherReady](../../shiori-event/network-update/OnUpdateOtherReady.md)などOnUpdateがOnUpdateOtherに変わったイベンド群が通知され、すべて更新が終わった後に結果の総括として[OnUpdateResult](../../shiori-event/network-update/OnUpdateResult.md)が発生する。<br />
オプション指定はSSPのみ。[更新オプション指定](note-1.md#補足)を参照。

**対応:** SSP

## 記述例

```sakurascript
シェルの更新を実行。\![update,shell]
```
