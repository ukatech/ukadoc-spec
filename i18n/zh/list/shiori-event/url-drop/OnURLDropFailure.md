# OnURLDropFailure

**カテゴリ:** URL拖放事件

接收已拖放的URL失败或被取消时触发。<br />
此事件在尝试安装NAR失败时触发。其他情况（安装homeurl或feed(RSS)）不会触发。

- **Reference0**: 已完成下载的文件的本地路径。
- **Reference1**: [※失败原因](../network-update/caption_updateresultfailure.md)
- **Reference2**: 已拖放的URL。
- **Reference3**: 已拖放的角色的scope编号。本体侧为0，搭档为1，第三人及之后为2以上。

**対応:** Materia / SSP Ref2,3自2.6.36起支持 / CROW
