# Verify

**カテゴリ:** internal_crypto

以公開金鑰驗證簽章。正確時回傳`1`，不正確時回傳`0`（簽章長度不同時也回傳`0`）。也可以傳入私密金鑰代替公開金鑰（`bip340`除外）。<br />
在`bip340`中，即使公開金鑰是32位元組但不是曲線上的點，也會依照BIP-340的規定回傳`0`（長度不同時則回傳400 `invalid key`）。

- **Argument1**: 方式（請參閱[公開金鑰密碼學](internal_crypto_pkey.md)）
- **Argument2**: 公開金鑰
- **Argument3**: data（預設格式為`text`）
- **Argument4**: signature（預設格式為`base64url`。`bip340`為`hex`）
- **選項**: `--data-in=` / `--signature-in=` / `--charset=` / `--key-in=`（僅限`bip340`。預設為`hex`）

**対応:** SSP 2.9.14
