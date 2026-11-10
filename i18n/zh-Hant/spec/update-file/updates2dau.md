# updates2.dau (Version 2)

This format uses byte value 1 as the field delimiter, and each line ends with CRLF.

- **Character encoding**: The default is the OS default charset. It can be specified by appending a `charset=character-encoding-name` field to the end of the first entry.

- **Line format**: Each line has the following format.

  ```
  ファイルパス\x01MD5ハッシュ\x01拡張フィールド1\x01拡張フィールド2\x01...
  ```

  `\x01` indicates byte value 1. Lines end with CRLF.

## Sample

```
ghost/master/descript.txt\x01a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4\x01size=1234\x01date=2024-01-15T12:34:56\x01charset=Shift_JIS\x01
ghost/master/shiori.dll\x01f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3\x01size=65536\x01date=2024-01-15T12:34:56\x01
shell/master/surface0.png\x01deadbeefdeadbeefdeadbeefdeadbeef\x01size=32768\x01date=2024-01-15T12:34:56\x01
```

※ `\x01` is actually byte value 1. `charset=` is appended only to the end of the first entry.
