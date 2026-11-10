# element\*,DrawingMethod,Filename,X coordinate,Y coordinate(,Options...)

**カテゴリ:** surface directive

Compositing the base surface.<br />
A mechanism for compositing multiple images and treating the result as a single image serving as the base surface.<br />
If an image named surface\*.png corresponding to the surface exists, defining element0 discards the contents of the original surface\*.png and replaces them with element0<br />
element1 and later are composited on top of it in sequence.<br />
The \* portion (elementID) is a sequential number starting at 0, consistent within the same surface.<br />
See [drawing methods](h-drowmethod/index.md) below for drawing methods.<br />
If an animated GIF/APNG/animated WebP is specified for surface\*.png or an element definition, it will animate automatically without a SERIKO definition (SSP 2.7.38～).<br />
A surface defined with element also behaves like a single image when used as an animation part (SSP 2.3.53～; behavior was undefined before that).

The options are as follows. Multiple options can be specified consecutively, as in "element0,overlay,face.png,0,0,--clipping,10,10,50,50,--alpha,128".

- **--clipping,left,top,right,bottom**: \[SSP 2.8.15～\]Draws only the rectangular area specified by left, top, right, and bottom. Using this disables animation loading.<br />
  Example: element0,overlay,face.png,0,0,--clipping,10,10,50,50
- **--alpha,value(0-255)**: \[SSP 2.8.37～\]Specifies the opacity when drawing. 0 is fully transparent; 255 is fully opaque.<br />
  Example: element0,overlay,face.png,0,0,--alpha,128
- **--source,value**: \[SSP 2.8.41～\]Specifies the item to actually draw from an image or file that has multiple drawing candidates.<br />
  For a multipage TIFF, specify the zero-based page number; for an icon in a DLL/EXE, specify the zero-based resource number; for a PSD or similar file, specify the layer name.<br />
  To specify a layer inside a layer group, write the group name, separated by :: (nested groups are supported).<br />
  The drawing method can be set to auto only when the format, such as PSD, includes drawing method information in its layer information.<br />
  If the specified layer in a PSD or similar file has an opacity setting, that layer opacity information is used automatically when the alpha option is not specified.<br />
  Example: element0,auto,face.png,0,0,--source,顔::頭
- **--scaling,horizontal,vertical**: \[SSP 2.8.73～\]Scales the image to the specified size before compositing. If used with clipping, scaling is applied to the clipped area.<br />
  Append % to the horizontal or vertical value to specify a percentage of the original image (after clipping); if omitted or followed by px, the value is treated as a number of pixels.<br />
  A negative value flips the image horizontally or vertically, using its absolute value as the size.<br />
  \[SSP 2.8.82～\]If one of horizontal or vertical is set to 0, the image is scaled to fit the nonzero dimension while preserving the original aspect ratio.<br />
  The specified size is limited to the range of 1–4096px.<br />
  Example: element0,overlay,face.png,0,0,--scaling,50%,50%<br />
  Example: element0,overlay,face.png,0,0,--scaling,150,0 (if the original image is 300x200, the result is 150x100)
- **--scaling,size,reference side**: \[SSP 2.8.82～\]Scales the image while preserving its original aspect ratio so that the reference side is the specified size. The size must be in pixels; % cannot be used.<br />
  Specify long (longer side) or short (shorter side) for the reference side.<br />
  Append max to the reference side to only scale down (images smaller than the specified size are not enlarged); append min to only scale up (images larger than the specified size are not reduced).<br />
  If long or short is omitted and only max or min is written, long is assumed.<br />
  A negative size flips the image both horizontally and vertically, using its absolute value as the size.<br />
  The specified size is limited to the range of 1–4096px.<br />
  Example: element0,overlay,face.png,0,0,--scaling,300,long (if the original image is 400x300, the result is 300x225)<br />
  Example: element0,overlay,face.png,0,0,--scaling,300,longmax (scales down to 300px only if the longer side exceeds 300px)<br />
  Example: element0,overlay,face.png,0,0,--scaling,300,shortmin (scales up to 300px only if the shorter side is less than 300px)

**既定値:** No effect

**対応:** Materia / SSP / CROW
