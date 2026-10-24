# Convert

**カテゴリ:** internal_data

データを別の形式で書き直す（base64⇔16進⇔パーセントエンコード⇔文字列など）。入力は`--data-in=`、出力は`--out=`で指定する。

- **Argument1**: data（既定の形式は`text`）
- **オプション**: `--data-in=` / `--out=`（既定は`text`） / `--charset=` / `--hrp=`（\[SSP 2.9.14\] `--out=bech32`のhrp）

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
