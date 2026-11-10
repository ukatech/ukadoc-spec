# OnURLDropped

**カテゴリ:** URL拖放事件

接收完已拖放的URL时触发。<br />
此事件在即将安装NAR、下载处理刚完成后触发。其他情况（安装homeurl或feed(RSS)）不会触发。

- **Reference0**: 已完成下载的文件的本地路径。
- **Reference1**: 已拖放的URL。
- **Reference2**: 已拖放的角色的scope编号。本体侧为0，搭档为1，第三人及之后为2以上。

**対応:** Materia / SSP Ref1,2自2.6.36起支持 / CROW
