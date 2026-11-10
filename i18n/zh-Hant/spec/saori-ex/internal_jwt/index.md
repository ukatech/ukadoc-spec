# internal_jwt

建立與驗證 JWT（RFC 7519）。格式僅支援 JWS 的緊湊序列化形式（`ヘッダ.ペイロード.署名`）。<br />
alg 如下（引數與`--alg=`不區分大小寫）。除以下項目外，包括`none`在內的其他值都會回傳 400（`unsupported algorithm`）。

- **HS256 / HS384 / HS512**: HMAC（共用金鑰）。金鑰以`--key-in=`指定的格式傳入（預設為`text`。字串使用 UTF-8）。金鑰長度必須至少等於雜湊長度（HS256 為 32 位元組、HS384 為 48 位元組、HS512 為 64 位元組），否則會回傳 400（`invalid key`。RFC 7518 的要求）。
- **RS256 / RS384 / RS512 / PS256 / PS384 / PS512 / ES256 / ES384 / ES512 / EdDSA**: 公開金鑰加密。金鑰的傳遞方式與演算法詳細資訊，和[internal_crypto 的公開金鑰加密](../internal_crypto/internal_crypto_pkey.md)相同（`EdDSA`僅支援 Ed25519。`ES256` / `ES384` / `ES512`的曲線分別為 P-256 / P-384 / P-521）。不能使用`--key-in=`（400 `invalid parameter`）。\[SSP 2.9.27\] 新增了`RS384` `RS512` `PS384` `PS512` `ES384` `ES512`。

## 一覧

- [Sign](internal_jwt.Sign.md)
- [Verify](internal_jwt.Verify.md)
