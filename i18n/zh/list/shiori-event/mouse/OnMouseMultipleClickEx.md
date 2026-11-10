# OnMouseMultipleClickEx

**カテゴリ:** 鼠标事件

使用左、右键以外的按键连续点击 3 次或更多次时触发。<br />
※如果 SHIORI 未对此事件作出响应，则会按通常流程返回 OnMouseClickEx 和 OnMouseDoubleClickEx。

- **Reference0**: 鼠标光标的 x 坐标（局部坐标）
- **Reference1**: 鼠标光标的 y 坐标（局部坐标）
- **Reference2**: 始终为 0。
- **Reference3**: 对于本体为 0，对于搭档为 1，此后为 2 或更大
- **Reference4**: 命中区域的标识符。
- **Reference5**: 滚轮单击（或三键鼠标的中键）为 middle，扩展按键 1（通常分配给“后退”）为 xbutton1，扩展按键 2（通常分配给“前进”）为 xbutton2。
- **Reference6**: 来自支持多点触控环境的触摸屏（※不包括触摸板）的输入为 touch，来自数位板的输入为 pen，来自数位板橡皮擦端的输入为 eraser，来自鼠标等设备的输入为 mouse
- **Reference7**: 连续点击次数

**対応:** SSP
