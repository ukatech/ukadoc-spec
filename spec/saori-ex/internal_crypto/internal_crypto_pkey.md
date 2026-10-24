# 公開鍵暗号（GenerateKeyPair / Sign / Verify / KeyAgreement）

署名の方式は次のとおりです（名前のハイフン・アンダースコアの有無と大文字小文字は区別しない）。これ以外は400（`unsupported algorithm`）です。`ed25519`～`ps256`は、それぞれJWT（JWS）のalgの`EdDSA` / `ES256` / `RS256` / `PS256`と同じ署名になります。

- **ed25519**: Ed25519（RFC 8032）。署名は64バイト。
- **es256**: ECDSA（P-256）+ SHA-256。署名は64バイト（r‖s。JWSと同じ形で、DER形式ではない）。
- **rs256**: RSA（RSASSA-PKCS1-v1_5）+ SHA-256。
- **ps256**: RSA（RSASSA-PSS）+ SHA-256。MGF1もSHA-256、ソルトは32バイト（JWAのPS256と同じ）。
- **bip340**: secp256k1のSchnorr署名（BIP-340。nostrのイベントの署名と同じ）。署名は64バイト。メッセージはハッシュせずにそのまま署名する（長さは自由。nostrではイベントのID（32バイト）を`--data-in=hex`で渡す）。鍵の渡し方はほかの方式と違う（下を参照）。

鍵は、1行のDERのbase64か、PEMで渡します。[GenerateKeyPair](internal_crypto.GenerateKeyPair.md)は前者（秘密鍵はPKCS#8、公開鍵はSubjectPublicKeyInfo）を出力します。<br />
PEMは改行を含みSAORIのヘッダに書けないので、改行を空白にしたもの（または改行を除いて1行にしたもの）を渡してください。`-----BEGIN`で始まればPEMとして、`-----BEGIN ...-----`と`-----END`の間をbase64として読みます。<br />
秘密鍵はPKCS#8（`PRIVATE KEY`）のほか、RSAはPKCS#1（`RSA PRIVATE KEY`）、ECDSAはSEC1（`EC PRIVATE KEY`）も読めます。パスワードで暗号化された秘密鍵は読めません。公開鍵はSubjectPublicKeyInfo（`PUBLIC KEY`）です。<br />
RSAの鍵は2048～4096ビット、ECDSAの鍵はP-256だけです。読めない鍵・種類や大きさが方式に合わない鍵は400（`invalid key`）です。

**`bip340`と`KeyAgreement`の`secp256k1`の鍵は、DER / PEMではなく生の値**です。秘密鍵は32バイト、公開鍵はx座標だけの32バイト（BIP-340の形。nostrの公開鍵と同じ）で、既定の形式は`hex`です。`--key-in=`で読み方を変えられます（`--key-in=bech32`なら`nsec1...` / `npub1...`をそのまま渡せる）。<br />
長さが違う鍵、0や位数以上の秘密鍵は400（`invalid key`）です。`--key-in=`はこの2つの方式でだけ使えます（ほかの方式で付けると400 `invalid parameter`）。
