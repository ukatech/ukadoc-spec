# `\![open,dialog,color,パラメータ]`

**カテゴリ:** オープンコマンド

カラーパレットのダイアログを開く。このダイアログで色を指定しても、実際に何かが行われるわけではない。<br />
決定時、SHIORIイベント[OnSystemDialog](../../shiori-event/dialogbox/OnSystemDialog.md)が発生し、reference0に「color」、Reference2に「R,G,B」形式で選択した色が格納されているため、ここで実際の処理を各ゴースト作者が作成し実行させる。<br />
閉じるとSHIORIイベント[OnSystemDialogCancel](../../shiori-event/dialogbox/OnSystemDialogCancel.md)が発生する。<br />
パラメータは以下をカンマ区切りで指定可能。

- **--color=R G B**: RGBをそれぞれ0～255で指定
- **--id=イベントID**: OnSystemDialog/OnSystemDialogCancelに送るID<br />
  イベントIDをOn～にするとそのIDのイベントが発生する。Referenceの内容はOnSystemDialogと同じ。<br />
  Reference0は固定で「color」が入っている。

**対応:** SSP

## 記述例

```sakurascript
\![open,dialog,color,--color=255 0 0,--id=テストカラーダイアログ]初期表示色が赤のカラーパレットダイアログを表示。
```
