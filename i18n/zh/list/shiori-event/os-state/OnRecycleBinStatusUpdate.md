# OnRecycleBinStatusUpdate

**カテゴリ:** OS 状态事件

向回收站中放入文件或在资源管理器中清空回收站时发生，并通知所有正在运行的 ghost。<br />
此外，在 ghost 启动时也会通过*\[NOTIFY\]*通知。

- **Reference0**: 当前回收站中的文件数
- **Reference1**: 当前回收站中文件的大小，单位为字节
- **Reference2**: 当前回收站中的文件数与之前的差值
- **Reference3**: 当前回收站中文件大小与之前的差值，单位为字节
- **Reference4**: 始终为1（用于兼容OnRecycleBinEmpty的虚拟值）
- **Reference5**: 始终为空（用于兼容OnRecycleBinEmpty的虚拟值）

**対応:** SSP 2.6.04/Ref4为2.6.35
