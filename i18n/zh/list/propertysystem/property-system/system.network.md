# system.network.(キー)

**カテゴリ:** 属性系统

网络连接状态。(キー)可使用以下字符串。

- **status**: 网络连接状态。为online（已连接）或offline（未连接）。
- **ipaddress**: 本地IP地址。
- **type**: 连接类型。为bluetooth、cellular、ethernet、none、wifi、wimax、other、unknown之一。
- **cost**: 连接费用类型。为unknown（未知）、unrestricted（无限制）、fixed（固定费用）、variable（按用量计费）之一。
- **downlink**: 下行最大链路速度（Mbps）。
- **downlink.estimate**: 下行估算链路速度（Mbps）。这是根据实测结果计算出的、更为保守的估算值。

**対応:** SSP 2.8.17
