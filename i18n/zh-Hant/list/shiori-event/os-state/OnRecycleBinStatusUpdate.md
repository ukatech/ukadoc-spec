# OnRecycleBinStatusUpdate

**カテゴリ:** OS 狀態事件

檔案移入資源回收筒，或在檔案總管中清空資源回收筒時發生，並通知所有已啟動的 ghost。<br />
此外，ghost 啟動時也會以 *\[NOTIFY\]* 通知。

- **Reference0**: 目前資源回收筒中的檔案數量
- **Reference1**: 目前資源回收筒中的檔案大小，單位為位元組
- **Reference2**: 目前資源回收筒中的檔案數量與前一次的差值
- **Reference3**: 目前資源回收筒中的檔案大小與前一次的差值，單位為位元組
- **Reference4**: 固定為 1（與 OnRecycleBinEmpty 相容的虛設值）
- **Reference5**: 固定為空（與 OnRecycleBinEmpty 相容的虛設值）

**対応:** SSP 2.6.04/Ref4 為 2.6.35
