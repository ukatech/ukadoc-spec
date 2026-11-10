# internal_jwt

创建和验证 JWT（RFC 7519）。格式仅支持 JWS 紧凑形式（`头部.载荷.签名`）。<br />
alg 如下（参数和`--alg=`不区分大小写）。除以下算法外（包括`none`），均返回 400（`unsupported algorithm`）。

- **HS256 / HS384 / HS512**：HMAC（对称密钥）。密钥以`--key-in=`指定的形式传入（默认是`text`。字符串使用 UTF-8）。密钥长度必须不小于哈希长度（HS256 为 32 字节，HS384 为 48 字节，HS512 为 64 字节），否则返回 400（`invalid key`。这是 RFC 7518 的要求）。
- **RS256 / RS384 / RS512 / PS256 / PS384 / PS512 / ES256 / ES384 / ES512 / EdDSA**：公钥密码。密钥的传递方式和算法详情与[internal_crypto 的公钥密码](../internal_crypto/internal_crypto_pkey.md)相同（`EdDSA`仅支持 Ed25519。`ES256` / `ES384` / `ES512`分别使用 P-256 / P-384 / P-521 曲线）。不能使用`--key-in=`（400 `invalid parameter`）。\[SSP 2.9.27\] 新增了`RS384` `RS512` `PS384` `PS512` `ES384` `ES512`。

## 一覧

- [Sign](internal_jwt.Sign.md)
- [Verify](internal_jwt.Verify.md)
