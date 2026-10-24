# Normalize

**カテゴリ:** internal_text

文字列をUnicodeの正規化形式にそろえる。半角カナと全角カナ、合成済みの文字と結合文字の並びなど、見た目が同じで符号が違う文字列を比べる前にそろえるのに使う。<br />
OSの機能（Windows Vista以降の`NormalizeString`）を使う。使えないOSでは500（`internal error`）。対になっていないサロゲートを含む文字列は400（`invalid encoding`）。

- **Argument1**: 形式：`NFC` / `NFD` / `NFKC` / `NFKD`（大文字小文字は区別しない。これ以外は400 `unsupported algorithm`）
- **Argument2**: 文字列

## 記述例

```
Argument0: Normalize
Argument1: NFKC
Argument2: ｶﾞｲﾄﾞ①

→ Result: ガイド1
```

**対応:** SSP 2.9.13
