# OnMouseMultipleClick

**カテゴリ:** 鼠标事件

连续点击 3 次或更多次时触发。<br />
※如果 SHIORI 未对此事件作出响应，则会按通常流程返回 OnMouseClick 和 OnMouseDoubleClick。

- **Reference0**: 鼠标光标的 x 坐标（局部坐标）
- **Reference1**: 鼠标光标的 y 坐标（局部坐标）
- **Reference2**: 始终为 0。
- **Reference3**: 对于本体为 0，对于搭档为 1，此后为 2 或更大
- **Reference4**: 命中区域的标识符。
- **Reference5**: 左键单击为 0，右键单击为 1
- **Reference6**: 来自支持多点触控环境的触摸屏（※不包括触摸板）的输入为 touch，来自数位板的输入为 pen，来自数位板橡皮擦端的输入为 eraser，来自鼠标等设备的输入为 mouse
- **Reference7**: 连续点击次数

**対応:** SSP
