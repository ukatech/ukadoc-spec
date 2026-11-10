# `\f[strike,パラメータ]`

**カテゴリ:** 文字變更指令

參數指定為 true 或 1 時，會顯示刪除線範例。<br />
參數指定為 false 或 0 時，會停用此功能。<br />
指定 default 時，會還原為 balloon 設定的預設值。<br />
指定 disable 時，會使用與停用顯示相同的設定。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\f[strike,1]文字に打ち消し線を引く。\f[strike,default]バルーンのデフォルト設定にもどす。
```
