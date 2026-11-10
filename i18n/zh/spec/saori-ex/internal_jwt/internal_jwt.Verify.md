# Verify

**カテゴリ:** internal_jwt

验证 JWT 签名和有效期；验证成功时返回载荷（JSON）。如果载荷中有换行符，会替换为空格后返回（不改变其作为 JSON 的含义）。<br />
**必须通过`--alg=`指定 alg**（未指定时返回 400 `invalid parameter`）。不信任令牌头部中的`alg`，如果与指定值不一致则验证失败（以防止算法替换或通过`none`伪造）。<br />
如果存在`exp`（有效期）和`nbf`（生效时间），则对其进行检查。不检查`iss`、`aud`、`iat`等其他字段；如有需要，请在脚本中自行检查。

- **Argument1**：令牌
- **Argument2**：密钥（HS\*为对称密钥，其他算法为公钥）
- **オプション**：`--alg=`（必需） / `--leeway=`（秒。允许的时钟偏差。默认值为 0。范围 0～86400） / `--key-in=`（仅 HS\*） / `--time=`（替代当前时间使用的日期时间。格式与[internal_time](../internal_time/index.md)的日期时间参数相同。默认使用当前时间）

错误如下。

- **500 authentication failed**：签名不匹配。头部中的`alg`与`--alg=`不一致（区分大小写）。头部中有`crit`。令牌格式错误（无法拆分为 3 部分、无法作为 base64url 读取、头部或载荷不是 JSON 对象、不是有效的 UTF-8）。`exp` / `nbf`不是数值。
- **500 expired**：当前时间大于或等于`exp`＋leeway（在`exp`指定的时刻失效）。
- **500 not yet valid**：当前时间＋leeway早于`nbf`。
- **400 invalid key**：无法读取密钥、密钥类型不匹配、HS\*密钥过短。

## 記述例

```
Argument0: Verify
Argument1: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzYWt1cmEiLCJleHAiOjQxMDI0NDQ4MDB9.eJKcQzLKm4FjTltXWvPqonVpfwhVaBgpvf9nZw0szuM
Argument2: 0123456789abcdef0123456789abcdef
Argument3: --alg=HS256

→ Result: {"sub":"sakura","exp":4102444800}
```

**対応:** SSP 2.9.14
