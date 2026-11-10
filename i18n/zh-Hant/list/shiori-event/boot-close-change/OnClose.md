# OnClose

**カテゴリ:** 啟動、結束與切換事件

收到結束指示時觸發。<br />
在 SSP 中，若 [OnGhostChanging](OnGhostChanging.md)、[OnCloseAll](OnCloseAll.md) 未傳回腳本（204），則接著觸發此事件。

- **Reference0**: ※僅限 SSP　結束原因。<br />
  使用者結束時，會傳回 user<br />
  關機時，會傳回 system。
- **Reference1**: ※僅限 SSP　執行結束操作之選單所屬角色的 scope 編號。會受 popupmenu.type 影響。（主方0、搭檔1...）
- **Reference2**: ※僅限 SSP　執行結束操作之視窗角色的 scope 編號。不受 popupmenu.type 影響。（主方0、搭檔1...）

**対応:** Materia / SSP / CROW / Ninix
