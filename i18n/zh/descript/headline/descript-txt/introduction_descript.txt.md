# descript.txt（Headline的）

## 概要

Headline sensor的基本设置文件。

## 記述例与基本写法

```
charset,Shift_JIS
name,ダミーサイト
dllname,dummy.dll
url,http://ほげほげ/hoge.html
openurl,http://ほげほげ/spec/
```

name、dllname、url、openurl为必填项。

另外，以\\或%开头的字符串会被视为Sakura Script或环境变量标签，并因安全风险而被丢弃。若要将它们作为普通字符使用，则必须使用\\\\或\\%等形式进行转义。
