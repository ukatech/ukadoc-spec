# Digest

**カテゴリ:** internal_crypto

ハッシュ値を求める。

- **Argument1**: アルゴリズム名
- **Argument2**: data（既定の形式は`text`。`file`も使える）
- **オプション**: `--data-in=` / `--out=`（既定は`hex`） / `--charset=`

## 記述例

```
Argument0: Digest
Argument1: sha256
Argument2: abc

→ Result: ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
```

文字列は既定でUTF-8のバイト列としてハッシュする。Shift_JISのバイト列のハッシュがほしいときは`--charset=Shift_JIS`を付けてください。

**対応:** SSP 2.9.13
