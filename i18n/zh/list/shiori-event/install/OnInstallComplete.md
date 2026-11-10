# OnInstallComplete

**カテゴリ:** 安装事件

安装成功完成时触发。<br />
这是旧版规范，因此一次安装中同时安装的项目中，只有*前2项*会收到通知。<br />
如果通过捆绑可能同时安装3项或更多项目，请使用[OnInstallCompleteEx](OnInstallCompleteEx.md)。

- **Reference0**: 已安装项目的[※标识符](caption_install-identifier.md)。
- **Reference1**: 已安装项目的名称（install.txt 中指定的 name）。
- **Reference2**: 已安装项目的名称 2（例如，随 ghost 一同捆绑 balloon 时的 balloon 名称）。

**対応:** Materia / SSP / CROW / Ninix
