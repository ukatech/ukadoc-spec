# OnWindowModeChange

**カテゴリ:** OS 狀態事件

SSP 的視窗模式切換時發生。*\[啟動時NOTIFY/其他GET\]*<br />
視窗模式是指將 ghost 顯示在 SSP 提供的視窗（容器）中，而非桌面上的模式。對 ghost 而言，容器內部就是畫面。<br />
切換後 ghost 的畫面大小會改變，因此此事件之後也會發生 [OnDisplayChange](OnDisplayChange.md)。<br />
目前的模式也可以透過 [baseware.windowmode](../../propertysystem/property-system/baseware.windowmode.md) 取得。

- **Reference0**: init（啟動時通知）或 update（啟動後切換）
- **Reference1**: 目前模式。<br />
  normal：一般模式（在桌面上顯示 ghost）<br />
  shared：視窗模式。所有 ghost 共用一個容器<br />
  perghost：視窗模式。每個 ghost 使用一個容器
- **Reference2**: 前一個模式。值的種類與 Reference1 相同。Reference0 為 init 時是空值。

**対応:** SSP 2.8.93
