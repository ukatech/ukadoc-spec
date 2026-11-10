# OnDisplayChangeEx

**カテゴリ:** OS状态事件

屏幕的分辨率／色深发生更改时触发。支持多显示器。*\[启动时NOTIFY/其他GET\]*

- **Reference0**: init (启动时通知) 或 update (启动后的更新)
- **Reference1～**: 左、上、右、下、位深、是否为主显示器(0/1)、任务栏位置(left,top,right,bottom,unknown)、任务栏与工作区域的分界坐标<br />
  示例： 0,0,1600,900,32,1,bottom,1560<br />
  在[窗口模式](OnWindowModeChange.md)下，只会有一条记录，并将容器客户区作为一个屏幕(示例： 0,0,1280,720,32,1,unknown,0)。实际显示器更改时不会触发；容器大小更改或切换窗口模式时会触发。

**対応:** SSP 2.4.09/任务栏为2.6.35
