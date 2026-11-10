# Sign

**カテゴリ:** internal_jwt

Sign the payload to create a JWT.<br />
The payload must be a JSON object and is used as written (in UTF-8). If it is not a single JSON object, return 400 (`invalid parameter`).<br />
The header has the form `{"alg":"HS256","typ":"JWT"}`. Add header fields such as `kid` by writing a JSON object in `--header=` (if `typ` is specified, it takes precedence; if `alg` is specified, it must match Argument1 or return 400 `invalid parameter`).

- **Argument1**: alg
- **Argument2**: Key (symmetric key for HS\*, private key otherwise)
- **Argument3**: Payload (JSON)
- **Options**: `--header=` (JSON) / `--key-in=` (HS\* only)

## 記述例

```
Argument0: Sign
Argument1: HS256
Argument2: 0123456789abcdef0123456789abcdef
Argument3: {"sub":"sakura","exp":4102444800}

→ Result: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzYWt1cmEiLCJleHAiOjQxMDI0NDQ4MDB9.eJKcQzLKm4FjTltXWvPqonVpfwhVaBgpvf9nZw0szuM
```

**対応:** SSP 2.9.14
