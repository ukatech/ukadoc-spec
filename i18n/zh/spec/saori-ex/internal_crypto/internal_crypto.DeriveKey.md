# DeriveKey

**カテゴリ:** internal_crypto

Derive a byte sequence for use as an encryption key from a password or other input. Specify parameters for each method as options; specifying an option that the method does not use returns 400 (`invalid parameter`).<br />
This operation uses time and memory, so [`--async`](../async.md) is recommended.

- **Argument1**: Method: `pbkdf2` / `hkdf` / `hkdf-extract` / `hkdf-expand` / `scrypt` / `argon2id`
- **Argument2**: password (default format is `text`)
- **Argument3**: salt (default format is `text`)
- **Argument4**: Length (bytes; 1～1024)
- **Options**: `--password-in=` / `--salt-in=` / method-specific options below / `--out=` (default is `hex`) / `--charset=`

- **pbkdf2**: `--digest=` (default is `sha256`) / `--iterations=` (default is 600000; 1～10000000)
- **hkdf**: `--digest=` (default is `sha256`) / `--info=` (`--info-in=`, default format is `text`). password is the input key (IKM) and cannot be empty (if empty, returns 400 `invalid parameter`). salt may be empty.
- **hkdf-extract**: \[SSP 2.9.14\] HKDF extract only (RFC 5869 §2.2). `--digest=` (default is `sha256`). password is the input key (IKM; cannot be empty; if empty, returns 400 `invalid parameter`), and salt is used as is. The result is the PRK, so the length must be exactly the hash length (32 for sha256); otherwise, returns 400 (`out of range`).
- **hkdf-expand**: \[SSP 2.9.14\] HKDF expand only (RFC 5869 §2.3). `--digest=` (default is `sha256`) / `--info=`. password is the PRK (cannot be empty; if empty, returns 400 `invalid parameter`). salt must be empty (if not empty, returns 400 `invalid parameter`). The length can be up to 255 times the hash length.
- **scrypt**: `--n=` (default is 8192; must be a power of 2 and at least 2, otherwise returns 400 `invalid parameter`) / `--r=` (default is 8) / `--p=` (default is 10; 1～16). N×r×128 bytes must be no more than 12MiB.
- **argon2id**: `--iterations=` (default is 3; 1～1000) / `--memory=` (KiB; default is 12288; lanes×8～12288) / `--lanes=` (default is 1; 1～16). salt must be at least 8 bytes (if shorter, returns 400 `invalid parameter`); length must be at least 4 (if shorter, returns 400 `out of range`). The version is 1.3 (0x13). Secret keys (secret) and associated data cannot be used.

Values outside the permitted ranges return 400 (`out of range`). The default parameters are a combination of OWASP recommendations that fits within the memory limit (12MiB).

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
