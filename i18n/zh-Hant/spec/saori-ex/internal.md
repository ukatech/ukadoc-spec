# 內建模組的通用規範

SSP 內建且名稱以`internal_`開頭的模組，皆適用以下通用規範。（為避免與同名的 SAORI DLL 衝突，名稱以`internal_`開頭。）<br />
這些模組只能透過 Direct SSTP 呼叫，不能作為 DLL 載入。

## 函式與引數

`Argument0`是函式名稱（不區分大小寫），`Argument1`之後是該函式的引數。未知的函式名稱會回傳 400（`unknown function`）。<br />
引數由各函式規定數量的**位置引數**及其後排列的**選項**（`--名稱=值`）組成。

- 位於位置引數位置的值，即使以`--`開頭，也不會視為選項，而是當作資料處理。
- 選項只能寫在位置引數之後。若要略過可省略的位置引數來寫選項，請放入空引數。
- 選項名稱不區分大小寫。同名選項重複出現時，以後者為準。
- 沒有`=`的`--名稱`等同於值為空的`--名稱=`。也可以指定值為空的選項。例如，`--aad=`代表「空的額外驗證資料」。但若值為空就沒有意義（例如`--async=`、`--iv=`），則該函式會失敗（多半是 400 `invalid parameter`）。
- 接受數值的引數與選項使用十進位整數，可以加上符號（`+` `-`）。不可包含空白、使用十六進位或小數。若無法解析為數值，會回傳 400（`invalid parameter`）；若超出 64 位元有號整數的範圍，會回傳 400（`out of range`）。各函式的值範圍各有規定。
- 位置引數之後出現未以`--`開頭的值，或函式不接受的選項，都會回傳 400（`invalid parameter`）。將新版 SSP 新增的選項傳給舊版 SSP 時，也會發生這種情況；可透過[internal_system的Describe](internal_system/internal_system.Describe.md)確認是否支援。
- \[SSP 2.9.25\] 位置引數數量不固定的函式（[internal_file的MediaInfo](internal_file/internal_file.MediaInfo.md)以及 \[SSP 2.9.27\] [ImageInfo](internal_file/internal_file.ImageInfo.md)），會從第二個位置起，將第一個以`--`開頭的值及其後的值視為選項。
- 所有函式都接受[`--async=識別碼`](async.md)。

```
Argument0: Digest
Argument1: sha256
Argument2: SGVsbG8=
Argument3: --data-in=base64
Argument4: --out=base64
```

## 位元組序列的輸入格式

雜湊等功能會處理位元組序列，但 SAORI 傳遞的內容是字串。接受位元組序列的引數各有名稱（例如`data`、`key`、`password`、`salt`、`ciphertext`、`signature`、`a`、`b`等，請參閱各函式的說明），可以用`--名稱-in=格式`變更該引數的讀取方式。例如：`--key-in=hex`、`--data-in=base64`。<br />
透過選項傳遞的位元組序列（`--aad=`、`--iv=`、`--info=`）也相同，可以用`--aad-in=hex`之類的方式變更讀取方式。

- **text**：將字串轉換為`--charset=`指定字元編碼的位元組序列（預設為**UTF-8**）。這不是要求的`Charset`（無論傳送端使用何種字元編碼，都會得到與 Web API 簽章等相同的值）。若字串包含無法以該字元編碼表示的字元，會回傳 400（`invalid encoding`）。
- **hex**：十六進位。大小寫皆可。若位數為奇數或包含非十六進位字元，會回傳 400（`invalid encoding`）。
- **base64 / base64url**：填充字元（`=`）可有可無。兩種格式都會讀取 base64 和 base64url 使用的字元（`+ / - _`）。若包含其他字元或填充格式錯誤，會回傳 400（`invalid encoding`）。
- **base32**：RFC 4648。大小寫皆可，填充字元可有可無。若包含無效字元，會回傳 400（`invalid encoding`）。
- **url**：解開百分比編碼後的內容。`+`不會轉換為空白。若`%`後面不是兩位十六進位數字，會回傳 400（`invalid encoding`）。
- **bech32**：\[SSP 2.9.14\] BIP-173 的 bech32（例如 nostr 的`npub1...` / `nsec1...`。無法讀取 bech32m）。會將資料部分轉換為位元組序列。忽略`1`之前的部分（hrp，例如`npub`），若要確認類型，請在指令碼中檢查字串開頭。全大寫或全小寫皆可。若大小寫混用、檢查碼錯誤或包含無效字元，會回傳 400（`invalid encoding`）。沒有長度限制（BIP-173 的 90 個字元）。
- **file**：將值視為檔案路徑，讀取檔案內容。只能用於`internal_crypto`的`Digest` / `HMAC`的`data`（用於其他函式或`data`以外的引數時，會回傳 400 `invalid parameter`）。<br />
  路徑規則請參閱[檔案路徑](#ファイルのパス)。若檔案不存在，會回傳 400（`file not found`）；若讀取過程中發生錯誤，會回傳 500（`file read failed`）。

各引數都有各自的預設格式（請參閱各函式的說明）。解碼後的資料每個引數最多為 8MB（`too large`），但 Direct SSTP 要求本身最多為 1MB，因此實際上會更小。`file`會逐步讀取，因此沒有大小上限。

## 位元組序列的輸出格式

回傳位元組序列的函式可以透過`--out=格式`變更結果的表示方式。預設格式依函式而異。輸出的預設格式會配合同名輸入的預設格式，因此可以將輸出的值直接傳遞給其他函式。

- **hex**：十六進位（小寫）。
- **HEX**：十六進位（大寫）。格式名稱不區分大小寫，但`--out=`的`HEX`是例外，只有寫成`HEX`時才會輸出大寫（`Hex`會輸出小寫十六進位）。在輸入的`--名稱-in=`中，`HEX`會以與`hex`相同的格式讀取。
- **base64**：有填充。
- **base64url**：無填充。
- **base32**：RFC 4648。有填充。
- **url**：將 RFC 3986 的非保留字元（`A-Z a-z 0-9 - . _ ~`）以外的所有字元轉換為`%XX`（大寫）。
- **bech32**：\[SSP 2.9.14\] BIP-173 的 bech32（小寫）。使用`--hrp=`指定 hrp（例如`npub`，長度為 1～83 個字元）。只有[internal_data的Convert](internal_data/internal_data.Convert.md)接受`--hrp=`；其他函式使用`--out=bech32`時，會回傳 400（`invalid parameter`）。
- **text**：以`--charset=`指定的字元編碼（預設為 UTF-8）回傳字串。若位元組序列無法以該字元編碼正確還原為字串，或包含 NUL、換行字元（無法寫入 SAORI 標頭），會回傳 500（`not text`）。<br />
  回應會以要求的`Charset`字元編碼傳回，因此無法以該編碼表示的字元會變成`?`。若要確保能接收任何字元，請以`Charset: UTF-8`傳送要求。

`--charset=`請指定字元編碼名稱（例如`UTF-8`、`Shift_JIS`、`EUC-JP`）。若名稱不明，或指定 UTF-16、UTF-32，會回傳 400（`invalid parameter`）。

## 檔案路徑

適用於指定檔案的引數（`--data-in=file`及[internal_file](internal_file/index.md)的各函式）。

- 相對路徑以 ghost 資料夾（ghost/master）為基準。在沒有 ghost 的呼叫中傳入相對路徑，會回傳 400（`ghost required`）。
- 分隔符號可使用`/`或`\`。
- 對接受檔案的引數傳入資料夾時，會視為檔案不存在，並回傳 400（`file not found`）。
- \[SSP 2.9.33\] 對接受資料夾的引數（`CompressArchive`的壓縮來源）傳入檔案時，會回傳 400（`invalid parameter`）。
- **不限制讀取的目標。** 僅讀取檔案的處理（使用`--data-in=file`進行雜湊、`MediaInfo` / `ImageInfo` / `IsMediaLoadable` / `IsImageLoadable`、`ExtractArchive`的封存檔、`CompressArchive`的壓縮來源），只要使用絕對路徑，也可以讀取 SSP 管理資料夾以外的檔案。只有寫入目的地（`CompressArchive`的壓縮目的地、`ExtractArchive`的解壓縮目的地）才會限制在 SSP 管理的資料夾內。可透過是否回傳`file not found`得知檔案是否存在，因此請勿將使用者輸入等內容直接作為路徑傳入。

## 回應與失敗原因

成功時會回傳 200，結果會放在`Result`中。結果為空字串時，會回傳 204。回傳布林值的函式會以 200 回傳`1`（真）或`0`（假）。「不相符」等情況不算失敗。<br />
失敗時的[ErrorDescription](directsstp.md)除了通用項目外，還可能包含下列內容。

- **unsupported algorithm**：400。未知的演算法名稱。
- **invalid encoding**：400。無法以`--名稱-in=`指定的格式讀取時。壓縮資料損毀時。
- **invalid key**：400。金鑰長度不符合演算法要求時。無法將內容解析為公開金鑰，或金鑰類型與演算法不符時。
- **out of range**：400。數值或日期時間超出可處理範圍時。
- **too large**：400。資料過大時。
- **file not found**：400。`--data-in=file`指定的檔案不存在時。
- **not text**：500。使用`--out=text`時，無法還原為字串。
- **file read failed**：500。讀取檔案過程中發生錯誤時。
- **authentication failed**：500。無法解密時（例如密文遭到竄改或金鑰不同）。無法驗證 JWT 時。
- **expired / not yet valid**：500。JWT 有效期限（`exp`）已過期 / 尚未到達生效時間（`nbf`）時。
- **internal error**：500。baseware 發生預期外的錯誤。
