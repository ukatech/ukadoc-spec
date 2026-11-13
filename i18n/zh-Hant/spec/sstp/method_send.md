# 方法：SEND

SEND 是從外部應用程式向 ghost 傳送並播放 Sakura Script 或 SHIORI 事件的方法。<br />
SEND 與 NOTIFY 視為相同的處理，兩者在功能上沒有差異。以下規格同樣適用於 NOTIFY。<br />
可以使用 Script 標頭直接指定 Sakura Script，也可以使用 Event 標頭傳送事件，從 SHIORI 回應取得腳本。<br />
Event 與 Script 可以併用；若 Event 的 SHIORI 回應未傳回腳本，則回退使用 Script 標頭中的腳本。<br />
若未指定目標 ghost，則以目前執行中的 ghost 為目標。

## 基本腳本播放範例

```
SEND SSTP/1.4
Charset: UTF-8
Sender: SampleApp
Script: \h\s[0]こんにちは。\w5\u\s[10]ご機嫌いかが？\e
```

## 事件傳送範例

```
SEND SSTP/1.4
Charset: UTF-8
Sender: SampleApp
Event: OnExternalEvent
Reference0: param1
Reference1: param2
```

## 事件＋回退腳本範例

```
SEND SSTP/1.4
Charset: UTF-8
Sender: SampleApp
Event: OnCustomEvent
Reference0: data
Script: \h\s[0]イベント未対応時のスクリプト\e
```

透過多次記述 IfGhost 標頭並搭配對應的 Script 標頭，可以為各個 ghost 指定不同的腳本。

## 使用 IfGhost 分流的範例

```
SEND SSTP/1.4
Charset: UTF-8
Sender: SampleApp
Script: \h\s[0]こんにちは。\e
IfGhost: まゆら
Script: \h\s[0]まゆらさん、こんにちは。\e
IfGhost: 花ちゃん,妹
Script: \h\s[0]花ちゃんと妹さん、こんにちは。\e
```

## 抑制中斷的範例

```
SEND SSTP/1.4
Charset: UTF-8
Sender: SampleApp
Script: \h\s[0]割り込まないで追加。\e
Option: nobreak
```

## request 專用標頭

- **Sender**: 雖然是共通標頭，但在 SEND/NOTIFY 中可使用特殊值 `Sender: First`。指定後，會以首次啟動時的 ghost（sakura）為目標。<br />
  若未指定 Sender 和 User-Agent，則回傳 400 Bad Request。
- **Script**: 要播放的 Sakura Script。<br />
  與 Event 標頭併用時，若 Event 的 SHIORI 回應未傳回腳本，則作為回退腳本使用。
- **Entry**: 項目資料，會傳遞給 SHIORI。
- **Event**: SHIORI 事件名稱。在 SHIORI/3.0 中，視為指定 ID 標頭。
- **Reference\***: 事件的 Reference 標頭。僅執行字元編碼轉換等最低限度的處理後，直接傳遞給 SHIORI。
- **IfGhost**: 以 `\0`側名稱,`\1`側名稱 的格式指定 ghost 名稱時，緊接其後的 Script 標頭會視為特定 ghost 專用。<br />
  若存在不緊接在 IfGhost 之後的 Script 標頭，則該標頭作為不符合 IfGhost 時的預設處理用 Script。<br />
  \[SSP 2.9.35\] 也可以指定 ghost 的 [UUID](../../list/propertysystem/property-system/general-property/uuid.md) 代替名稱（不含逗號，且符合 UUID 格式）。如此可正確區分同名的 ghost。<br />
  省略時，所有 ghost 都會播放相同的 Script 標頭。<br />
  詳細分流規則請參閱後述的[使用 IfGhost 分流腳本](method_send.md#ifghostによるスクリプト振り分け)。
- **Ghost**: 以 ghost 名稱（descript.txt 的 name）指定目標 ghost。
- **Option**: 指定如何處理由 SSTP 執行的 Sakura Script。<br />
  可用逗號分隔來指定多個選項。除共通選項（nodescript、notranslate 等）外，SEND/NOTIFY 可使用的選項旗標如下。<br />
  nobreak : 不中斷目前播放中的腳本，將腳本加入佇列。<br />
  notify : 以 notify 模式（不需回應）傳送 SHIORI 事件。此外，腳本會被強制視為與[透過 ValueNotify 標頭傳回時](../shiori3/request.md)相同。 \[SSP 2.6.76\]

## response 專用標頭

- **Script**: 實際播放的腳本。換行會被移除。
- **SHIORI 自訂標頭**: SHIORI 回應中包含的標頭會直接透傳。

## 使用 IfGhost 分流腳本

透過多次記述 IfGhost 標頭並搭配對應的 Script 標頭，可以為各個 ghost 指定不同的腳本。<br />
IfGhost 與 Script 依出現順序對應。在第一個 IfGhost 之前記述的 Script 為預設腳本。

- **名稱比對**: 若 IfGhost 的格式為「`\0`側名稱,`\1`側名稱」，則兩個名稱都必須相符。<br />
  若 IfGhost 只有「`\0`側名稱」，則只需 `\0`側名稱相符即可選取。<br />
  \[SSP 2.9.35\] 若 IfGhost 符合 UUID 格式（22 個 base64 字元加上 `==`），則不比對名稱，而是根據 ghost 的 UUID 是否相符來選取。若有多個 UUID 相同的 ghost 正在執行，則優先選取顯示中的 ghost。<br />
  若皆不相符，則使用預設腳本。但若 ghost 設定為「拒絕未指定 SSTP」，則預設腳本也不會使用。
- **視為預設 ghost**: 以下名稱會被視為預設 ghost（sakura），其腳本也會作為預設腳本。<br />
  「さくら」「エミリ」「えみりぃ」
