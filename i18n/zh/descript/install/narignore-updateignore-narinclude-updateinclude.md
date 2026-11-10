# .narignore / .updateignore / .narinclude / .updateinclude

## .narignore / .updateignore

为了比developer_options.txt的写法更加灵活，.narignore/.updateignore允许直接使用.gitignore的写法。

写法请参阅 [.gitignore手册](https://git-scm.com/docs/gitignore/ja)，或者向LLM（文本生成AI）描述需求并让其生成。

但与.gitignore不同，即使放在子目录中也不会生效。只有放在ghost根目录下时才有效。

作为伺か专用的特殊功能，可以使用include:指定。例如<br />
include:.narignore<br />
这样写时，会将.narignore文件的全部内容视为插入在这一行的位置来处理。

include:指定的相对路径并非以ghost根目录为基准，而是以写有该行的文件所在目录为基准解析。也可以在读取的文件中继续写include:；此时基准目录会依次更新为“当前读取的文件所在目录”（基准会从父级移至子级，再从子级移至孙级）。

递归读取有深度上限，最多可遍历3层。超过该深度的include:会被拒绝读取。路径分隔符可以使用 / 或 \\。

例如，在ghost根目录下的.narinclude中写入include:sub/extra.txt，会读取sub/extra.txt。如果在该extra.txt中继续写入include:foo.txt，则会以extra.txt所在的sub/目录为基准，而不是ghost根目录，读取sub/foo.txt。

**対応:** SSP

## .narinclude / .updateinclude

这是.narignore/.updateignore的白名单版本。只有写在这里的内容才会包含在更新文件/NAR中。<br />
对子目录的处理方式与gitignore不同，例如只写shell/master而不写shell/，也会正确地包含父目录并进行处理。

此外，与.narignore/.updateignore一样，它也与.gitignore不同，即使放在子目录中也不会生效。只有放在ghost根目录下时才有效。

**対応:** SSP
