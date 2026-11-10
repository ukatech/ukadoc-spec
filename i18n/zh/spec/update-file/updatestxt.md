# updates.txt (Version 3)

与updates2.dau一样以字节值1分隔，但这是各行带有行类型前缀的文本格式。

- **行类型**: 根据每行开头的前缀确定类型。既不是 `file,` 也不是 `charset,` 的行将被忽略。

  - **charset,字符编码名称**: 指定后续行的字符编码。写在文件开头附近。
  - **file,数据组...**: `file,` 前缀之后的内容与updates2.dau格式相同。

## 示例

```
charset,Shift_JIS
file,ghost/master/descript.txt\x01a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4\x01size=1234\x01date=2024-01-15T12:34:56\x01
file,ghost/master/shiori.dll\x01f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3\x01size=65536\x01date=2024-01-15T12:34:56\x01
file,shell/master/surface0.png\x01deadbeefdeadbeefdeadbeefdeadbeef\x01size=32768\x01date=2024-01-15T12:34:56\x01
```

※ `\x01` 实际上是字节值1。
