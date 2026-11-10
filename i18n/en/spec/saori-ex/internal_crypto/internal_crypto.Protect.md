# Protect

**カテゴリ:** internal_crypto

Wrap data using the OS data protection feature (Windows DPAPI). The wrapped data can be unwrapped with [Unprotect](internal_crypto.Unprotect.md) only by the same user on the same PC (or by any user on the same PC if `--scope=machine` is specified).<br />
This is intended to prevent tokens and similar data stored in save data from being read if copied to another PC or another user's account; it does not isolate ghosts from each other (other ghosts or programs running as the same user can unwrap the data).

- **Argument1**: data (default format is `text`)
- **Options**: `--data-in=` / `--scope=user` (default) / `--scope=machine` (any other value results in 400 `invalid parameter`) / `--out=` (default is `base64`) / `--charset=`

**If save data is moved to another PC (for example, by sharing SSP save data, synchronizing it through cloud storage, or copying it manually), or if the Windows user account is recreated, the data can no longer be unwrapped**. Scripts should handle Unprotect failures by, for example, asking the user to log in again.

**対応:** SSP 2.9.13
