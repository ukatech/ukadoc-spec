# Sign

**カテゴリ:** internal_jwt

Sign the payload and create a JWT.<br />
The payload must be a JSON object, and is used as written (in UTF-8). If it is not a single JSON object, return 400 (`invalid parameter`).<br />
The header has the form `{"alg":"HS256","typ":"JWT"}`. Writing a JSON object to `--header=` adds its fields (such as `kid`) (`typ` takes precedence if specified; if `alg` is specified, it must have the same value as Argument1, or 400 `invalid parameter` is returned).

- **Argument1**: alg
- **Argument2**: Key (symmetric key for HS\*, private key otherwise)
- **Argument3**: Payload (JSON)
- **オプション**: `--header=` (JSON) / `--key-in=` (HS\* only)

## 記述例

```
Argument0: Sign
Argument1: HS256
Argument2: 0123456789abcdef0123456789abcdef
Argument3: {"sub":"sakura","exp":4102444800}

→ Result: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzYWt1cmEiLCJleHAiOjQxMDI0NDQ4MDB9.eJKcQzLKm4FjTltXWvPqonVpfwhVaBgpvf9nZw0szuM
```

**対応:** SSP 2.9.14
