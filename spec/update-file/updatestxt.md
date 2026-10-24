# updates.txt (Version 3)

updates2.dauと同じバイト値1区切りだが、各行に行種別プレフィックスを持つテキスト形式である。

- **行種別**: 各行は行頭のプレフィックスにより種別が決まる。`file,` でも `charset,` でもない行は無視される。

  - **charset,文字コード名**: 以降の行の文字コードを指定する。ファイル先頭付近に記述する。
  - **file,データ群...**: `file,` プレフィックスの後の内容はupdates2.dauと同一フォーマットである。

## サンプル

```
charset,Shift_JIS
file,ghost/master/descript.txt\x01a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4\x01size=1234\x01date=2024-01-15T12:34:56\x01
file,ghost/master/shiori.dll\x01f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3\x01size=65536\x01date=2024-01-15T12:34:56\x01
file,shell/master/surface0.png\x01deadbeefdeadbeefdeadbeefdeadbeef\x01size=32768\x01date=2024-01-15T12:34:56\x01
```

※ `\x01` は実際にはバイト値1である。
