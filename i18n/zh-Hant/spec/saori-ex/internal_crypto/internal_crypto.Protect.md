# Protect

**カテゴリ:** internal_crypto

Wraps data using the OS data protection feature (Windows DPAPI). The wrapped data can only be [Unprotect](internal_crypto.Unprotect.md)ed by the same user on the same PC (or by any user on the same PC when `--scope=machine` is used).<br />
This is intended to prevent tokens and similar data stored in save data from being read if copied to another PC or another user; it does not isolate ghosts from each other (other ghosts and programs running as the same user can unwrap it).

- **Argument1**: data (default format is `text`)
- **Options**: `--data-in=` / `--scope=user` (default) / `--scope=machine` (any other value results in 400 `invalid parameter`) / `--out=` (default is `base64`) / `--charset=`

**If save data is moved to another PC (such as by sharing SSP save data, syncing with cloud storage, or copying it manually), or if the Windows user is recreated, the data can no longer be Unprotected**. Scripts should handle an Unprotect failure as something like “please log in again.”

**対応:** SSP 2.9.13
