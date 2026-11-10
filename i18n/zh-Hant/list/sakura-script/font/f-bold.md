# `\f[bold,パラメータ]`

**カテゴリ:** 文字變更指令

參數指定為 true 或 1 時，文字會變粗體。<br />
參數指定為 false 或 0 時，會停用粗體。<br />
指定 default 時，會恢復 balloon 設定的預設值。<br />
指定 disable 時，會使用與無效文字顯示相同的設定。<br />
若字型不支援粗體，就不會以粗體顯示。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\f[bold,1]太字にする。\f[bold,default]バルーンのデフォルト設定にもどす。
```
