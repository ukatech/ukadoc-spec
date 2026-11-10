# Describe

**カテゴリ:** internal_system

傳回內建模組函式的呼叫方式（位置引數數量、接受的選項、可供名稱選擇的候選值）。<br />
內建模組函式收到未知選項或未知演算法名稱時，會以 400（`invalid parameter`或`unsupported algorithm`）失敗。在舊版 SSP 中使用新版 SSP 新增的選項或演算法時，就會發生這種情況。先用此函式查詢，即可在呼叫前判斷是否可用。[ListFunctions](internal_system.ListFunctions.md)只會回答函式是否存在。

- **Argument1**: 模組名稱（不區分大小寫）
- **Argument2**: 函式名稱（不區分大小寫）

非內建模組的名稱（包括相容模組）會回傳 400（`unknown module`）；該模組中不存在的函式名稱會回傳 400（`unknown function`）。缺少任一項時會回傳 400（`invalid parameter`）。

結果如下。

- **Result**: 函式名稱（標準拼法）。
- **Value0**: 位置引數的最大數量。指`Argument1`之後、可放在選項之前的數量。位置引數數量可變的函式（例如`internal_file`的`MediaInfo`）會在此提供其上限。
- **Value1**: 必要位置引數的數量。
- **Value2**: 位置引數數量可變時為`1`，固定時為`0`。對於數量可變的函式，會將第二個位置以後第一個以`--`開頭的值及其後續值視為選項（[共通規範](../internal.md#関数と引数)）。
- **Value3**: 以逗號分隔列出可接受的選項名稱。不包含`--`。包含所有函式都接受的`async`。`--資料名稱-in=`形式的選項（例如`data-in`、`key-in`）也會照原樣列出。
- **Value4以後**: 若有只能從固定候選值中選擇的引數或選項，每項會有一個值。格式為`名稱=候選值|候選值|…`；名稱若為位置引數，則為`Argument1`等（與要求中的`ArgumentN`使用相同編號），若為選項，則為`--digest`等。候選值的拼法與各函式說明中列出的名稱相同。沒有固定可選名稱的函式不會提供Value4以後的值。

`--out=`或`--data-in=`等形式的名稱（[共通規範](../internal.md#バイト列の入力の形式)），以及[Format](../internal_time/internal_time.Format.md)的格式名稱，不會列入候選值。

## 記述例

```
Argument0: Describe
Argument1: internal_crypto
Argument2: KeyAgreement

→ Result: KeyAgreement
→ Value0: 3
→ Value1: 3
→ Value2: 0
→ Value3: key-in,peer-in,out,async
→ Value4: Argument1=secp256k1|x25519|p256
```

根據此結果，可將`Value4`以`=`和`|`分割，確認是否包含`x25519`，藉此判斷是否可使用`x25519`。

**対応:** SSP 2.9.27
