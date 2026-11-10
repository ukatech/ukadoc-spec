# 方法：SEND

SEND 是從外部應用程式向 ghost 傳送 Sakura Script 或 SHIORI 事件並使其播放的方法。<br />
SEND 和 NOTIFY 會視為相同的處理方式。兩者在功能上沒有差異。以下規格同樣適用於 NOTIFY。<br />
可以使用 Script 標頭直接指定 Sakura Script，也可以使用 Event 標頭傳送事件，再從 SHIORI 回應取得腳本。<br />
Event 和 Script 可以併用；若 SHIORI 對 Event 的回應沒有傳回腳本，則會使用 Script 標頭中的腳本作為後備。<br />
未指定目標 ghost 時，會以目前已啟動的 ghost 為目標。

## 基本腳本播放範例

```
SEND SSTP/1.4
Charset: UTF-8
Sender: SampleApp
Script: \h\s[0]こんにちは。\w5\u\s[10]ご機嫌いかが？\e
```

## 傳送事件範例

```
SEND SSTP/1.4
Charset: UTF-8
Sender: SampleApp
Event: OnExternalEvent
Reference0: param1
Reference1: param2
```

## 事件＋後備腳本範例

```
SEND SSTP/1.4
Charset: UTF-8
Sender: SampleApp
Event: OnCustomEvent
Reference0: data
Script: \h\s[0]イベント未対応時のスクリプト\e
```

重複指定 IfGhost 標頭，並與對應的 Script 標頭組合，即可為不同 ghost 指定不同腳本。

## 使用 IfGhost 分流範例

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

- **Sender**：雖然是共通標頭，但在 SEND/NOTIFY 中可使用特殊值 `Sender: First`。指定後，會以首次啟動時的 ghost（sakura）為目標。<br />
  Sender 和 User-Agent 兩者皆未指定時，會回應 400 Bad Request。
- **Script**：要播放的 Sakura Script。<br />
  與 Event 標頭併用時，若 SHIORI 對 Event 的回應沒有傳回腳本，則會使用此標頭作為後備。
- **Entry**：項目資料。會傳遞給 SHIORI。
- **Event**：SHIORI 事件名稱。在 SHIORI/3.0 中會作為 ID 標頭指定值處理。
- **Reference\***：事件的 Reference 標頭。只會對 SHIORI 進行字元編碼轉換等最低限度的處理，之後原樣傳遞。
- **IfGhost**：使用 `\0`側名,`\1`側名 的格式指定 ghost 名稱時，緊接其後的 Script 標頭會視為專供特定 ghost 使用。<br />
  若有不在 IfGhost 後方的 Script 標頭，則該標頭會作為不符合 IfGhost 時的預設處理腳本。<br />
  省略時，所有 ghost 都會播放相同的 Script 標頭。<br />
  詳細分流規則請參閱後文的[使用 IfGhost 分流腳本](method_send.md#ifghostによるスクリプト振り分け)。
- **Ghost**：以 ghost 名稱（descript.txt 的 name）指定目標 ghost。
- **Option**：指定 SSTP 執行的 Sakura Script 如何處理。<br />
  可用逗號分隔指定多個選項。除了共通選項（nodescript、notranslate 等）之外，SEND/NOTIFY 可使用的選項旗標如下。<br />
  nobreak：將腳本加入佇列，不中斷目前正在播放的腳本。<br />
  notify：以 notify 模式（不需要回應）傳送 SHIORI 事件。此外，也會強制以與[透過 ValueNotify 標頭傳回腳本時](../shiori3/request.md)相同的方式處理。 \[SSP 2.6.76\]

## response 專用標頭

- **Script**：實際播放的腳本。會移除換行字元。
- **SHIORI 自訂標頭**：SHIORI 回應所包含的標頭會透傳。

## 使用 IfGhost 分流腳本

重複指定 IfGhost 標頭，並與對應的 Script 標頭組合，即可為不同 ghost 指定不同腳本。<br />
IfGhost 和 Script 會依出現順序配對。第一個 IfGhost 之前指定的 Script 會作為預設腳本。

- **名稱比對**：IfGhost 的格式為「`\0`側名,`\1`側名」時，兩個名稱都必須相符。<br />
  IfGhost 的格式只有「`\0`側名」時，只要 `\0`側名相符就會選用。<br />
  若兩者皆不相符，則會使用預設腳本。但若 ghost 設定為「拒絕未指定的 SSTP」，也不會使用預設腳本。
- **視為預設 ghost**：以下名稱會視為預設 ghost（sakura），其腳本也會作為預設腳本。<br />
  「さくら」「エミリ」「えみりぃ」
