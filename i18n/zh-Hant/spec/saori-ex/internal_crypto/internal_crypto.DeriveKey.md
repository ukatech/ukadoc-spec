# DeriveKey

**カテゴリ:** internal_crypto

從密碼等資料衍生出可用作加密金鑰等用途的位元組序列。各方法的參數以選項指定；若指定該方法不使用的選項，會回傳400（`invalid parameter`）。<br />
這項作業會耗用時間與記憶體，因此建議使用[`--async`](../async.md)。

- **Argument1**: 方法：`pbkdf2` / `hkdf` / `hkdf-extract` / `hkdf-expand` / `scrypt` / `argon2id`
- **Argument2**: password（預設格式為`text`）
- **Argument3**: salt（預設格式為`text`）
- **Argument4**: 長度（位元組。1～1024）
- **オプション**: `--password-in=` / `--salt-in=` / 以下各方法的選項 / `--out=`（預設為`hex`） / `--charset=`

- **pbkdf2**: `--digest=`（預設為`sha256`） / `--iterations=`（預設為600000。1～10000000）
- **hkdf**: `--digest=`（預設為`sha256`） / `--info=`（`--info-in=`，預設格式為`text`）。password是輸入金鑰（IKM），不可為空（若為空，會回傳400 `invalid parameter`）。salt可以為空。
- **hkdf-extract**: \[SSP 2.9.14\] 僅執行HKDF的extract步驟（RFC 5869 §2.2）。`--digest=`（預設為`sha256`）。password是輸入金鑰（IKM，不可為空；若為空，會回傳400 `invalid parameter`），salt則直接使用。結果為PRK，長度必須恰好等於雜湊長度（sha256為32），否則會回傳400（`out of range`）。
- **hkdf-expand**: \[SSP 2.9.14\] 僅執行HKDF的expand步驟（RFC 5869 §2.3）。`--digest=`（預設為`sha256`） / `--info=`。password是PRK（不可為空；若為空，會回傳400 `invalid parameter`）。salt必須為空（若不為空，會回傳400 `invalid parameter`）。長度上限為雜湊長度×255。
- **scrypt**: `--n=`（預設為8192。必須是2的冪次且大於或等於2，否則會回傳400 `invalid parameter`） / `--r=`（預設為8） / `--p=`（預設為10。1～16）。N×r×128位元組不得超過12MiB。
- **argon2id**: `--iterations=`（預設為3。1～1000） / `--memory=`（KiB。預設為12288。lanes×8～12288） / `--lanes=`（預設為1。1～16）。salt至少為8位元組（不足時會回傳400 `invalid parameter`），長度至少為4（不足時會回傳400 `out of range`）。版本為1.3（0x13）。不能使用秘密金鑰（secret）與相關資料（associated data）。

超出範圍時會回傳400（`out of range`）。預設參數是符合OWASP建議、且記憶體用量不超過上限（12MiB）的組合。

## 記述例

```
Argument0: DeriveKey
Argument1: pbkdf2
Argument2: password
Argument3: salt
Argument4: 20
Argument5: --digest=sha1
Argument6: --iterations=4096

→ Result: 4b007901b765489abead49d926f721d065a429c1
```

**対応:** SSP 2.9.13
