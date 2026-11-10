# system.cpu.(key)

**カテゴリ:** Property System

Information about the CPU in the running environment. The strings that can be used for (key) are as follows.

- **load**: Load percentage (integer, averaged over a moving window of approximately one minute)
- **num**: Total number of cores recognized by the OS
- **vendor**: Vendor name. Example: GenuineIntel
- **name**: Name. Example: 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz
- **clock**: Clock frequency
- **features**: List of supported instruction set extensions (separated by spaces). Example: MMX SSE SSE2 SSE3

**対応:** SSP 2.6.26
