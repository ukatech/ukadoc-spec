# Sign

**カテゴリ:** internal_jwt

对载荷签名并创建 JWT。<br />
载荷是 JSON 对象，按书写的字符串原样使用（UTF-8）。如果不是单个 JSON 对象，则返回 400（`invalid parameter`）。<br />
头部的形式为`{"alg":"HS256","typ":"JWT"}`。在`--header=`中写入 JSON 对象即可添加其中的字段（例如`kid`）（如果写入`typ`，则优先使用该值。写入`alg`时，必须与 Argument1 的值相同，否则返回 400 `invalid parameter`）。

- **Argument1**：alg
- **Argument2**：密钥（HS\*为对称密钥，其他算法为私钥）
- **Argument3**：载荷（JSON）
- **オプション**：`--header=`（JSON） / `--key-in=`（仅 HS\*）

## 記述例

```
Argument0: Sign
Argument1: HS256
Argument2: 0123456789abcdef0123456789abcdef
Argument3: {"sub":"sakura","exp":4102444800}

→ Result: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzYWt1cmEiLCJleHAiOjQxMDI0NDQ4MDB9.eJKcQzLKm4FjTltXWvPqonVpfwhVaBgpvf9nZw0szuM
```

**対応:** SSP 2.9.14
