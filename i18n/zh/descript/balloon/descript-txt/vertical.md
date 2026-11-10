# vertical,0/1

**カテゴリ:** descript.txt

指定1时，此气球中的文本将以日语竖排方式显示（文字从上向下排列，行从右向左排列）。

设为竖排后，descript.txt中坐标指定的含义会变为如下所示。坐标本身仍和以往一样，以气球图像的左上角为原点填写。

- origin.x … *第1列的右端*。从这里开始向左排列各列。通常不指定，而是交由validrect的定义处理。
- origin.y … 文字排列的起始位置（第1个字符的上端）。通常不指定，而是交由validrect的定义处理。
- validrect … 不变。文本允许绘制的范围。
- 换行位置通过[wordwrappoint.y](wordwrappoint.y.md)指定。wordwrappoint.x会被忽略。
- SSTP消息的显示结束位置通过[sstpmessage.yb](sstpmessage.yb.md)指定。sstpmessage.xr会被忽略。
- [number.y](number.y.md)（＝number.yb） … 计数器数值的*下端*。数值从这里开始向上延伸。[number.x](number.x.md)（＝number.xr）则是数值所在列的位置。

对于origin.x或number.x等以右端为基准的坐标，可以按照[\*1](../index.md#balloon設定)的规则用负值书写（例如：origin.x,-14表示距离气球图像右端14像素）。

字体会自动使用指定字体名称对应的竖排变体（字体名称前加@的字体）。<br />
如果指定的字体没有竖排变体（例如放置在气球文件夹中的字体文件或西文字体），则会自动替换为系统标准黑体的竖排变体。

此外，请注意，以下项目会按照“以文字排列方向为基准的方向”而不是“画面上的方向”生效。

- `\f[align,～]`用于列内文字对齐（left＝顶部对齐，right＝底部对齐），`\f[valign,～]`用于行厚度方向的对齐（top＝右侧对齐，bottom＝左侧对齐）。
- arrow0（向上滚动）和arrow1（向下滚动）在含义上分别变为向右和向左滚动。图像和位置需由气球提供。
- 下划线（font.underline、`\f[underline,true]`、锚点下划线）会绘制在列的右侧。

限制：SSTP标记的发送源显示和网络更新进度显示也会以竖排方式绘制。输入框（communicatebox）仍保持横排。

也可以在气球各个表面的[balloon(s/k)\*s.txt](../balloonsoption/index.md)中指定，但如果在同一个气球内按表面切换竖排和横排，切换前显示的文本布局会错乱。

**既定値:** 0（横排）

**対応:** SSP 2.8.80
