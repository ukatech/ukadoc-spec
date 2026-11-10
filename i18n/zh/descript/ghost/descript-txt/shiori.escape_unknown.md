# shiori.escape_unknown,0/1

**カテゴリ:** descript.txt

与 SHIORI 通信时，如果存在无法转换为所用字符编码的 Unicode 字符，则使用特殊转义，以尽可能避免这些字符完全无法识别。<br />
具体来说，会将无法转换的字符串改写为类似 ?escape!unicode\[0xABCD\] 的特殊形式后传给 SHIORI；如果 SHIORI 以相同形式返回，则会将其正确转换回来。

**既定値:** 0（false）

**対応:** SSP 2.6.89
