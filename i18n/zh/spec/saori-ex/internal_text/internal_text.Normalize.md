# Normalize

**カテゴリ:** internal_text

Normalizes a string to a Unicode normalization form. Use this to make strings with different encodings but identical appearance consistent before comparing them, such as half-width and full-width katakana, or precomposed characters and sequences of combining characters.<br />
Uses OS functionality (`NormalizeString` on Windows Vista and later; on XP, uses `normaliz.dll` from the IDN add-on package if available). Returns 500 (`internal error`) on OSes where this functionality is unavailable. Results may vary depending on the OS Unicode version. An empty string returns an empty string (204). A string containing an unpaired surrogate results in 400 (`invalid encoding`).

- **Argument1**: Form: `NFC` / `NFD` / `NFKC` / `NFKD` (case-insensitive; any other value results in 400 `unsupported algorithm`)
- **Argument2**: String

## 記述例

```
Argument0: Normalize
Argument1: NFKC
Argument2: ｶﾞｲﾄﾞ①

→ Result: ガイド1
```

**対応:** SSP 2.9.13
