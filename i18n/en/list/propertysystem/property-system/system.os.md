# system.os.(key)

**カテゴリ:** Property System

Information about the running OS. The following strings can be used for (key).

- **type**: OS type, such as Windows,MacOS,Darwin,Linux,Android,FreeBSD,ReactOS. For a runtime on the web, this is "Web". (The value is in TitleCase for historical reasons.)
- **arch**: OS architecture, such as x86,x64,arm,arm64,ia64,risc-v,ppc,mips,loongarch. If it cannot be determined or is architecture-independent, this is "unknown".
- **name**: OS name. Example: Windows 11 22H2
- **version**: OS kernel version. Example: 10.0. Note that this may differ from the OS's marketed version. For example, both Windows 10 and 11 have version 10.0.
- **build**: OS build number. Example: 22621
- **parenttype**: If running in some kind of compatibility OS or compatibility layer, its type. An empty string if none. Currently, this is Wine or ReactOS.
- **parentname**: Name of the host (parent) OS for a compatibility OS or compatibility layer. An empty string if none. Example: Linux 5.19.0-23-generic
- **locale**: OS UI locale name, formed by joining the language code and country or region code with "-". Example: ja-JP (SSP 2.8.17 and later)
- **locale.language**: OS UI language code (ISO 639). Example: ja (SSP 2.8.17 and later)
- **locale.country**: OS UI country or region code (ISO 3166). Example: JP (SSP 2.8.17 and later)
- **timezone.offset**: Offset of the current time zone from UTC, in minutes. Regions ahead of UTC have a negative value. Example: -540 for Japan Standard Time (SSP 2.8.17 and later)
- **dst**: 1 if daylight saving time is currently in effect, otherwise 0. (SSP 2.8.17 and later)
- **uptime**: Time elapsed since the OS started, in seconds. (SSP 2.8.17 and later)
- **unixtime**: UNIX time for the current time (seconds elapsed since 1970-01-01 00:00:00 UTC). (SSP 2.8.17 and later)
- **idletime**: Time elapsed since the last user input (keyboard or mouse operation), in seconds. (SSP 2.8.17 and later)

**対応:** SSP 2.6.26/27
