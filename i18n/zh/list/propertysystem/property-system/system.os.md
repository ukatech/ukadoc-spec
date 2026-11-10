# system.os.(キー)

**カテゴリ:** 属性系统

运行中OS的信息。(キー)可使用以下字符串。

- **type**: OS类型。例如Windows、MacOS、Darwin、Linux、Android、FreeBSD、ReactOS等。若运行时位于Web上，则为"Web"。（由于历史原因，值采用TitleCase）
- **arch**: OS架构。例如x86、x64、arm、arm64、ia64、risc-v、ppc、mips、loongarch等。无法确定或与架构无关时为"unknown"
- **name**: OS名称。例如：Windows 11 22H2
- **version**: OS内核版本。例如：10.0。请注意，这可能与OS的名称不一致。例如，Windows 10和11的版本号都是10.0。
- **build**: OS内部版本号。例如：22621
- **parenttype**: 若通过某种兼容OS/兼容层运行，则为其类型。若不存在则为空字符串。目前包括Wine或ReactOS。
- **parentname**: 兼容OS/兼容层的宿主侧（父级）OS名称。若不存在则为空字符串。例如：Linux 5.19.0-23-generic
- **locale**: OS的UI区域设置名称。由语言代码和国家/地区代码以「-」连接组成。例如：ja-JP（SSP 2.8.17及以后版本）
- **locale.language**: OS的UI语言代码（ISO 639）。例如：ja（SSP 2.8.17及以后版本）
- **locale.country**: OS的UI国家/地区代码（ISO 3166）。例如：JP（SSP 2.8.17及以后版本）
- **timezone.offset**: 当前时区相对UTC的偏移量（单位为分钟）。相对于UTC时间较早的地区将返回负值。例如：日本标准时间为-540（SSP 2.8.17及以后版本）
- **dst**: 当前是否采用夏令时。采用时为1，否则为0。（SSP 2.8.17及以后版本）
- **uptime**: OS启动后的经过时间（秒）。（SSP 2.8.17及以后版本）
- **unixtime**: 当前时间的UNIX时间戳（自1970-01-01 00:00:00 UTC起经过的秒数）。（SSP 2.8.17及以后版本）
- **idletime**: 自最后一次用户输入（键盘或鼠标操作）起经过的时间（秒）。（SSP 2.8.17及以后版本）

**対応:** SSP 2.6.26/27
