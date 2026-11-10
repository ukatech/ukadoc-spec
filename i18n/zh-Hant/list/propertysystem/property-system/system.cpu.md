# system.cpu.(キー)

**カテゴリ:** 屬性系統

執行中環境的 CPU 資訊。可填入 (キー) 的字串如下。

- **load**: 負載率（單位為％，整數，會適時以約每分鐘為單位計算移動平均並加以平滑）
- **num**: OS 識別的核心總數
- **vendor**: 廠商名稱。例如：GenuineIntel
- **name**: 名稱。例如：11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz
- **clock**: 時脈頻率
- **features**: 可解讀的擴充指令清單（以半形空白分隔）。例如：MMX SSE SSE2 SSE3

**対応:** SSP 2.6.26
