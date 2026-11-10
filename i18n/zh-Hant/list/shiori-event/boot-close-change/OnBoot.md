# OnBoot

**カテゴリ:** 啟動、結束與切換事件

啟動時觸發。<br />
在 SSP 中，若 [OnGhostChanged](OnGhostChanged.md)、[OnGhostCalled](OnGhostCalled.md)、[OnFirstBoot](OnFirstBoot.md)、[OnVanished](../vanish/OnVanished.md) 未傳回腳本（204），則接著觸發此事件。

- **Reference0**: 啟動時的 shell 名稱。
- **Reference6**: ※僅限 MATERIA、SSP　若上次處理期間程式異常終止，則為 halt。
- **Reference7**: ※僅限 MATERIA、SSP　上次處理期間程式異常終止的 ghost 名稱。

**対応:** Materia / SSP / CROW / Ninix
