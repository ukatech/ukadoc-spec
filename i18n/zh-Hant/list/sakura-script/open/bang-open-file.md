# `\![open,file,ファイル名]`

**カテゴリ:** Open commands

Executes a file. Specify a relative path from \[the folder of the running ghost\]/ghost/master/ or an absolute path.<br />
Windows environment variables such as %SYSTEMROOT%, %SYSTEM%, and %TEMP% can be used.<br />
If the file name is an executable, its path is searched for automatically.

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
