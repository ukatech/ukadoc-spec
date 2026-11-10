# OnURLQuery

**カテゴリ:** URL拖放事件

URL被拖放到角色窗口时会收到通知。<br />
对此返回脚本后，通常的下载处理会被取消。<br />
只有在ghost侧需要自行处理URL时才返回脚本。

- **Reference0**: URL路径。
- **Reference1**: 本体侧为0，搭档侧为1。SSP/CROW中还可能为2以上。
- **Reference2**: 已拖放URL的MIME类型
- **Reference3**: 如果未作出响应，SSP接下来预定执行的处理。<br />
  为feed、nar、homeurl、ical、ssf、unknown中的一种。<br />
  如果是unknown，则表示本体无法处理该URL，本体侧不能再进行后续处理。<br />
  其他情况下，将其与Reference0一起原样传递给 [`\![execute,dropdefault,url]`](../../sakura-script/misc/bang-execute-dropdefault-file-.-bang-execute-dropdefault-url-URL.md)\[2.9.10\] 或 [`\![execute,install,url]`](../../sakura-script/misc/bang-execute-install-url-URL.md)，即可继续处理。

**対応:** SSP的Ref3自2.6.35起支持
