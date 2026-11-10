# OnDisplayChangeEx

**カテゴリ:** OS 狀態事件

螢幕的解析度／色深變更時觸發。支援多螢幕。*\[啟動時NOTIFY/其他GET\]*

- **Reference0**: init（啟動時通知）或 update（啟動後更新）
- **Reference1～**: 左、上、右、下、位元深度、是否為主要螢幕（0/1）、工作列位置（left,top,right,bottom,unknown）、工作列與工作區域的分界座標<br />
  範例： 0,0,1600,900,32,1,bottom,1560<br />
  在[視窗模式](OnWindowModeChange.md)中，僅有一筆資料，將容器的用戶端區域視為一個螢幕（範例： 0,0,1280,720,32,1,unknown,0）。實體螢幕變更時不會觸發；容器尺寸變更或切換視窗模式時會觸發。

**対応:** SSP 2.4.09/工作列支援為2.6.35
