# descript.txt（Plugin的）

## 概要

plugin的基本设置文件。

## 記述例与基本写法

```
charset,Shift_JIS
name,ダミープラグ
id,21AC84B0-6B1F-11E4-9803-0800200C9A66
filename,rei.dll
```

name、id、filename为必填项。

另外，以\\或%开头的字符串会被视为Sakura Script或环境变量标签，出于安全风险考虑会被丢弃。若要将它们作为普通字符使用，则需要用\\\\或\\%等形式进行转义。
