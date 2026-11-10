# Decrypt

**カテゴリ:** internal_crypto

Decrypt ciphertext produced by [Encrypt](internal_crypto.Encrypt.md).<br />
If decryption fails, returns 500 (`authentication failed`). For authenticated encryption, this happens if the ciphertext, authentication tag, or `--aad=` differs. For CBC, this happens if the padding is invalid. It also happens if the ciphertext is shorter than the leading nonce / IV (or, for authenticated encryption, shorter than the leading nonce / IV plus the trailing authentication tag). Unauthenticated CTR and `chacha20` return some value even with an incorrect key.

- **Argument1**: algorithm name
- **Argument2**: key (default format is `text`)
- **Argument3**: ciphertext (default format is `base64`)
- **Options**: `--key-in=` / `--ciphertext-in=` / `--aad=` / `--aad-in=` / `--iv=` / `--iv-in=` / `--pack=none` / `--out=` (default is `text`) / `--charset=`

When using `--pack=none`, `--iv=` is required. When `--pack=none` is not used (the nonce / IV is at the start of the ciphertext), specifying `--iv=` returns 400 (`invalid parameter`).

**対応:** SSP 2.9.13
