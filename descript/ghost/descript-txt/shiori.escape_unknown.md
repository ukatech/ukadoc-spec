# shiori.escape_unknown,0/1

**カテゴリ:** descript.txt

SHIORIとの通信中の文字コードに変換できないUnicode文字があった時に、特殊なエスケープを行い、まったく文字として認識できない事態を最低限回避する。<br />
具体的には、?escape!unicode\[0xABCD\]のような形で、変換できない文字列を特別な形態に書き換えてSHIORIに渡し、同じ形態のままSHIORIから返ってきた時に適切に再変換する。

**既定値:** 0(false)

**対応:** SSP 2.6.89
