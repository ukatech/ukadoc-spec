# `\x`

**カテゴリ:** 等待指令

讓 balloon 等待點擊。<br />
點擊後會重設 scope 為 `\0`，並解除 `\f`（文字裝飾）類 Sakura Script 的效果。由 `\e` 解除的 Sakura Script 則會繼續生效。

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
\1ここで相方が\f[bold,1]トークする。\xクリック後、スコープはデフォルトの本体側に戻り、フォント変更のさくらスクリプトは解除される。
```
