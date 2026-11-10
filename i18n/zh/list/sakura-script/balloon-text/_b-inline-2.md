# `\_b`\[文件路径,inline,[选项](note-1.md#_bファイルパスについて),选项...\]

**カテゴリ:** 气球、文本命令

将图像插入气球的文本行内，并按一个字符处理。<br />
\[已执行的 ghost 的文件夹\]/ghost/master 是基准文件夹。<br />
※可以使用 base64 编码或 exe/dll 资源代替文件名来指定图像，[※参见下文](note-1.md#補足)。

可指定的选项请参见[※下文](note-1.md#_bファイルパスについて)。

## 記述例

```sakurascript
本体側バルーンに、[実行したゴーストのフォルダ]/ghost/masterフォルダにあるtest.png\_b[test.png,inline,--option=use_self_alpha,--clipping=100 30 150 90]を、文字扱い、ファイルの透過情報付きpngとして、画像の横100～150pixel縦30～90pixelの範囲を表示する。
```

**対応:** SSP
