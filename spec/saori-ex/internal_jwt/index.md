# internal_jwt

JWT（RFC 7519）の作成と検証。形式はJWSのコンパクト形式（`ヘッダ.ペイロード.署名`）だけである。<br />
algは次のとおり（引数・`--alg=`では大文字小文字を区別しない）。`none`を含め、これ以外は400（`unsupported algorithm`）。

- **HS256 / HS384 / HS512**: HMAC（共通鍵）。鍵は`--key-in=`の形式（既定は`text`。文字列はUTF-8）で渡す。鍵はハッシュの長さ以上（HS256は32バイト、HS384は48バイト、HS512は64バイト）でなければ400（`invalid key`。RFC 7518の要求）。
- **RS256 / PS256 / ES256 / EdDSA**: 公開鍵暗号。鍵の渡し方と方式の詳細は[internal_cryptoの公開鍵暗号](../internal_crypto/internal_crypto_pkey.md)と同じ（`EdDSA`はEd25519だけ）。`--key-in=`は使えない（400 `invalid parameter`）。

## 一覧

- [Sign](internal_jwt.Sign.md)
- [Verify](internal_jwt.Verify.md)
