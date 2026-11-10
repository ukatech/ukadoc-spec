# ShioriEcho

**カテゴリ:** 對話式 ghost 開發用 exe「Ghost Terminal」

輸入指令後發生的事件

- **Reference0**: 在終端機收集到的指令
- **戻り値**: 如果未定義\`ShioriEcho.GetResult\`，可以在此回傳\`ShioriEcho.GetResult\`所支援的任意回傳值。這些回傳值會由終端機正確處理（但若未定義\`ShioriEcho.GetResult\`且不回傳任何內容，回傳值 3 會進入取得下一個指令的流程）。<br />
  如果已定義\`ShioriEcho.GetResult\`，此處的回傳值會被忽略（\*\*但 Sakura Script 仍會正常執行\*\*）。
