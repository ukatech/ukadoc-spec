# descript.txt（Headlineの）

## 概要

ヘッドラインセンサの基本設定ファイル。

## 記述例と基本の書き方

```
charset,Shift_JIS
name,ダミーサイト
dllname,dummy.dll
url,http://ほげほげ/hoge.html
openurl,http://ほげほげ/spec/
```

name、dllname、url、openurlは必須。

なお、\\や%で始まる文字列はさくらスクリプトや環境変数のタグと見なされ、セキュリティ上のリスクから破棄される。もし単なる文字としてそれらを含めたい場合は、\\\\や\\%などとしてエスケープする必要がある。
