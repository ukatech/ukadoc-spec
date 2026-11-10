# descript.txt (for Headline)

## Overview

The basic configuration file for a headline sensor.

## 記述例 and basic usage

```
charset,Shift_JIS
name,ダミーサイト
dllname,dummy.dll
url,http://ほげほげ/hoge.html
openurl,http://ほげほげ/spec/
```

name, dllname, url, and openurl are required.

Strings beginning with \\ or % are treated as Sakura Script or environment-variable tags and discarded due to security risks. To include them as literal characters, they must be escaped, for example as \\\\ or \\%.
