# `\x`

**カテゴリ:** 等待命令

使 balloon 等待点击。<br />
点击后，scope 会重置为 `\0`，`\f`（文字装饰）类 Sakura Script 的效果也会解除。由 `\e` 解除的 Sakura Script 则会继续生效。

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
\1ここで相方が\f[bold,1]トークする。\xクリック後、スコープはデフォルトの本体側に戻り、フォント変更のさくらスクリプトは解除される。
```
