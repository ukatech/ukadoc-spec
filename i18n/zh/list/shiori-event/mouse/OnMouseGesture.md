# OnMouseGesture

**カテゴリ:** 鼠标事件

使用鼠标右键拖动或拖动滚轮时触发。<br />
另外，从 SSP 2.3.53 起，在触摸屏环境中，如果 SHIORI 对 Reference5 为 up 或 down 的 OnMouseGesture 没有返回任何内容（返回了 204 No Content），则会触发替代事件 [OnMouseWheel](OnMouseWheel.md)。详情请参阅 OnMouseWheel 一节。

- **Reference0**: 对于本体为 0，对于搭档为 1。SSP/CROW 中也可能为 2 或更大。
- **Reference1**: 鼠标光标的 xy 坐标（以字节值 1 分隔）
- **Reference2**: 命中区域的标识符。
- **Reference3**: 开始右键拖动时鼠标光标的 xy 坐标（以字节值 1 分隔）
- **Reference4**: 开始右键拖动时的命中区域标识符。
- **Reference5**: 手势方向。<br />
  left_up（左上） up（上） right_up（右上）<br />
  left（左） right（右）<br />
  left_down（左下） down（下） right_down（右下）<br />
  circle.cw（顺时针） circle.ccw（逆时针）<br />
  end（松开鼠标右键）
- **Reference6**: 手势移动角度。<br />
  从右侧的 0 度开始，逆时针旋转 360 度。

**対応:** SSP
