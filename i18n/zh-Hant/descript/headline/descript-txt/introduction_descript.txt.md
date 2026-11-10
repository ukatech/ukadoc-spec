# descript.txt（Headline 的）

## 概要

headline sensor 的基本設定檔。

## 記述例與基本寫法

```
charset,Shift_JIS
name,ダミーサイト
dllname,dummy.dll
url,http://ほげほげ/hoge.html
openurl,http://ほげほげ/spec/
```

name、dllname、url、openurl 為必填。

另外，以\\或%開頭的字串會被視為 Sakura Script 或環境變數標籤，基於安全風險會被丟棄。若要將這些字元當作一般文字使用，必須以\\\\或\\%等方式跳脫。
