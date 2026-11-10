# updates2.dau (Version 2)

以字节值1作为字段分隔符，每行以CRLF结尾。

- **字符编码**: 默认为OS默认charset。可在首个条目的末尾添加 `charset=字符编码名称` 字段进行指定。

- **行格式**: 每行的格式如下。

  ```
  ファイルパス\x01MD5ハッシュ\x01拡張フィールド1\x01拡張フィールド2\x01...
  ```

  `\x01` 表示字节值1。换行符为CRLF。

## 示例

```
ghost/master/descript.txt\x01a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4\x01size=1234\x01date=2024-01-15T12:34:56\x01charset=Shift_JIS\x01
ghost/master/shiori.dll\x01f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3\x01size=65536\x01date=2024-01-15T12:34:56\x01
shell/master/surface0.png\x01deadbeefdeadbeefdeadbeefdeadbeef\x01size=32768\x01date=2024-01-15T12:34:56\x01
```

※ `\x01` 实际上是字节值1。`charset=` 仅添加在首个条目的末尾。
