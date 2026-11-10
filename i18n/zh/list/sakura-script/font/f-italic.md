# `\f[italic,パラメータ]`

**カテゴリ:** 文字更改命令

参数指定为 true 或 1 时显示为斜体 Sample。<br />
参数指定为 false 或 0 时禁用。<br />
指定 default 时恢复为 balloon 设置的默认值。<br />
指定 disable 时会采用与无效显示相同的设置。<br />
如果字体不支持，则不会显示为斜体。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\f[italic,1]This is italic.\f[italic,default]バルーンのデフォルト設定にもどす。
```
