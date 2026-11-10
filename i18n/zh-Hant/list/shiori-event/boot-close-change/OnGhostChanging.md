# OnGhostChanging

**カテゴリ:** 啟動、結束與切換事件

收到切換至其他ghost的指示時觸發。<br />
在SSP中，若此事件未傳回腳本（204），接著會觸發[OnClose](OnClose.md)。

- **Reference0**: 即將切換至的ghost本體名稱。
- **Reference1**: 手動切換時傳回manual<br />
  系統切換時傳回automatic<br />
  。
- **Reference2**: 即將切換至的ghost名稱。\[僅SSP\]
- **Reference3**: 即將切換至的ghost路徑。\[僅SSP\]

**対応:** Materia / SSP / CROW / Ninix
