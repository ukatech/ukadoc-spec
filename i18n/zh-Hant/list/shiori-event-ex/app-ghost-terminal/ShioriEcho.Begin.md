# ShioriEcho.Begin

**カテゴリ:** 用於開發 ghost 的互動式 exe「Ghost Terminal」

此 ghost 啟動時發生的 ghost_terminal 事件

- **Reference0**: 終端機版本
- **Reference1**: 終端機的工作階段類型<br />
  若終端機以 \`-s\` 開頭，則為 \`SakuraScript\`。<br />
  若終端機以 \`-c\` 開頭，則為 \`Command\`。<br />
  若以共用方式啟動終端機，則為 \`Common\`。
- **返回值：X-SSTP-PassThru-Tittle（選用）**: 設定終端機標題
- **返回值：X-SSTP-PassThru-Icon（選用）**: 設定終端機圖示
- **返回值：X-SSTP-PassThru-SmallIcon（選用）**: 設定終端機的小圖示<br />
  若未設定，則與 \`X-SSTP-PassThru-Icon\` 相同
- **返回值：X-SSTP-PassThru-CustomLoginInfo（選用）**: 若有設定，終端機不會顯示預設登入資訊，而會顯示此內容。<br />
  此返回值會直接進行跳脫處理：<br />
  \- \``\n`\` 會轉換為換行。<br />
  \- \``\t`\` 會轉換為定位字元。<br />
  \- \`\\\\\` 會轉換為 \`\\\`。
