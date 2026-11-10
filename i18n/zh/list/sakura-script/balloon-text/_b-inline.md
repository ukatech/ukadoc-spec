# `\_b[file path,inline]`

**カテゴリ:** Balloon, text commands

Embeds an image within a line of balloon text, treating it as one character.<br />
The base folder is \[the folder of the running ghost\]/ghost/master.<br />
※Instead of a file name, an image can be specified using base64 encoding or an exe/dll resource; [see below](note-1.md#補足).

**対応:** SSP / Ninix

## 記述例

```sakurascript
本体側バルーンに、[実行したゴーストのフォルダ]/ghost/masterフォルダにあるtest.png\_b[test.png,inline]を、現在のバルーン内の文字表示位置に、左上のドットを透過色として、表示する。
```
