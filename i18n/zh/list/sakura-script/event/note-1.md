# 补充

## 更新选项指定

- **checkonly**: 不触发普通更新事件，而是通知 SHIORI 事件[OnUpdateCheckComplete](../../shiori-event/network-update/OnUpdateCheckComplete.md)；若失败，则通知[OnUpdateCheckFailure](../../shiori-event/network-update/OnUpdateCheckFailure.md)。确认是否有更新后即可中断处理。<br />
  所有更新完成后，会汇总结果；使用 updateother 时触发[OnUpdateCheckResultEx](../../shiori-event/network-update/OnUpdateCheckResultEx.md)，其他情况下触发[OnUpdateCheckResult](../../shiori-event/network-update/OnUpdateCheckResult.md)。
- **testonly**: 像正式更新一样下载更新文件，但不会实际替换文件。<br />
  在 SSP 中，其行为与通过开发用面板执行的 "Update Full Check" 相同。
- **recovery \[SSP 2.5.26～\]**: 在修复模式下执行更新。在 SSP 中，其行为与按住在设置-ゴースト(1)-修复模式切换键有效中设置的按键进行更新时相同。<br />
  忽略本地的所有更新定义文件，仅采用从网络下载的更新定义，然后与本地所有文件的哈希值进行比较，并下载不同的文件。
