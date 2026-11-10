# `\x[noclear]`

**カテゴリ:** Wait command

Waits for a temporary balloon click.<br />
After the click, the balloon contents and scope are retained.<br />
Unlike `\x`, the effects of Sakura Script commands in the `\f` (text decoration) family remain.

**対応:** SSP

## 記述例

```sakurascript
\1ここで相方が\f[bold,1]トークする。\x[noclear]クリック後、スコープも文字装飾系のさくらスクリプトは有効。
```
