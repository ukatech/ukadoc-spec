# `\f[bold,パラメータ]`

**カテゴリ:** 文字更改命令

参数指定为 true 或 1 时显示为粗体。<br />
参数指定为 false 或 0 时禁用。<br />
指定 default 时恢复为 balloon 设置的默认值。<br />
指定 disable 时会采用与无效显示相同的设置。<br />
如果字体不支持，则不会显示为粗体。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\f[bold,1]太字にする。\f[bold,default]バルーンのデフォルト設定にもどす。
```
