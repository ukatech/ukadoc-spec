# `\![timemachine,reset]`

**カテゴリ:** 未分類コマンド

「現在時刻の仮想的変更」（タイムマシン）の差分を0に戻し、実際の時刻に戻す。[`\![timemachine,set,0]`](bang-timemachine-set-value.md) と同じ。<br />
SSPを `--allow-timemachine-control` 付きで起動したときだけ有効。付けていないときは何もせず、エラーログに警告を記録する。認可されていないSSTP（外部からのSSTP）からは実行できない。

**対応:** SSP 2.9.39

## 記述例

```sakurascript
\![timemachine,reset]
```
