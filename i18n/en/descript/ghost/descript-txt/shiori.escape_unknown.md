# shiori.escape_unknown,0/1

**カテゴリ:** descript.txt

When a Unicode character cannot be converted to the character encoding used for communication with SHIORI, applies a special escape to avoid, as much as possible, the situation where the character is not recognized as text at all.<br />
Specifically, a string that cannot be converted is rewritten in a special form such as ?escape!unicode\[0xABCD\] and passed to SHIORI; if SHIORI returns it in the same form, it is converted back appropriately.

**既定値:** 0 (false)

**対応:** SSP 2.6.89
