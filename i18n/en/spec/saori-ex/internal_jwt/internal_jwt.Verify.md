# Verify

**カテゴリ:** internal_jwt

Verify the JWT signature and expiration, and return the payload (JSON) if valid. If the payload contains line breaks, replace them with spaces before returning it (this does not change its meaning as JSON).<br />
**`--alg=` must always be specified** (if omitted, return 400 `invalid parameter`). Do not trust the token header's `alg`; fail if it does not match the specified value (to prevent algorithm substitution or forgery using `none`).<br />
Check `exp` (expiration time) and `nbf` (time before which the token is not valid) if present. Other fields such as `iss`, `aud`, and `iat` are not checked; check them in a script if needed.

- **Argument1**: Token
- **Argument2**: Key (symmetric key for HS\*, public key otherwise)
- **Options**: `--alg=` (required) / `--leeway=` (seconds; allowed clock skew; default is 0; range 0–86400) / `--key-in=` (HS\* only) / `--time=` (date and time to use instead of the current time. Use the same format as the date-time argument for [internal_time](../internal_time/index.md). Defaults to the current time)

Failures are as follows.

- **500 authentication failed**: Signature does not match. Header `alg` differs from `--alg=` (case-sensitive). Header contains `crit`. Token is malformed (not split into 3 parts, not readable as base64url, header or payload is not a JSON object, or invalid UTF-8). `exp` / `nbf` is not numeric.
- **500 expired**: Current time is at or after `exp` + leeway (the token expires exactly at the time specified by `exp`).
- **500 not yet valid**: Current time + leeway is earlier than `nbf`.
- **400 invalid key**: Key cannot be read, is of the wrong type, or is too short for HS\*.

## 記述例

```
Argument0: Verify
Argument1: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzYWt1cmEiLCJleHAiOjQxMDI0NDQ4MDB9.eJKcQzLKm4FjTltXWvPqonVpfwhVaBgpvf9nZw0szuM
Argument2: 0123456789abcdef0123456789abcdef
Argument3: --alg=HS256

→ Result: {"sub":"sakura","exp":4102444800}
```

**対応:** SSP 2.9.14
