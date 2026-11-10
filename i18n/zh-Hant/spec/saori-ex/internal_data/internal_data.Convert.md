# Convert

**カテゴリ:** internal_data

Rewrites data in a different format (such as base64 ⇔ hexadecimal ⇔ percent-encoding ⇔ string). Specify the input with `--data-in=` and the output with `--out=`.

- **Argument1**: data (default format is `text`)
- **オプション**: `--data-in=` / `--out=` (default is `text`) / `--charset=` / `--hrp=` (\[SSP 2.9.14\] hrp for `--out=bech32`)

## 記述例

```
Argument0: Convert
Argument1: 48656c6c6f
Argument2: --data-in=hex
Argument3: --out=base64

→ Result: SGVsbG8=
```

```
Argument0: Convert
Argument1: 7e7e9c42a91bfef19fa929e5fda1b72e0ebc1a4c1141673e2794234d86addf4e
Argument2: --data-in=hex
Argument3: --out=bech32
Argument4: --hrp=npub

→ Result: npub10elfcs4fr0l0r8af98jlmgdh9c8tcxjvz9qkw038js35mp4dma8qzvjptg
```

**対応:** SSP 2.9.13
