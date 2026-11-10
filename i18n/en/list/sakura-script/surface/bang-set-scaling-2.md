# `\![set,scaling,横倍率,縦倍率]`

**カテゴリ:** Surface command

Set the surface's horizontal and vertical scale factors separately. The unit is %.<br />
The scale factor is relative to the user-configured scale, which is treated as 100%.<br />
Negative values are allowed; -100 flips the surface along the corresponding axis.

Effective until the ghost ends.

**対応:** SSP

## 記述例

```sakurascript
\![set,scaling,50,100]本体側のサーフェスの大きさが、横50%縦100%になる。
```
