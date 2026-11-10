# `\f[italic,パラメータ]`

**カテゴリ:** Text formatting command

Specify true or 1 for the parameter to enable italics.<br />
Specify false or 0 for the parameter to disable it.<br />
Specify default to restore the balloon's default setting.<br />
Specify disable to use the same setting as disabled text display.<br />
If the font does not support italics, the text will not be italicized.

**対応:** SSP / Ninix

## 記述例

```sakurascript
\f[italic,1]This is italic.\f[italic,default]バルーンのデフォルト設定にもどす。
```
