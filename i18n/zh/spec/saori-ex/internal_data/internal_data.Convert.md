# Convert

**カテゴリ:** internal_data

将数据转换为其他格式（例如 base64⇔十六进制⇔百分号编码⇔字符串）。使用`--data-in=`指定输入格式，使用`--out=`指定输出格式。

- **Argument1**: data（默认格式为`text`）
- **选项**: `--data-in=` / `--out=`（默认为`text`） / `--charset=` / `--hrp=`（\[SSP 2.9.14\] `--out=bech32`时使用的 hrp）

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
