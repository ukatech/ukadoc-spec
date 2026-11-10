# Sign

**カテゴリ:** internal_crypto

Signs data with a private key.

- **Argument1**: method (see [public-key cryptography](internal_crypto_pkey.md))
- **Argument2**: private key
- **Argument3**: data (default format is `text`)
- **Options**: `--data-in=` / `--out=` (default is `base64url`; `bip340` uses `hex`) / `--charset=` / `--key-in=` (`bip340` only; default is `hex`) / `--aux=` (`bip340` only; 32 bytes of BIP-340 auxiliary random data. `--aux-in=`, default format is `hex`. Random data is generated each time if omitted. Use only when comparing against test vectors.)

## 記述例

```
Argument0: Sign
Argument1: ed25519
Argument2: MC4CAQAwBQYDK2VwBCIEIJ1hsZ3v/VpguoRK9JLsLMREScVpezJpGXA7rAMcrn9g
Argument3: eyJhbGciOiJFZERTQSJ9.RXhhbXBsZSBvZiBFZDI1NTE5IHNpZ25pbmc

→ Result: hgyY0il_MGCjP0JzlnLWG1PPOt7-09PGcvMg3AIbQR6dWbhijcNR4ki4iylGjg5BhVsPt9g7sVvpAr_MuM0KAg
```

```
Argument0: Sign
Argument1: bip340
Argument2: b7e151628aed2a6abf7158809cf4f3c762e7160f38b4da56a784d9045190cfef
Argument3: 243f6a8885a308d313198a2e03707344a4093822299f31d0082efa98ec4e6c89
Argument4: --data-in=hex
Argument5: --aux=0000000000000000000000000000000000000000000000000000000000000001

→ Result: 6896bd60eeae296db48a229ff71dfe071bde413e6d43f917dc8dcf8c78de33418906d11ac976abccb20b091292bff4ea897efcb639ea871cfa95f6de339e4b0a
```

(BIP-340 test vector 1)

Ed25519 and RSA (rs256 / rs384 / rs512) produce the same signature every time for the same key and data. es256 / es384 / es512, ps256 / ps384 / ps512, and bip340 produce a different signature each time (all can be verified with [Verify](internal_crypto.Verify.md)).

**対応:** SSP 2.9.14
