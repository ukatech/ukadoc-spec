# OnMouseDown

**カテゴリ:** 鼠标事件

按下鼠标左键或右键时触发。

- **Reference0**: 鼠标光标的 x 坐标（局部坐标）
- **Reference1**: 鼠标光标的 y 坐标（局部坐标）
- **Reference2**: 始终为0。
- **Reference3**: 本体为0，搭档为1。SSP/CROW中也可能为2及以上。
- **Reference4**: 命中区域的标识符。
- **Reference5**: 左键单击为0，右键单击为1，中键单击为2（兼容规格：建议改用OnMouseClickEx）。
- **Reference6**: 来自支持多点触控的环境中的触摸屏（※不包括触摸板）的输入为touch，来自数位板的输入为pen，来自数位板橡皮擦端的输入为eraser，来自鼠标等设备的输入为mouse

**対応:** SSP / Ninix
