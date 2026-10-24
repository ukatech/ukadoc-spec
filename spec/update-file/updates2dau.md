# updates2.dau (Version 2)

バイト値1をフィールド区切りとし、各行をCRLFで終端する形式である。

- **文字コード**: デフォルトはOSデフォルトのcharset。先頭エントリの末尾に `charset=文字コード名` フィールドを付加することで指定できる。

- **行フォーマット**: 各行は以下の形式である。

  ```
  ファイルパス\x01MD5ハッシュ\x01拡張フィールド1\x01拡張フィールド2\x01...
  ```

  `\x01` はバイト値1を示す。改行はCRLF。

## サンプル

```
ghost/master/descript.txt\x01a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4\x01size=1234\x01date=2024-01-15T12:34:56\x01charset=Shift_JIS\x01
ghost/master/shiori.dll\x01f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3\x01size=65536\x01date=2024-01-15T12:34:56\x01
shell/master/surface0.png\x01deadbeefdeadbeefdeadbeefdeadbeef\x01size=32768\x01date=2024-01-15T12:34:56\x01
```

※ `\x01` は実際にはバイト値1である。`charset=` は先頭エントリの末尾にのみ付加される。
