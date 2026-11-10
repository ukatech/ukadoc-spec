# surface ID,名称

**カテゴリ:** surfacetable.txt

为 surface ID 指定一个用于识别的名称。<br />
通常写在组内。<br />
组内最先写入的项目会被视为该组的标准 surface（例如，scope,0 时为 0，scope,1 时为 10）。<br />
如果名称设为“\_\_parts”，则表示该 surface 主要用作动画或 dressup 等部件（在 SSP 的 surface 测试中会按名称未指定处理）。<br />
省略名称可以明确表示名称未定义。在 SSP 的 surface 测试中，只有[特定 surface](../../shell-surfaces/surface-brace/caption_standarddef.md)会在未指定时获得初始值，因此可用于取消这些 surface 的指定。

**既定値:** 无行为 / 在 SSP 的 surface 测试中，仅特定 surface 使用[标准 surface 定义](../../shell-surfaces/surface-brace/caption_standarddef.md)。

**対応:** SSP
