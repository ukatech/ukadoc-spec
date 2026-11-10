# system.cpu.(key)

**カテゴリ:** プロパティシステム

Information about the CPU of the running environment. The strings that can be used for (key) are as follows.

- **load**: Load percentage (unit: %, integer; smoothed by calculating a moving average over an interval of approximately one minute, as appropriate)
- **num**: Total number of cores recognized by the OS
- **vendor**: Vendor name. Example: GenuineIntel
- **name**: Name. Example: 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz
- **clock**: Clock frequency
- **features**: List of interpretable extended instructions (separated by half-width spaces). Example: MMX SSE SSE2 SSE3

**対応:** SSP 2.6.26
