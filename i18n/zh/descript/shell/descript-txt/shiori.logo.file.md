# shiori.logo.file,文件名

**カテゴリ:** descript.txt

用作 AI 图表背景的图像文件名。<br />
显示多个图表时，加载在扩展名前加上数字的文件。<br />
例：指定 aigraph.png 时，加载 aigraph0.png、aigraph1.png…<br />
图像尺寸为 288x288px 时可填满图表绘制区域。<br />
深色模式下使用文件名末尾另加 \_dark 的文件。以上例而言，即 aigraph0_dark.png。如果不存在，则固定显示浅色模式。

也可写在 ghost 侧的 descript.txt 中。如果 shell 侧已指定，则优先使用 shell 侧的值；否则使用 ghost 侧的值。

**既定値:** ai.png（ai0.png、ai1.png…/ai0_dark.png、ai1_dark.png…），如果不存在则使用 baseware 的标准背景

**対応:** Materia 废止规格 / SSP 多个指定从 2.4.26 起支持，深色模式从 2.8.56 起支持
