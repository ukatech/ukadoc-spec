# `\![updateother,更新対象/オプション群,...]`

**カテゴリ:** イベントコマンド

任意の名前の更新対象のネットワーク更新イベントを開始する。起動中でないものも指定できる。<br />
以下の指定をいくつでも追加できる。<br />
--balloon=バルーン名<br />
--shell=シェル名<br />
--plugin=プラグイン名<br />
--headline=ヘッドライン名<br />
--language=言語リソース名<br />
更新があればSHIORIイベント[OnUpdateOtherReady](../../shiori-event/network-update/OnUpdateOtherReady.md)などOnUpdateがOnUpdateOtherに変わったイベンド群が通知され、すべて更新が終わった後に結果の総括として[OnUpdateResultEx](../../shiori-event/network-update/OnUpdateResultEx.md)が発生する。<br />
--option=で指定できるオプション指定はSSPのみ。[更新オプション指定](note-1.md#補足)を参照。

**対応:** SSP

## 記述例

```sakurascript
プラグイン「共有変数プラグイン」「うかてん」の更新を実行。\![updateother,--plugin=共有変数プラグイン,--plugin=うかてん]
```
