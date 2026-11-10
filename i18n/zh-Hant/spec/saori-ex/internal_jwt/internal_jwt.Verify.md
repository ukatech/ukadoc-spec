# Verify

**カテゴリ:** internal_jwt

驗證 JWT 的簽章與有效期限，若正確則回傳 Payload（JSON）。若 Payload 中有換行，會以空白取代後回傳（不會改變 JSON 的意義）。<br />
**必須透過`--alg=`指定 alg**（若未指定，則回傳 400 `invalid parameter`）。不信任 Token 標頭中的`alg`，若與指定值不符則判定失敗（以防止 alg 替換或利用`none`偽造）。<br />
若有`exp`（有效期限）和`nbf`（生效時間），則會進行檢查。不會檢查`iss`、`aud`、`iat`等其他項目，必要時請在 script 中自行檢查。

- **Argument1**: Token
- **Argument2**: 金鑰（HS\*為共用金鑰，其餘為公開金鑰）
- **オプション**: `--alg=`（必填） / `--leeway=`（秒。時鐘偏差的容許值。預設為0。0～86400） / `--key-in=`（僅限 HS\*） / `--time=`（用來取代目前時間的日期時間。寫法與[internal_time](../internal_time/index.md)的日期時間引數相同。預設為目前時間）

失敗情況如下。

- **500 authentication failed**: 簽章不符。標頭的`alg`與`--alg=`不同（區分大小寫）。標頭中有`crit`。Token 格式錯誤（無法分成三個部分、無法作為 base64url 讀取、標頭或 Payload 不是 JSON 物件、不是有效的 UTF-8）。`exp` / `nbf`不是數值。
- **500 expired**: 目前時間已到`exp`＋leeway（在`exp`的時間點即失效）。
- **500 not yet valid**: 目前時間＋leeway早於`nbf`。
- **400 invalid key**: 無法讀取金鑰、金鑰類型不符，或 HS\*金鑰太短。

## 記述例

```
Argument0: Verify
Argument1: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzYWt1cmEiLCJleHAiOjQxMDI0NDQ4MDB9.eJKcQzLKm4FjTltXWvPqonVpfwhVaBgpvf9nZw0szuM
Argument2: 0123456789abcdef0123456789abcdef
Argument3: --alg=HS256

→ Result: {"sub":"sakura","exp":4102444800}
```

**対応:** SSP 2.9.14
