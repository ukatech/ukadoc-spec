# Convert

**カテゴリ:** internal_data

將資料轉換為其他格式（例如base64⇔16進位⇔百分比編碼⇔字串）。以`--data-in=`指定輸入格式，以`--out=`指定輸出格式。

- **Argument1**: data（預設格式為`text`）
- **選項**: `--data-in=` / `--out=`（預設為`text`） / `--charset=` / `--hrp=`（\[SSP 2.9.14\] `--out=bech32`時使用的hrp）

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
