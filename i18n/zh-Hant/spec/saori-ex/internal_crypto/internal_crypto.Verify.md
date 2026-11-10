# Verify

**カテゴリ:** internal_crypto

Verifies a signature with a public key. Returns `1` if valid and `0` if invalid (also returns `0` if the signature has the wrong length). A private key may be supplied instead of a public key (except for `bip340`).<br />
For `bip340`, a 32-byte public key that is not a point on the curve also returns `0`, as required by BIP-340 (a different length results in 400 `invalid key`).

- **Argument1**: method (see [public-key cryptography](internal_crypto_pkey.md))
- **Argument2**: public key
- **Argument3**: data (default format is `text`)
- **Argument4**: signature (default format is `base64url`; `bip340` uses `hex`)
- **Options**: `--data-in=` / `--signature-in=` / `--charset=` / `--key-in=` (`bip340` only; default is `hex`)

**対応:** SSP 2.9.14
