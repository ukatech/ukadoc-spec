# updates.txt (Version 3)

Like updates2.dau, this format uses byte value 1 as the delimiter, but is a text format in which each line has a line-type prefix.

- **Line type**: The type of each line is determined by its prefix. Lines that are neither `file,` nor `charset,` are ignored.

  - **charset,character encoding name**: Specifies the character encoding for subsequent lines. Write this near the beginning of the file.
  - **file,data...**: The content following the `file,` prefix uses the same format as updates2.dau.

## Example

```
charset,Shift_JIS
file,ghost/master/descript.txt\x01a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4\x01size=1234\x01date=2024-01-15T12:34:56\x01
file,ghost/master/shiori.dll\x01f6e5d4c3b2a1f6e5d4c3b2a1f6e5d4c3\x01size=65536\x01date=2024-01-15T12:34:56\x01
file,shell/master/surface0.png\x01deadbeefdeadbeefdeadbeefdeadbeef\x01size=32768\x01date=2024-01-15T12:34:56\x01
```

※ `\x01` is actually byte value 1.
