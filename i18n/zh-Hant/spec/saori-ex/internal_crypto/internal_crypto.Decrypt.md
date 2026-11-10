# Decrypt

**カテゴリ:** internal_crypto

解密[Encrypt](internal_crypto.Encrypt.md)產生的密文。<br />
若無法解密，會回傳500（`authentication failed`）。使用認證加密時，密文、認證標籤或`--aad=`任一項不符都會回傳此錯誤。使用CBC時，填補資料不符也會回傳此錯誤。密文短於開頭的nonce / IV（使用認證加密時，還包括結尾的認證標籤）時，也會回傳此錯誤。不帶認證的CTR和`chacha20`即使金鑰錯誤，也會回傳某個值。

- **Argument1**: 演算法名稱
- **Argument2**: key（預設格式為`text`）
- **Argument3**: ciphertext（預設格式為`base64`）
- **オプション**: `--key-in=` / `--ciphertext-in=` / `--aad=` / `--aad-in=` / `--iv=` / `--iv-in=` / `--pack=none` / `--out=`（預設為`text`） / `--charset=`

使用`--pack=none`時必須指定`--iv=`。未使用`--pack=none`時（nonce / IV 位於密文開頭），若指定`--iv=`，會回傳400（`invalid parameter`）。

**対応:** SSP 2.9.13
