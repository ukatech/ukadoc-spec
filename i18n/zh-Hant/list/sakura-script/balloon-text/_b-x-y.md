# `\_b[ファイルパス,x,y]`

**カテゴリ:** balloon, text command

Paste an image at the balloon's XY coordinates. The image is displayed behind the text.<br />
The color of the upper-left pixel is used as the transparent color.<br />
\[folder of the running ghost\]/ghost/master is the base folder.<br />
※Only SSP lets you specify a base64-encoded image or an image resource from an exe/dll instead of a file name. [※See below](note-1.md#補足).<br />
※Only SSP lets you specify an image URL.<br />
※Only SSP searches for files in the plugin folder as well.

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
\_b[image\test.png,50,100]本体側バルーンに、[実行したゴーストのフォルダ]/ghost/master/imageフォルダにあるtest.pngを左上のpixelを透過色として、バルーン内座標X:50,Y:100に表示する。
```
