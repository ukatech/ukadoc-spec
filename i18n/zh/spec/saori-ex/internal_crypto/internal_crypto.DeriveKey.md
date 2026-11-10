# DeriveKey

**カテゴリ:** internal_crypto

从密码等内容导出可用作加密密钥等的字节序列。各方式的参数通过选项指定；如果指定了该方式不使用的选项，则返回 400（`invalid parameter`）。<br />
此操作会消耗时间和内存，因此建议使用[`--async`](../async.md)。

- **Argument1**: 方式：`pbkdf2` / `hkdf` / `hkdf-extract` / `hkdf-expand` / `scrypt` / `argon2id`
- **Argument2**: password（默认格式为`text`）
- **Argument3**: salt（默认格式为`text`）
- **Argument4**: 长度（字节，1～1024）
- **选项**: `--password-in=` / `--salt-in=` / 以下各方式对应的选项 / `--out=`（默认值为`hex`） / `--charset=`

- **pbkdf2**: `--digest=`（默认值为`sha256`） / `--iterations=`（默认值为 600000，1～10000000）
- **hkdf**: `--digest=`（默认值为`sha256`） / `--info=`（`--info-in=`，默认格式为`text`）。password 是输入密钥（IKM），不能为空（为空时返回 400 `invalid parameter`）。salt 可以为空。
- **hkdf-extract**: \[SSP 2.9.14\] 仅执行 HKDF 的 extract（RFC 5869 §2.2）。`--digest=`（默认值为`sha256`）。password 是输入密钥（IKM，不能为空；为空时返回 400 `invalid parameter`），salt 原样使用。结果为 PRK，其长度必须恰好等于哈希长度（sha256 时为 32），否则返回 400（`out of range`）。
- **hkdf-expand**: \[SSP 2.9.14\] 仅执行 HKDF 的 expand（RFC 5869 §2.3）。`--digest=`（默认值为`sha256`） / `--info=`。password 是 PRK（不能为空；为空时返回 400 `invalid parameter`）。salt 必须为空（非空时返回 400 `invalid parameter`）。长度最多为哈希长度×255。
- **scrypt**: `--n=`（默认值为 8192，必须是 2 的幂且不小于 2，否则返回 400 `invalid parameter`） / `--r=`（默认值为 8） / `--p=`（默认值为 10，1～16）。N×r×128 字节不得超过 12MiB。
- **argon2id**: `--iterations=`（默认值为 3，1～1000） / `--memory=`（KiB，默认值为 12288，范围为 lanes×8～12288） / `--lanes=`（默认值为 1，1～16）。salt 至少为 8 字节（较短时返回 400 `invalid parameter`），长度至少为 4（较短时返回 400 `out of range`）。版本为 1.3（0x13）。不能使用秘密密钥（secret）和关联数据（associated data）。

超出范围时返回 400（`out of range`）。默认参数采用 OWASP 推荐的参数组合，并将内存用量限制在上限（12MiB）以内。

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
