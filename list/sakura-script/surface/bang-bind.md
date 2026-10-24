# `\![bind,カテゴリ名,パーツ名,数値]`

**カテゴリ:** サーフェスコマンド

着せ替えパーツを着衣、脱衣する。<br />
数値部分は1で着衣、0で脱衣。<br />
パーツ名を空欄にするとカテゴリ単位の動作になる。<br />
数値欄を空欄または省略するとメニュー操作時のようにON/OFFの繰り返しとなる。<br />
スクリプト実行後、SHIORIイベントOnDressupChangedが通知され、その後にSHIORIイベントOnNotifyDressupInfoが通知される。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\![bind,head,ribbon,1]本体側の着せ替えとして設定された、headカテゴリのribbonを装着。\1\![bind,arm,,0]相方側の着せ替えとして設定された、armカテゴリのパーツを全て解除。
```
