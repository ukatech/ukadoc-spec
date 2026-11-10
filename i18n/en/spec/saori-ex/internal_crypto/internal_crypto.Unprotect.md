# Unprotect

**カテゴリ:** internal_crypto

Unwrap data wrapped with [Protect](internal_crypto.Protect.md). If it cannot be unwrapped, the result is 500 (`authentication failed`).

- **Argument1**: data (default format is `base64`)
- **Options**: `--data-in=` / `--out=` (default is `text`) / `--charset=`

**対応:** SSP 2.9.13
