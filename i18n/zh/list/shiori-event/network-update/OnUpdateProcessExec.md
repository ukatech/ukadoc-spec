# OnUpdateProcessExec

**カテゴリ:** 网络更新事件

通过菜单等发出执行更新指令时触发。<br />
向此事件返回任意脚本，即可自定义更新处理。<br />
忽略此事件时，将自动进入标准更新处理。

- **Reference0**: manual : 从菜单执行了更新操作。<br />
  auto : 执行了预先设置的定期自动更新处理。<br />
  testonly : 执行了开发用面板中的Update Full Check。

**対応:** SSP 2.6.23
