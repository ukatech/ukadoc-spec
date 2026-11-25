# system.os.(键)

**カテゴリ:** 属性系统

当前运行的 OS 的信息。(键)中填入的字符串如下。

- **type**: OS 类型。例如 Windows,MacOS,Darwin,Linux,Android,FreeBSD,ReactOS。Web 运行时为 "Web"。（由于历史原因，值采用 TitleCase）
- **arch**: OS 架构。例如 x86,x64,arm,arm64,ia64,risc-v,ppc,mips,loongarch。无法确定或与架构无关时为 "unknown"。
- **name**: OS 名称。例如：Windows 11 22H2
- **version**: OS 内核版本。例如：10.0。注意可能与 OS 的名称不一致。例如：Windows 10 和 11 都是 10.0。
- **build**: OS 构建号。例如：22621
- **parenttype**: 在兼容 OS 或兼容层上运行时，其类型。不存在时为空字符串。目前为 Wine 或 ReactOS。
- **parentname**: 兼容 OS 或兼容层的宿主（父级）OS 名称。不存在时为空字符串。例如：Linux 5.19.0-23-generic
- **locale**: OS 的 UI 区域设置名称。由语言代码和国家或地区代码以「-」连接而成。例如：ja-JP（SSP 2.8.17 及以后）
- **locale.language**: OS 的 UI 语言代码（ISO 639）。例如：ja（SSP 2.8.17 及以后）
- **locale.country**: OS 的 UI 国家或地区代码（ISO 3166）。例如：JP（SSP 2.8.17 及以后）
- **timezone.offset**: 当前时区相对于 UTC 的偏移量（单位为分钟）。在时间超前于 UTC 的地区，该值为负数。例如：日本标准时间为 -540（SSP 2.8.17 及以后）
- **dst**: 当前应用夏令时时为 1，否则为 0。通过 SSP 的「虚拟更改当前时间」（时间机器）调整时间时，返回调整后的日期和时间是否处于夏令时。（SSP 2.8.17 及以后）
- **uptime**: 自 OS 启动以来经过的时间（秒）。（SSP 2.8.17 及以后）
- **unixtime**: 当前时间的 UNIX 时间（自 1970-01-01 00:00:00 UTC 以来经过的秒数）。通过 SSP 的「虚拟更改当前时间」（时间机器）调整时间时，返回调整后的时间。（SSP 2.8.17 及以后）
- **timeshift**: SSP 的「虚拟更改当前时间」（时间机器）造成的当前时间偏移（秒）。为带符号的整数，向未来调整时为正，向过去调整时为负，未调整时为 0。（SSP 2.9.39 及以后）
- **idletime**: 自最后一次用户输入（键盘或鼠标操作）以来经过的时间（秒）。（SSP 2.8.17 及以后）

**対応:** SSP 2.6.26/27
