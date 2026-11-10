# DeriveKey

**カテゴリ:** internal_crypto

Derives a byte sequence for use as an encryption key from a password or similar input. Specify parameters for each method as options; specifying an option that is not used by the method returns 400 (`invalid parameter`).<br />
Since this operation uses time and memory, [`--async`](../async.md) is recommended.

- **Argument1**: Method: `pbkdf2` / `hkdf` / `hkdf-extract` / `hkdf-expand` / `scrypt` / `argon2id`
- **Argument2**: password (default format is `text`)
- **Argument3**: salt (default format is `text`)
- **Argument4**: Length (bytes; 1–1024)
- **Options**: `--password-in=` / `--salt-in=` / method-specific options below / `--out=` (default is `hex`) / `--charset=`

- **pbkdf2**: `--digest=` (default is `sha256`) / `--iterations=` (default is 600000; 1–10000000)
- **hkdf**: `--digest=` (default is `sha256`) / `--info=` (`--info-in=`, default format is `text`). The password is the input key (IKM) and cannot be empty (an empty value returns 400 `invalid parameter`). The salt may be empty.
- **hkdf-extract**: \[SSP 2.9.14\] HKDF extract only (RFC 5869 §2.2). `--digest=` (default is `sha256`). The password is the input key (IKM; it cannot be empty, and an empty value returns 400 `invalid parameter`); the salt is used as is. The result is the PRK, and its length must be exactly the hash length (32 for sha256), or 400 (`out of range`) is returned.
- **hkdf-expand**: \[SSP 2.9.14\] HKDF expand only (RFC 5869 §2.3). `--digest=` (default is `sha256`) / `--info=`. The password is the PRK (it cannot be empty; an empty value returns 400 `invalid parameter`). The salt must be empty (a non-empty value returns 400 `invalid parameter`). The length can be up to 255 times the hash length.
- **scrypt**: `--n=` (default is 8192; must be a power of 2 and at least 2, or 400 `invalid parameter` is returned) / `--r=` (default is 8) / `--p=` (default is 10; 1–16). N×r×128 bytes must not exceed 12 MiB.
- **argon2id**: `--iterations=` (default is 3; 1–1000) / `--memory=` (KiB; default is 12288; lanes×8–12288) / `--lanes=` (default is 1; 1–16). The salt must be at least 8 bytes (a shorter value returns 400 `invalid parameter`), and the length must be at least 4 (a shorter value returns 400 `out of range`). The version is 1.3 (0x13). Secret keys (secret) and associated data cannot be used.

Values outside the allowed ranges return 400 (`out of range`). The default parameters use a combination of OWASP-recommended values that stays within the memory limit (12 MiB).

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
