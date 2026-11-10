# system.cpu.(キー)

**カテゴリ:** プロパティシステム

正在运行的环境的 CPU 信息。(キー) 可填入以下字符串。

- **load**: 负载率（单位为％，整数，按需计算约分钟级移动平均后平滑处理）
- **num**: OS 识别到的核心总数
- **vendor**: 厂商名称。例：GenuineIntel
- **name**: 名称。例：11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz
- **clock**: 时钟频率
- **features**: 可识别的扩展指令列表（以半角空格分隔）。例：MMX SSE SSE2 SSE3

**対応:** SSP 2.6.26
