# `\j[ID]`

**カテゴリ:** Open command

Jump to the specified ID.<br />
Jump to a URL beginning with http://～.<br />
Execute a file with the extension associated with the OS using file:///～. In addition to an absolute path, a path relative to \[the folder of the executing ghost\]/ghost/master can be used as the file name.<br />
※SSP only: use mailto:～ to compose a new email addressed to the specified recipient.

**対応:** Materia / SSP / CROW / Ninix

## 記述例

```sakurascript
\j[http://ssp.shillest.net/]ばぐとら研究所をブラウザを立ち上げて表示する。
```

```sakurascript
\j[file:///descript.txt][実行したゴーストのフォルダ]/ghost/masterフォルダにあるdescript.txtを開く。
```
