# `\_b[文件路径,inline]`

**カテゴリ:** 气球、文本命令

将图像插入气球的文本行内，并按一个字符处理。<br />
\[已执行的 ghost 的文件夹\]/ghost/master 是基准文件夹。<br />
※可以使用 base64 编码或 exe/dll 资源代替文件名来指定图像，[※参见下文](note-1.md#補足)。

**対応:** SSP / Ninix

## 記述例

```sakurascript
本体側バルーンに、[実行したゴーストのフォルダ]/ghost/masterフォルダにあるtest.png\_b[test.png,inline]を、現在のバルーン内の文字表示位置に、左上のドットを透過色として、表示する。
```
