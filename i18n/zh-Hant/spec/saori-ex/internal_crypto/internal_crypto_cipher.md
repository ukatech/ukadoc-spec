# 對稱金鑰加密（Encrypt / Decrypt）

演算法如下（名稱中的連字號、底線有無及大小寫均不區分）。其他演算法會回傳400（`unsupported algorithm`）。

- **aes-256-gcm（建議） / aes-128-gcm / chacha20-poly1305**: 附帶驗證的加密。遭竄改的密文無法解密。密文格式為「nonce（12位元組）＋密文＋驗證標籤（16位元組）」。
- **aes-256-cbc / aes-128-cbc**: 使用PKCS#7填補。密文格式為「IV（16位元組）＋密文」。由於無法偵測竄改，僅在與其他系統交換資料時使用。
- **aes-256-ctr**: 密文格式為「IV（16位元組）＋密文」。無法偵測竄改。
- **chacha20**: \[SSP 2.9.14\] 不附帶驗證的ChaCha20（RFC 8439。nonce為12位元組，區塊計數器從0開始）。密文格式為「nonce（12位元組）＋密文」。由於無法偵測竄改，僅在與其他系統交換資料時使用（例如nostr的NIP-44等另外附加MAC的方式）。

金鑰（key）的長度必須恰好等於演算法的金鑰長度（AES-256與ChaCha20為32位元組，AES-128為16位元組），否則會回傳400（`invalid key`）。從密碼產生金鑰時，請使用[DeriveKey](internal_crypto.DeriveKey.md)。<br />
每次加密時都會以亂數產生nonce / IV，並加在密文開頭。`--iv=`（指定nonce / IV）與`--pack=none`（不加在開頭）僅供其他系統另外傳遞nonce時使用。**以相同金鑰重複使用相同nonce / IV，會使GCM・ChaCha20-Poly1305・CTR的加密失效**（明文會洩漏，也會變得可以竄改）。請勿在`--iv=`中設定並重複使用固定值。

所有選項錯誤都會回傳400（`invalid parameter`）。

- 將`--aad=`用於不附帶驗證的方式（CBC・CTR・`chacha20`）。
- `--iv=`的長度與該方式的nonce / IV長度（上述「12位元組」或「16位元組」）不完全相同。
- 在`--pack=`中指定`none`以外的值。
