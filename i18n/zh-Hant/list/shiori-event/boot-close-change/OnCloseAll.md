# OnCloseAll

**カテゴリ:** 啟動、結束與切換事件

SSP 本身結束時觸發。<br />
除了從 owner draw 選單選擇「全部結束」之外，對唯一正在執行的 ghost 發出「結束」指示時，以及因 OS 關機而使 SSP 結束時，也會觸發此事件。

- **Reference0**: ※僅限 SSP　結束原因。<br />
  使用者結束時，會傳回 user<br />
  關機時，會傳回 system。
- **Reference1**: ※僅限 SSP　執行結束操作之選單所屬角色的 scope 編號。會受 popupmenu.type 影響。（主方0、搭檔1...）
- **Reference2**: ※僅限 SSP　執行結束操作之視窗角色的 scope 編號。不受 popupmenu.type 影響。（主方0、搭檔1...）

**対応:** SSP / Ninix
