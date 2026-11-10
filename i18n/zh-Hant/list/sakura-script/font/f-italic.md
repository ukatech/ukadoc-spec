# `\f[italic,パラメータ]`

**カテゴリ:** Text change command

Set the parameter to true or 1 to enable italic text (slanted).<br />
Set the parameter to false or 0 to disable it.<br />
Specify default to restore the balloon's default setting.<br />
Specify disable to use the same settings as disabled text display.<br />
If the font does not support italics, the text will not be italicized.

**対応:** SSP / Ninix

## 記述例

```sakurascript
\f[italic,1]This is italic.\f[italic,default]バルーンのデフォルト設定にもどす。
```
