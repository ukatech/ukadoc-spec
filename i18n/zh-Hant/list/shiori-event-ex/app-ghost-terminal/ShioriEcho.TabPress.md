# ShioriEcho.TabPress

**カテゴリ:** 用於開發 ghost 的互動式 exe「Ghost Terminal」

按下 Tab 時用來完成命令的事件。

- **Reference0**: 終端機收集到的命令。
- **Reference1**: 按下 Tab 時游標所在位置的命令首字元的位置（起始值為 0）。
- **Reference2**: 使用者首次連續按下 Tab 的次數（起始值為 0）。
- **Reference3**: 在此輪 Tab 補全中首次按下 Tab 時游標所在位置的命令首字元的位置（起始值為 0）。
- **返回值（選用）：X-SSTP-PassThru-Command**: 將命令替換為此內容。
- **返回值（選用）：X-SSTP-PassThru-InsertIndex**: 將游標移至此位置（若未提供則不變）。
- **返回值（選用）：X-SSTP-PassThru-OldInsertIndex**: 將後續的 \`Reference3\` 更新為此內容，並在這輪 Tab 補全結束前維持有效（若未提供則不變）。
