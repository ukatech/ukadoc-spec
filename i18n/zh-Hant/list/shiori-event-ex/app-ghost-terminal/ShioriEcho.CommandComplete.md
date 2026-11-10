# ShioriEcho.CommandComplete

**カテゴリ:** 用於開發 ghost 的互動式 exe「Ghost Terminal」

使用者按下命令列最右側的 \`→\` 時發生的事件

- **Reference0**: 終端機收集到的命令
- **Reference1**: 在游標所在位置按下 \`→\` 時，命令中第一個字元的位置（起始值為 0）。
- **返回值（選用）：X-SSTP-PassThru-Command**: 將命令替換為此內容。<br />
  ghost 可在此事件中自動完成命令。
- **返回值（選用）：X-SSTP-PassThru-InsertIndex**: 將游標移至此位置（若未提供則維持原位）。
