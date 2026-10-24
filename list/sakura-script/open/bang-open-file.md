# `\![open,file,ファイル名]`

**カテゴリ:** オープンコマンド

ファイルを実行する。\[実行したゴーストのフォルダ\]/ghost/master/からの相対パスか、絶対パスで指定。<br />
windowsの環境変数(%SYSTEMROOT%,%SYSTEM%,%TEMP%等)を使う事ができる。<br />
ファイル名に実行ファイルを指定した場合、自動でパス探索する。

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
