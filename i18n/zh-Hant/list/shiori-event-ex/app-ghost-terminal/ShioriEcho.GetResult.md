# ShioriEcho.GetResult

**カテゴリ:** 用於開發 ghost 的互動式 exe「Ghost Terminal」

ValueResult 事件的查詢

可回覆的標頭 1：

- **返回值：X-SSTP-PassThru-Result**: 顯示內容，並進入取得下一個命令的流程。
- **返回值（選用）：X-SSTP-PassThru-Type**: 附加資訊：值類型

可回覆的標頭 2：

- **返回值：X-SSTP-PassThru-Special**: 顯示內容，並進入取得下一個命令的流程。<br />
  此返回值會直接進行跳脫處理：<br />
  \- \``\n`\` 會轉換為換行。<br />
  \- \``\t`\` 會轉換為定位字元。<br />
  \- \`\\\\\` 會轉換為 \`\\\`。

可回覆的標頭 3：空

等待 1 秒後，再次執行 ShioriEcho.GetResult。

其他

- **返回值：X-SSTP-PassThru-Status**: 此返回值可與上述返回值搭配使用<br />
  若為 \`End\`，終端機便會結束。<br />
  若為 \`Continue\`，終端機不會顯示任何內容，並進入取得下一個命令的流程。
