# `\f[strike,パラメータ]`

**カテゴリ:** 文字変更命令

将参数设为 true 或 1 时，会显示删除线 示例。<br />
将参数设为 false 或 0 时，会禁用此效果。<br />
指定 default 时，会恢复为 balloon 设置的默认值。<br />
指定 disable 时，会采用与禁用显示相同的设置。

**対応:** SSP / Ninix

## 記述例

```sakurascript
\f[strike,1]文字に打ち消し線を引く。\f[strike,default]バルーンのデフォルト設定にもどす。
```
