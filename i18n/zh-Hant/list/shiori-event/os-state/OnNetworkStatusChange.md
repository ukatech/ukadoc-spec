# OnNetworkStatusChange

**カテゴリ:** OS 狀態事件

網路連線狀態變更時發生。<br />
僅在啟動後立即以 NOTIFY 通知。

- **Reference0**: online 或 offline。
- **Reference1**: 指派給目前所在電腦的 IP 位址，以位元組值 1 為分隔符號的清單。
- **Reference2**: 連線類型。 \[SSP 2.4.22\]<br />
  cellular : 行動網路，或一般 PPP（不含 PPPoE 等）<br />
  ethernet : Ethernet（有線 LAN）<br />
  none : 未連線<br />
  wifi : 無線 LAN<br />
  wimax : WiMAX<br />
  other : 其他、不明<br />
  unknown : 偵測失敗
- **Reference3**: 表示連線的下載方向最大傳輸速度的數值。單位為 MBps。 \[SSP 2.4.22\]
- **Reference4**: 表示連線的下載方向推估有效傳輸速度的數值。單位為 MBps。 \[SSP 2.5.26\]<br />
  在無法取得網路統計資料的環境，或統計值不準確時，會與 Reference3 的值相同。
- **Reference5**: 通知連線是否為計量付費連線。 \[SSP 2.6.15\]<br />
  unknown : 未設定／不明<br />
  unrestricted : 完全不限量<br />
  fixed : 有資料量上限的定額制<br />
  variable : 計量付費<br />
  在 Windwos 10/11 設定「計量付費連線」時，值會是 fixed。

**対応:** SSP
