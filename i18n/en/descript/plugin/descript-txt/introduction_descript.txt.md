# descript.txt (for plugins)

## Overview

The basic configuration file for a plugin.

## 記述例 and basic usage

```
charset,Shift_JIS
name,ダミープラグ
id,21AC84B0-6B1F-11E4-9803-0800200C9A66
filename,rei.dll
```

name, id, and filename are required.

Strings beginning with \\ or % are treated as Sakura Script or environment variable tags and discarded for security reasons. To include them as literal characters, they must be escaped, for example as \\\\ or \\%.
