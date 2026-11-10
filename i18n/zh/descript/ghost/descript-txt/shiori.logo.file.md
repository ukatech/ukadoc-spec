# shiori.logo.file,文件名

**カテゴリ:** descript.txt

指定用于 AI 图表背景的图像文件名。<br />
显示多个图表时，会读取在扩展名前加上数字的文件。<br />
例：指定 aigraph.png 时，会读取 aigraph0.png、aigraph1.png…<br />
图像尺寸为 288x288px，会铺满图表绘制区域。<br />
暗色模式下，会使用文件名后附加\_dark的文件。以上述示例为例，即 aigraph0_dark.png。文件不存在时，固定显示亮色模式。

**既定値:** ai.png（ai0.png、ai1.png…/ai0_dark.png、ai1_dark.png…），若不存在则使用 baseware 标准背景

**対応:** Materia 废止规格 / SSP 多文件指定自 2.4.26 起支持 暗色模式自 2.8.56 起支持
