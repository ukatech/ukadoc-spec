# OnMouseWheel

**カテゴリ:** 鼠标事件

鼠标滚轮转动时触发。<br />
从SSP2.3.53开始，在触摸屏环境下，如果SHIORI对[OnMouseGesture](OnMouseGesture.md)的Reference5为up或down的事件未返回任何内容（返回204 No Content），则也会触发OnMouseWheel作为替代事件。此时，Reference2的数值会根据原始OnMouseGesture的移动量及up・down方向进行转换（up为正数，down为负数）。

- **Reference0**: 鼠标光标的 x 坐标（局部坐标）
- **Reference1**: 鼠标光标的 y 坐标（局部坐标）
- **Reference2**: 鼠标滚轮的转动量及转动方向。
- **Reference3**: 主角色为0，搭档为1。SSP/CROW中还可能有2及以上的值。
- **Reference4**: 命中判定的标识符。
- **Reference5**: ※仅限SSP/NINIX　始终为0。
- **Reference6**: ※仅限SSP/NINIX　来自支持多点触控环境的触摸屏（※不包括触摸板）的输入为touch，来自数位板的输入为pen，来自数位板橡皮擦端的输入为eraser，来自鼠标等设备的输入为mouse

**対応:** Materia / SSP / CROW / Ninix
