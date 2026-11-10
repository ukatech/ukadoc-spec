# system.os.(キー)

**カテゴリ:** Property system

Information about the running OS. The strings that can be used for (キー) are as follows.

- **type**: OS type, such as Windows,MacOS,Darwin,Linux,Android,FreeBSD,ReactOS. For a runtime on the web, the value is "Web". (Values are in TitleCase for historical reasons.)
- **arch**: OS architecture, such as x86,x64,arm,arm64,ia64,risc-v,ppc,mips,loongarch. If it cannot be determined or is architecture-independent, the value is "unknown".
- **name**: OS name. Example: Windows 11 22H2
- **version**: OS kernel version. Example: 10.0. Note that it may differ from the OS's commonly used name. For example, both Windows 10 and 11 have the version 10.0.
- **build**: OS build number. Example: 22621
- **parenttype**: If running in some kind of compatibility OS or compatibility layer, its type. If there is none, an empty string. Currently, this may be Wine or ReactOS.
- **parentname**: Name of the host-side (parent) OS for a compatibility OS or compatibility layer. If there is none, an empty string. Example: Linux 5.19.0-23-generic
- **locale**: OS UI locale name. A language code and country/region code joined by "-". Example: ja-JP (SSP 2.8.17 and later)
- **locale.language**: OS UI language code (ISO 639). Example: ja (SSP 2.8.17 and later)
- **locale.country**: OS UI country/region code (ISO 3166). Example: JP (SSP 2.8.17 and later)
- **timezone.offset**: Current time zone offset from UTC (in minutes). Regions ahead of UTC have negative values. Example: -540 for Japan Standard Time (SSP 2.8.17 and later)
- **dst**: 1 if daylight saving time (summer time) is currently in effect, otherwise 0. (SSP 2.8.17 and later)
- **uptime**: Elapsed time since the OS started (seconds). (SSP 2.8.17 and later)
- **unixtime**: Current UNIX time (seconds elapsed since 1970-01-01 00:00:00 UTC). (SSP 2.8.17 and later)
- **idletime**: Elapsed time since the last user input (keyboard or mouse operation) (seconds). (SSP 2.8.17 and later)

**対応:** SSP 2.6.26/27
