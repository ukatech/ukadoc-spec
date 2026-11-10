# `\![open,file,ファイル名]`

**カテゴリ:** 開啟指令

執行檔案。以相對於\[執行中的 ghost 資料夾\]/ghost/master/的路徑或絕對路徑指定。<br />
可以使用 Windows 環境變數（例如 %SYSTEMROOT%、%SYSTEM%、%TEMP%）。<br />
若檔名指定為可執行檔，會自動搜尋路徑。

**対応:** SSP

## 記述例

```sakurascript
\![open,file,shell/master/surface0.png]shell/masterフォルダのsurface0.pngが開かれる。
```

```sakurascript
\![open,file,%ComSpec%]コマンドプロンプトが実行される。
```

```sakurascript
\![open,file,TortoiseProc.exe]TortoiseSVNがインストールされていれば、パスを自動で検索して実行する。
```
