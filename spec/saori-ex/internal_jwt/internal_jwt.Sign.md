# Sign

**カテゴリ:** internal_jwt

ペイロードに署名して、JWTを作る。<br />
ペイロードはJSONのオブジェクトで、書かれた文字列のまま（UTF-8で）使う。JSONのオブジェクト1つでなければ400（`invalid parameter`）。<br />
ヘッダは`{"alg":"HS256","typ":"JWT"}`の形。`--header=`にJSONのオブジェクトを書くと、その項目（`kid`など）を足せる（`typ`を書けばそれが優先。`alg`を書くときはArgument1と同じ値でなければ400 `invalid parameter`）。

- **Argument1**: alg
- **Argument2**: 鍵（HS\*は共通鍵、ほかは秘密鍵）
- **Argument3**: ペイロード（JSON）
- **オプション**: `--header=`（JSON） / `--key-in=`（HS\*だけ）

## 記述例

```
Argument0: Sign
Argument1: HS256
Argument2: 0123456789abcdef0123456789abcdef
Argument3: {"sub":"sakura","exp":4102444800}

→ Result: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzYWt1cmEiLCJleHAiOjQxMDI0NDQ4MDB9.eJKcQzLKm4FjTltXWvPqonVpfwhVaBgpvf9nZw0szuM
```

**対応:** SSP 2.9.14
