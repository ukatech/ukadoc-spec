# `\![open,file,ファイル名]`

**カテゴリ:** 打开命令

执行文件。使用相对于\[当前运行的ghost文件夹\]/ghost/master/的路径，或使用绝对路径指定。<br />
可以使用windows环境变量（如%SYSTEMROOT%、%SYSTEM%、%TEMP%等）。<br />
如果文件名指定为可执行文件，会自动搜索路径。

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
