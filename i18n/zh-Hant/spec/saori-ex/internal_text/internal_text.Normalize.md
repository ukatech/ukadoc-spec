# Normalize

**カテゴリ:** internal_text

將字串轉換為指定的 Unicode 正規化形式。可用於比較外觀相同但編碼不同的字串，例如半形假名與全形假名、預組字元與組合字元序列等。<br />
使用 OS 功能（Windows Vista 以後的`NormalizeString`。在 XP 中，若有 IDN 附加套件的`normaliz.dll`，則使用該套件）。無法使用此功能的 OS 會回傳 500（`internal error`）。結果可能因 OS 的 Unicode 版本而異。空字串會回傳空字串（204）。包含不成對代理字元的字串會回傳 400（`invalid encoding`）。

- **Argument1**: 形式：`NFC` / `NFD` / `NFKC` / `NFKD`（不區分大小寫；其他值會回傳 400 `unsupported algorithm`）
- **Argument2**: 字串

## 記述例

```
Argument0: Normalize
Argument1: NFKC
Argument2: ｶﾞｲﾄﾞ①

→ Result: ガイド1
```

**対応:** SSP 2.9.13
