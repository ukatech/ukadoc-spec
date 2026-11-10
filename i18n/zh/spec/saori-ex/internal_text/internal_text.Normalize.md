# Normalize

**カテゴリ:** internal_text

将字符串统一为 Unicode 规范化形式。用于在比较外观相同但编码不同的字符串前，将半角片假名和全角片假名、预组字符和组合字符序列等统一起来。<br />
使用操作系统的功能（Windows Vista 及之后版本的 `NormalizeString`。在 XP 上，如果有 IDN 附加包中的 `normaliz.dll`，则使用该库）。在不支持该功能的操作系统上返回 500（`internal error`）。结果可能因操作系统的 Unicode 版本而异。空字符串返回空字符串（204）。包含未配对代理项的字符串返回 400（`invalid encoding`）。

- **Argument1**: 形式：`NFC` / `NFD` / `NFKC` / `NFKD`（不区分大小写；其他值返回 400 `unsupported algorithm`）
- **Argument2**: 字符串

## 記述例

```
Argument0: Normalize
Argument1: NFKC
Argument2: ｶﾞｲﾄﾞ①

→ Result: ガイド1
```

**対応:** SSP 2.9.13
