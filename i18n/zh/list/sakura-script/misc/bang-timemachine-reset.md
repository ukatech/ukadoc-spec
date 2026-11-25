# `\![timemachine,reset]`

**カテゴリ:** 未分类命令

将「虚拟更改当前时间」（时间机器）的偏移量重置为 0，恢复实际时间。与 [`\![timemachine,set,0]`](bang-timemachine-set-value.md) 相同。<br />
仅在启动 SSP 时指定 `--allow-timemachine-control` 才有效。未指定时不执行任何操作，并在错误日志中记录警告。无法从未授权的 SSTP（外部 SSTP）执行。

**対応:** SSP 2.9.39

## 記述例

```sakurascript
\![timemachine,reset]
```
