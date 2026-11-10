# `\f[italic,パラメータ]`

**カテゴリ:** 文字變更指令

參數指定為 true 或 1 時，文字會以斜體顯示。<br />
參數指定為 false 或 0 時，會停用斜體。<br />
指定 default 時，會恢復 balloon 設定的預設值。<br />
指定 disable 時，會使用與無效文字顯示相同的設定。<br />
若字型不支援斜體，就不會以斜體顯示。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\f[italic,1]This is italic.\f[italic,default]バルーンのデフォルト設定にもどす。
```
