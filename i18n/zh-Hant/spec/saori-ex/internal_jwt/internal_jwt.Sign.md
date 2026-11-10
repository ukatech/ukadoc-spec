# Sign

**カテゴリ:** internal_jwt

對 Payload 簽章並建立 JWT。<br />
Payload 必須是 JSON 物件，並以原始字串（UTF-8）使用。若不是單一 JSON 物件，則回傳 400（`invalid parameter`）。<br />
標頭格式為`{"alg":"HS256","typ":"JWT"}`。在`--header=`中填入 JSON 物件即可新增項目（例如`kid`）；若填入`typ`，則以該值為優先。填入`alg`時，必須與 Argument1 的值相同，否則回傳 400 `invalid parameter`。

- **Argument1**: alg
- **Argument2**: 金鑰（HS\*為共用金鑰，其餘為私密金鑰）
- **Argument3**: Payload（JSON）
- **オプション**: `--header=`（JSON） / `--key-in=`（僅限 HS\*）

## 記述例

```
Argument0: Sign
Argument1: HS256
Argument2: 0123456789abcdef0123456789abcdef
Argument3: {"sub":"sakura","exp":4102444800}

→ Result: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzYWt1cmEiLCJleHAiOjQxMDI0NDQ4MDB9.eJKcQzLKm4FjTltXWvPqonVpfwhVaBgpvf9nZw0szuM
```

**対応:** SSP 2.9.14
