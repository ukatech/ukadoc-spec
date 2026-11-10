# developer.log.日志类型.count

**カテゴリ:** プロパティシステム

SSP 当前记录的日志条目数。日志类型可使用以下字符串。

- **script**：脚本日志（日志窗口的类型 Script）。
- **error**：错误日志（同 Error）。
- **network**：网络日志（同 Network）。
- **update**：更新日志（同 Update）。

各类日志都有条目数上限（默认 50 条），超过上限后会从最旧的条目开始删除。<br />
所有 developer.log.～ 属性均为只读，无论开发者功能的设置如何，都可以获取。<br />
错误日志中，相同内容的日志连续出现时，可能会合并为一条 type 为 System 的摘要。

**対応:** SSP
