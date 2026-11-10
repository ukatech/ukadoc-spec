# OnDisplayHandover

**カテゴリ:** OS 狀態事件

視窗在不同螢幕間移動時發生。*\[NOTIFY/其他GET\]*

- **Reference0**: init（位置初始化完成時）或 update（初始化後更新）。<br />
  init 會在啟動後視窗位置確定時通知，不一定早於 OnBoot。
- **Reference1**: 本體為 0，搭檔為 1。SSP/CROW 中也可能有 2 以上的值。
- **Reference2**: 移動前　左,上,右,下,位元深度,是否為主要螢幕(0/1)　init 時為空欄<br />
  例： 0,0,1600,900,32,1
- **Reference3**: 移動後　左,上,右,下,位元深度,是否為主要螢幕(0/1)

**対応:** SSP 2.4.09
