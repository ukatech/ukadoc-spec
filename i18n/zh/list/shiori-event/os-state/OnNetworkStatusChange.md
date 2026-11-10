# OnNetworkStatusChange

**カテゴリ:** OS状态事件

网络连接状态发生变化时触发。<br />
仅在启动后立即通过NOTIFY通知。

- **Reference0**: online或offline。
- **Reference1**: 分配给当前计算机的IP地址列表，以字节值1分隔。
- **Reference2**: 连接类型。 \[SSP 2.4.22\]<br />
  cellular : 蜂窝网络或普通PPP(不包括PPPoE等)<br />
  ethernet : Ethernet (有线LAN)<br />
  none : 无连接<br />
  wifi : 无线LAN<br />
  wimax : WiMAX<br />
  other : 其他未知类型<br />
  unknown : 检测失败
- **Reference3**: 表示连接线路下载方向最大通信速度的数值。单位为MBps。 \[SSP 2.4.22\]
- **Reference4**: 表示连接线路下载方向估算有效通信速度的数值。单位为MBps。 \[SSP 2.5.26\]<br />
  在无法获取通信统计数据的环境中，或统计值不准确时，该值与Reference3相同。
- **Reference5**: 通知连接线路是否为按流量计费的线路。 \[SSP 2.6.15\]<br />
  unknown : 未设置/未知<br />
  unrestricted : 完全不限量<br />
  fixed : 有数据量上限的固定套餐<br />
  variable : 按流量计费<br />
  在Windwos 10/11中设置「按流量计费的连接」时，值为fixed。

**対応:** SSP
