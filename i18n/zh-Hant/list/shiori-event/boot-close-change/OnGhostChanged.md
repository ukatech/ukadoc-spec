# OnGhostChanged

**カテゴリ:** 啟動、結束與切換事件

從其他ghost切換至本ghost時觸發。<br />
在SSP中，若此事件未傳回腳本（204），接著會觸發[OnBoot](OnBoot.md)。

- **Reference0**: 前一個ghost的本體名稱。
- **Reference1**: 前一個ghost切換時使用的腳本。
- **Reference2**: 前一個ghost的名稱。 \[僅SSP\]
- **Reference3**: 前一個ghost的路徑（檔案位置）。 \[僅SSP\]
- **Reference7**: *切換後ghost的*shell名稱。 \[僅SSP\]

**対応:** Materia / SSP / CROW / Ninix
