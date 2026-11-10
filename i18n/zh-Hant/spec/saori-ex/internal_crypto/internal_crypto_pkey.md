# 公開金鑰密碼學（GenerateKeyPair / Sign / Verify / KeyAgreement）

簽章方式如下（名稱中的連字號、底線有無及大小寫均不區分）。其他方式會回傳 400（`unsupported algorithm`）。`ed25519`～`ps512`的簽章結果，分別與 JWT（JWS）的 alg `EdDSA` / `ES256` / `ES384` / `ES512` / `RS256` / `RS384` / `RS512` / `PS256` / `PS384` / `PS512` 相同。\[SSP 2.9.27\] 新增了 `es384` `es512` `rs384` `rs512` `ps384` `ps512`。

- **ed25519**: Ed25519（RFC 8032）。簽章為 64 位元組。
- **es256 / es384 / es512**: ECDSA（es256 為 P-256 + SHA-256、es384 為 P-384 + SHA-384、es512 為 P-521 + SHA-512）。簽章為 r‖s，長度為 64 / 96 / 132 位元組（格式與 JWS 相同，不是 DER 格式。P-521 的 r 和 s 各為 66 位元組）。
- **rs256 / rs384 / rs512**: RSA（RSASSA-PKCS1-v1_5）+ SHA-256 / SHA-384 / SHA-512。
- **ps256 / ps384 / ps512**: RSA（RSASSA-PSS）+ SHA-256 / SHA-384 / SHA-512。MGF1 使用相同的雜湊演算法，salt 長度等於該雜湊的長度（32 / 48 / 64 位元組，與 JWA 的 PS256 / PS384 / PS512 相同）。
- **bip340**: secp256k1 的 Schnorr 簽章（BIP-340。與 nostr 事件的簽章相同）。簽章為 64 位元組。訊息不經雜湊，直接簽章（長度不限。在 nostr 中，將事件 ID（32 位元組）以 `--data-in=hex` 傳入）。金鑰的傳入方式與其他方式不同（請參閱下文）。

金鑰以單行 DER 的 base64 或 PEM 傳入。[GenerateKeyPair](internal_crypto.GenerateKeyPair.md)會輸出前者（私鑰為 PKCS#8，公開金鑰為 SubjectPublicKeyInfo）。<br />
PEM 包含換行，無法寫入 SAORI 標頭，因此請將換行替換為空白後傳入（或移除換行，合併為一行）。若以 `-----BEGIN` 開頭，便會視為 PEM，並將 `-----BEGIN ...-----` 與 `-----END` 之間的內容作為 base64 讀取。<br />
私鑰除了 PKCS#8（`PRIVATE KEY`）外，RSA 也可讀取 PKCS#1（`RSA PRIVATE KEY`），ECDSA 也可讀取 SEC1（`EC PRIVATE KEY`）。無法讀取以密碼加密的私鑰。公開金鑰使用 SubjectPublicKeyInfo（`PUBLIC KEY`）。<br />
RSA 金鑰長度須為 2048～4096 位元，ECDSA 金鑰只接受該方式使用的曲線（es256 為 P-256、es384 為 P-384、es512 為 P-521）。無法讀取的金鑰，或種類、大小不符合方式要求的金鑰，會回傳 400（`invalid key`）。

**`bip340`使用原始值，而非 DER / PEM**。私鑰為 32 位元組，公開金鑰則只有 x 座標，為 32 位元組（BIP-340 格式，與 nostr 公開金鑰相同）；預設格式為 `hex`。可透過 `--key-in=`變更讀取方式（使用 `--key-in=bech32`時，可直接傳入 `nsec1...` / `npub1...`）。<br />
金鑰長度不符，或私鑰值為 0 或大於等於階數時，會回傳 400（`invalid key`）。`--key-in=`只能用於 `bip340`（用於其他方式時會回傳 400 `invalid parameter`）。

[KeyAgreement](internal_crypto.KeyAgreement.md)使用的金鑰（`secp256k1` `x25519` `p256`）同樣是原始值（格式請參閱 `KeyAgreement`的說明）。
