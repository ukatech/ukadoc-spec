# OnRecycleBinEmpty

**カテゴリ:** OS 狀態事件

使用[`\![execute,emptyrecyclebin]`](../../sakura-script/misc/bang-execute-emptyrecyclebin.md)清空資源回收筒時發生。<br />
除了執行指令的 ghost 之外，也會通知所有已啟動的 ghost，事件名稱為 OnRecycleBinEmptyFromOther。

- **Reference0**: 目前資源回收筒中的檔案數量（剛清空後通常為 0）
- **Reference1**: 目前資源回收筒中的檔案大小（剛清空後通常為 0），單位為位元組
- **Reference2**: 目前資源回收筒中的檔案數量與清空前的差值（剛清空後通常為負值）
- **Reference3**: 目前資源回收筒中的檔案大小與清空前的差值（剛清空後通常為負值），單位為位元組
- **Reference4**: 成功清空時為 1，發生錯誤時為 0（原本就是空的也為 0）
- **Reference5**: 執行標籤的 ghost 本體端名稱（sakuraname）。

**対応:** SSP 2.6.04/Ref4 為 2.6.35
