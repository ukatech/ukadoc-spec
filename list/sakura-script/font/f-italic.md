# `\f[italic,パラメータ]`

**カテゴリ:** 文字変更コマンド

パラメータにtrueまたは1を指定するとイタリック(斜体) Sample。<br />
パラメータにfalseまたは0を指定すると無効。<br />
defaultを指定するとバルーン設定の標準に戻る。<br />
disableを指定すると無効表示と同じ設定になる。<br />
フォントが対応していない場合、斜体にならない。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\f[italic,1]This is italic.\f[italic,default]バルーンのデフォルト設定にもどす。
```
