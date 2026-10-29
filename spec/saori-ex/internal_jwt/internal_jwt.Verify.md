# Verify

**カテゴリ:** internal_jwt

JWTの署名と有効期限を検証して、正しければペイロード（JSON）を返す。ペイロードに改行があれば空白に置き換えて返す（JSONとしての意味は変わらない）。<br />
**algは`--alg=`で必ず指定する**（無ければ400 `invalid parameter`）。トークンのヘッダの`alg`は信用せず、指定と一致しなければ失敗にする（algのすり替えや`none`による偽造を防ぐため）。<br />
`exp`（有効期限）と`nbf`（有効になる時刻）があれば確かめる。`iss`・`aud`・`iat`などほかの項目は見ないので、必要ならスクリプトで確かめること。

- **Argument1**: トークン
- **Argument2**: 鍵（HS\*は共通鍵、ほかは公開鍵）
- **オプション**: `--alg=`（必須） / `--leeway=`（秒。時計のずれの許容。既定は0。0～86400） / `--key-in=`（HS\*だけ） / `--time=`（現在時刻の代わりに使う日時。[internal_time](../internal_time/index.md)の日時の引数と同じ書き方。既定は現在時刻）

失敗は次のとおり。

- **500 authentication failed**: 署名が合わない。ヘッダの`alg`が`--alg=`と違う（大文字小文字も区別する）。ヘッダに`crit`がある。トークンの形が壊れている（3つに分かれない、base64urlとして読めない、ヘッダ・ペイロードがJSONのオブジェクトでない、UTF-8として正しくない）。`exp` / `nbf`が数値でない。
- **500 expired**: 現在時刻が`exp`＋leeway以降（`exp`の時刻ちょうどで失効）。
- **500 not yet valid**: 現在時刻＋leewayが`nbf`より前。
- **400 invalid key**: 鍵が読めない、種類が合わない、HS\*の鍵が短い。

## 記述例

```
Argument0: Verify
Argument1: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzYWt1cmEiLCJleHAiOjQxMDI0NDQ4MDB9.eJKcQzLKm4FjTltXWvPqonVpfwhVaBgpvf9nZw0szuM
Argument2: 0123456789abcdef0123456789abcdef
Argument3: --alg=HS256

→ Result: {"sub":"sakura","exp":4102444800}
```

**対応:** SSP 2.9.14
