# `\_b[ファイルパス,x,y]`

**カテゴリ:** Balloon, text command

Paste an image at the balloon's XY coordinates. The image is displayed underneath the text.<br />
The color of the top-left pixel becomes transparent.<br />
The base folder is \[folder of the ghost that executed this\]/ghost/master.<br />
※Only SSP allows base64-encoded data or an exe/dll resource to be specified as the image instead of a filename; [see below](note-1.md#補足).<br />
※Only SSP allows an image URL to be specified.<br />
※Only SSP also searches for files in the plugin folder.

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
\_b[image\test.png,50,100]本体側バルーンに、[実行したゴーストのフォルダ]/ghost/master/imageフォルダにあるtest.pngを左上のpixelを透過色として、バルーン内座標X:50,Y:100に表示する。
```
