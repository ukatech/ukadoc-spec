# system.os.(key)

**カテゴリ:** Property system

Information about the running OS. The strings accepted for (key) are as follows.

- **type**: OS type. Windows, MacOS, Darwin, Linux, Android, FreeBSD, ReactOS, etc. "Web" for a web runtime. (Values use TitleCase for historical reasons.)
- **arch**: OS architecture. x86, x64, arm, arm64, ia64, risc-v, ppc, mips, loongarch, etc. "unknown" if it cannot be determined or is architecture-independent.
- **name**: OS name. Example: Windows 11 22H2
- **version**: OS kernel version. Example: 10.0. Note that this may differ from the OS name. For example, both Windows 10 and 11 return 10.0.
- **build**: OS build number. Example: 22621
- **parenttype**: Type of compatibility OS or compatibility layer, if running under one. An empty string if none. Currently Wine or ReactOS.
- **parentname**: Name of the host (parent) OS of the compatibility OS or compatibility layer. An empty string if none. Example: Linux 5.19.0-23-generic
- **locale**: OS UI locale name. The language code and country or region code joined by "-". Example: ja-JP (SSP 2.8.17 and later)
- **locale.language**: OS UI language code (ISO 639). Example: ja (SSP 2.8.17 and later)
- **locale.country**: OS UI country or region code (ISO 3166). Example: JP (SSP 2.8.17 and later)
- **timezone.offset**: Current time zone offset from UTC in minutes. Negative for regions ahead of UTC. Example: -540 for Japan Standard Time (SSP 2.8.17 and later)
- **dst**: 1 if daylight saving time is currently in effect, otherwise 0. If SSP's "virtual modification of the current time" (time machine) has shifted the time, returns whether daylight saving time applies at the shifted date and time. (SSP 2.8.17 and later)
- **uptime**: Time elapsed since the OS started, in seconds. (SSP 2.8.17 and later)
- **unixtime**: Current time as UNIX time (seconds elapsed since 1970-01-01 00:00:00 UTC). If SSP's "virtual modification of the current time" (time machine) has shifted the time, returns the shifted time. (SSP 2.8.17 and later)
- **timeshift**: Current time offset in seconds due to SSP's "virtual modification of the current time" (time machine). A signed integer: positive if shifted into the future, negative if shifted into the past, or 0 if not shifted. (SSP 2.9.39 and later)
- **idletime**: Time elapsed since the last user input (keyboard or mouse activity), in seconds. (SSP 2.8.17 and later)

**対応:** SSP 2.6.26/27
