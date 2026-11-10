# OnInstallCompleteAll

**カテゴリ:** 安装事件

例如通过拖放多个 nar 进行安装时，所有项目均**成功**安装后，此事件会在 OnInstallComplete／OnInstallCompleteEx 之后最后触发。<br />
SSP 在 2.9.00 之前的版本中存在实现遗漏，因此实际上不会触发。

- **Reference0**: 已安装项目的[※标识符](caption_install-identifier.md)。有多个项目时以字节值 1 分隔。
- **Reference1**: 已安装项目的名称。有多个项目时以字节值 1 分隔。
- **Reference2**: 已安装项目的位置。有多个项目时以字节值 1 分隔。

**対応:** SSP 2.9.00 / Ninix
