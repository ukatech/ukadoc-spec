# descript.txt (for Headline)

## Overview

Basic configuration file for the headline sensor.

## 記述例 and basic writing

```
charset,Shift_JIS
name,ダミーサイト
dllname,dummy.dll
url,http://ほげほげ/hoge.html
openurl,http://ほげほげ/spec/
```

name, dllname, url, and openurl are required.

Strings beginning with \\ or % are treated as Sakura Script or environment variable tags and discarded as a security measure. To include them as literal characters, escape them as \\\\ or \\%.
