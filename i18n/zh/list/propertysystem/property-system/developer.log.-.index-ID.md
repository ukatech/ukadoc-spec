# developer.log.日志类型.index(ID).日志属性名

**カテゴリ:** プロパティシステム

获取日志中第 ID 个条目的信息。<br />
ID 按新到旧依次为 0、1、2...。指定超出范围的 ID 时，获取失败。<br />
日志类型参见[developer.log.日志类型.count](developer.log.-.count.md)。日志属性名可使用以下字符串。

- **type**：日志类型。<br />
  script 类型的日志格式为 Ghost(～) 或 SSTP(～)，括号中是以逗号分隔的相应属性（Ghost：External、Embed、SSF、Plugin　SSTP：Local 或 Remote、TempGhost、Auth　共通：NoTranslate）。Ghost 没有相应属性时，会省略括号，只显示 Ghost。有附加信息时，末尾会添加「:附加信息」。<br />
  其他日志类型为 Info、Notice、Warning、Error、Critical、System 中的一种。
- **name**：日志来源的名称（例如 ghost 名称）。没有来源时为\[SYSTEM\]。
- **value**：日志正文。较长的内容也会完整返回，不会省略。
- **time**：记录日志的日期和时间。使用本地时间，以半角空格分隔 OS 的短日期格式和 24 小时制的时:分。格式取决于 OS 的区域设置。

**対応:** SSP
