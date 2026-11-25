# `\![timemachine,reset]`

**カテゴリ:** Miscellaneous commands

Resets the "virtual modification of the current time" (time machine) offset to 0, restoring the actual time. Equivalent to [`\![timemachine,set,0]`](bang-timemachine-set-value.md).<br />
Effective only when SSP is started with `--allow-timemachine-control`. Otherwise, does nothing and records a warning in the error log. Cannot be executed from unauthorized SSTP (external SSTP).

**対応:** SSP 2.9.39

## 記述例

```sakurascript
\![timemachine,reset]
```
