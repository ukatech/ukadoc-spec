# updates.txt (Version 3)

與 updates2.dau 一樣，以位元組值 1 分隔，但這是具有行種類前綴的文字格式。

- **行種類**：每一行的種類由行首前綴決定。不是 `file,` 或 `charset,` 的行會被忽略。

  - **charset,文字編碼名稱**：指定後續行的字元編碼。請寫在檔案開頭附近。
  - **file,資料群...**：`file,` 前綴後的內容與 updates2.dau 格式相同。

## 範例

```
charset,Shift_JIS
file,ghost/master/descript.txt\x01a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4\x01size=1234\x01date=2024-01-15T12:34:56\x01
file,ghost/master/shiori.dll\x01f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3\x01size=65536\x01date=2024-01-15T12:34:56\x01
file,shell/master/surface0.png\x01deadbeefdeadbeefdeadbeefdeadbeef\x01size=32768\x01date=2024-01-15T12:34:56\x01
```

※ `\x01` 實際上是位元組值 1。
