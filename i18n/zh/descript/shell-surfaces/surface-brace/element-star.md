# element\*,绘制方法,文件名,X坐标,Y坐标(,选项...)

**カテゴリ:** surface大括号

基础surface合成。<br />
将多张图像合成为一张，并将合成结果作为基础surface处理的机制。<br />
如果存在与surface对应的surface\*.png图像，则定义element0时会丢弃原surface\*.png的内容，并替换为element0<br />
element1及之后的图像会依次合成在其上方。<br />
\*部分（elementID）是在同一surface内统一使用的、从0开始的连续编号。<br />
绘制方法请参阅以下[绘制方法](h-drowmethod/index.md)。<br />
如果在surface\*.png或element定义中指定动画GIF/APNG/WebP动画，则无需编写SERIKO定义也会自动播放动画（SSP 2.7.38～）。<br />
将通过element定义的surface用作动画部件时，也会像一张图像一样运行（SSP 2.3.53～；此前未定义）。

选项如下。需要指定多个选项时，可以像「element0,overlay,face.png,0,0,--clipping,10,10,50,50,--alpha,128」这样连续填写。

- **--clipping,左,上,右,下**: \[SSP 2.8.15～\]仅绘制由左、上、右、下指定的矩形区域。使用此选项后，动画加载将被禁用。<br />
  示例：element0,overlay,face.png,0,0,--clipping,10,10,50,50
- **--alpha,值(0-255)**: \[SSP 2.8.37～\]指定绘制时的不透明度。0为完全透明，255为完全不透明。<br />
  示例：element0,overlay,face.png,0,0,--alpha,128
- **--source,值**: \[SSP 2.8.41～\]从包含多个绘制候选项的图像或文件中，指定实际用于绘制的对象。<br />
  对于多页TIFF，指定从0开始的页码；对于DLL/EXE中的图标，指定从0开始的资源编号；对于PSD等文件，指定图层名称。<br />
  指定图层组中的图层时，使用::分隔并填写组名（支持嵌套图层组）。<br />
  仅当PSD等文件的图层信息中包含绘制方法信息时，才能将绘制方法设为auto。<br />
  当PSD等文件中指定的图层设有不透明度，且未指定alpha选项时，将自动使用图层的不透明度信息。<br />
  示例：element0,auto,face.png,0,0,--source,顔::頭
- **--scaling,横向,纵向**: \[SSP 2.8.73～\]将图像缩放到指定尺寸后进行合成。与clipping一起使用时，会缩放裁剪后的区域。<br />
  横向和纵向的数值末尾加%时，表示相对于原图（裁剪后）的百分比；未指定单位或末尾加px时，则按像素数处理。<br />
  数值为负数时，会按其绝对值指定的尺寸翻转图像，左右或上下显示。<br />
  \[SSP 2.8.82～\]横向或纵向其中一项指定为0时，会按照非0一项的尺寸缩放，同时保持原图的宽高比。<br />
  可指定的尺寸限制在1～4096px范围内。<br />
  示例：element0,overlay,face.png,0,0,--scaling,50%,50%<br />
  示例：element0,overlay,face.png,0,0,--scaling,150,0（原图为300x200时，结果为150x100）
- **--scaling,尺寸,基准边**: \[SSP 2.8.82～\]保持原图的宽高比进行缩放，使基准边达到指定尺寸后合成。尺寸仅能使用像素数，不能使用%。<br />
  基准边指定为long（长边）或short（短边）。<br />
  在基准边末尾加max时仅缩小（小于指定尺寸的图像不放大）；加min时仅放大（大于指定尺寸的图像不缩小）。<br />
  省略long・short而只填写max或min时，按指定了long处理。<br />
  尺寸为负数时，会按其绝对值指定的尺寸同时左右、上下翻转显示。<br />
  可指定的尺寸限制在1～4096px范围内。<br />
  示例：element0,overlay,face.png,0,0,--scaling,300,long（原图为400x300时，结果为300x225）<br />
  示例：element0,overlay,face.png,0,0,--scaling,300,longmax（仅当长边超过300px时缩小到300px）<br />
  示例：element0,overlay,face.png,0,0,--scaling,300,shortmin（仅当短边小于300px时放大到300px）

**既定値:** 无效果

**対応:** Materia / SSP / CROW
