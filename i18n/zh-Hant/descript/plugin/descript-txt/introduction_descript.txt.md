# descript.txt（Plugin）

## 概要

plugin 的基本設定檔案。

## 記述例與基本寫法

```
charset,Shift_JIS
name,ダミープラグ
id,21AC84B0-6B1F-11E4-9803-0800200C9A66
filename,rei.dll
```

name、id、filename 為必填。

此外，以 \\ 或 % 開頭的字串會被視為 Sakura Script 或環境變數標籤，基於安全風險會遭到丟棄。若要將這些字元作為一般文字使用，必須以 \\\\ 或 \\% 等方式跳脫。
