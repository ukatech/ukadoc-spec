# `\_b[ファイルパス,inline]`

**カテゴリ:** Balloon, text command

Embeds an image within a line of balloon text, treating it as one character.<br />
\[The running ghost's folder\]/ghost/master is the base folder.<br />
※A base64-encoded string or a resource in an exe/dll can be specified as an image instead of a file name; [see below](note-1.md#補足).

**対応:** SSP / Ninix

## 記述例

```sakurascript
本体側バルーンに、[実行したゴーストのフォルダ]/ghost/masterフォルダにあるtest.png\_b[test.png,inline]を、現在のバルーン内の文字表示位置に、左上のドットを透過色として、表示する。
```
