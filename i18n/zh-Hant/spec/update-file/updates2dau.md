# updates2.dau (Version 2)

以位元組值 1 作為欄位分隔符，並以 CRLF 結束每一行的格式。

- **字元編碼**：預設為作業系統的預設 charset。可在第一個項目的末尾附加 `charset=文字編碼名稱` 欄位來指定。

- **行格式**：每一行的格式如下。

  ```
  ファイルパス\x01MD5ハッシュ\x01拡張フィールド1\x01拡張フィールド2\x01...
  ```

  `\x01` 表示位元組值 1。換行符號為 CRLF。

## 範例

```
ghost/master/descript.txt\x01a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4\x01size=1234\x01date=2024-01-15T12:34:56\x01charset=Shift_JIS\x01
ghost/master/shiori.dll\x01f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3\x01size=65536\x01date=2024-01-15T12:34:56\x01
shell/master/surface0.png\x01deadbeefdeadbeefdeadbeefdeadbeef\x01size=32768\x01date=2024-01-15T12:34:56\x01
```

※ `\x01` 實際上是位元組值 1。`charset=` 只會附加在第一個項目的末尾。
