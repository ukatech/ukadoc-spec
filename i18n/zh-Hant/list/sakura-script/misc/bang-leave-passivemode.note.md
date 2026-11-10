# PassiveMode

處於被動模式時，會套用以下限制。<br />
這些限制適用於使用者操作；透過 Sakura Script 執行時則不受限制。

- 限制 owner draw 選單中可選擇的項目。
- 不檢查郵件。
- 不執行 headline sensor。
- 不自動切換。
- 不會中斷 script。
- 選項不會逾時。
- 對話框不會隨時間經過而消失。
- 即使有檔案透過 DnD 拖放進來，也會忽略。
- 也會忽略 nar 連按兩下安裝（SSP 仍會安裝，但 ghost 不會收到事件）。
- 不會收到 OnSurfaceRestore。
- cantalk 一律為 false。（仍會收到 OnSecondChange 和 OnMinuteChange 事件本身）
- 無法切換 ghost。
- （僅限 Materia：）通訊方塊會關閉，且不會重新開啟。
- 無法最小化。
- 無法結束。
- 無法進行 network update。
- 無法解除安裝。
