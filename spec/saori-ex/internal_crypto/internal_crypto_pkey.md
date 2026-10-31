# 公開鍵暗号（GenerateKeyPair / Sign / Verify / KeyAgreement）

署名の方式は次のとおり（名前のハイフン・アンダースコアの有無と大文字小文字は区別しない）。これ以外は400（`unsupported algorithm`）。`ed25519`～`ps512`は、それぞれJWT（JWS）のalgの`EdDSA` / `ES256` / `ES384` / `ES512` / `RS256` / `RS384` / `RS512` / `PS256` / `PS384` / `PS512`と同じ署名になる。\[SSP 2.9.27\] `es384` `es512` `rs384` `rs512` `ps384` `ps512`が加わった。

- **ed25519**: Ed25519（RFC 8032）。署名は64バイト。
- **es256 / es384 / es512**: ECDSA（es256はP-256 + SHA-256、es384はP-384 + SHA-384、es512はP-521 + SHA-512）。署名はr‖sで、64 / 96 / 132バイト（JWSと同じ形で、DER形式ではない。P-521のrとsは66バイトずつ）。
- **rs256 / rs384 / rs512**: RSA（RSASSA-PKCS1-v1_5）+ SHA-256 / SHA-384 / SHA-512。
- **ps256 / ps384 / ps512**: RSA（RSASSA-PSS）+ SHA-256 / SHA-384 / SHA-512。MGF1も同じハッシュ、ソルトはそのハッシュの長さ（32 / 48 / 64バイト。JWAのPS256 / PS384 / PS512と同じ）。
- **bip340**: secp256k1のSchnorr署名（BIP-340。nostrのイベントの署名と同じ）。署名は64バイト。メッセージはハッシュせずにそのまま署名する（長さは自由。nostrではイベントのID（32バイト）を`--data-in=hex`で渡す）。鍵の渡し方はほかの方式と違う（下を参照）。

鍵は1行のDERのbase64か、PEMで渡す。[GenerateKeyPair](internal_crypto.GenerateKeyPair.md)は前者（秘密鍵はPKCS#8、公開鍵はSubjectPublicKeyInfo）を出力する。<br />
PEMは改行を含みSAORIのヘッダに書けないので、改行を空白にしたもの（または改行を除いて1行にしたもの）を渡してください。`-----BEGIN`で始まればPEMとして、`-----BEGIN ...-----`と`-----END`の間をbase64として読む。<br />
秘密鍵はPKCS#8（`PRIVATE KEY`）のほか、RSAはPKCS#1（`RSA PRIVATE KEY`）、ECDSAはSEC1（`EC PRIVATE KEY`）も読める。パスワードで暗号化された秘密鍵は読めない。公開鍵はSubjectPublicKeyInfo（`PUBLIC KEY`）である。<br />
RSAの鍵は2048～4096ビット、ECDSAの鍵は方式の曲線（es256はP-256、es384はP-384、es512はP-521）だけである。読めない鍵・種類や大きさが方式に合わない鍵は400（`invalid key`）。

**`bip340`は、DER / PEMではなく生の値**である。秘密鍵は32バイト、公開鍵はx座標だけの32バイト（BIP-340の形。nostrの公開鍵と同じ）で、既定の形式は`hex`である。`--key-in=`で読み方を変えられる（`--key-in=bech32`なら`nsec1...` / `npub1...`をそのまま渡せる）。<br />
長さが違う鍵、0や位数以上の秘密鍵は400（`invalid key`）。`--key-in=`は`bip340`でだけ使える（ほかの方式で付けると400 `invalid parameter`）。

[KeyAgreement](internal_crypto.KeyAgreement.md)の鍵（`secp256k1` `x25519` `p256`）も、同じく生の値である（形は`KeyAgreement`の説明を参照）。
