# `\x`

**カテゴリ:** Wait commands

Wait for a click on the balloon.<br />
After the click, the scope is reset to `\0`, and the effects of Sakura Script commands in the `\f` (text formatting) family are also cleared. Sakura Script commands that are cleared by `\e` continue to apply.

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
\1ここで相方が\f[bold,1]トークする。\xクリック後、スコープはデフォルトの本体側に戻り、フォント変更のさくらスクリプトは解除される。
```
