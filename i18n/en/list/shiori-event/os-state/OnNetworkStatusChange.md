# OnNetworkStatusChange

**カテゴリ:** OS state event

Occurs when the network connection status changes.<br />
Only sent as NOTIFY immediately after startup.

- **Reference0**: online or offline.
- **Reference1**: A comma-separated list of the byte values of the IP addresses assigned to the current machine.
- **Reference2**: Connection type. \[SSP 2.4.22\]<br />
  cellular: Cellular connection or standard PPP (excluding PPPoE, etc.)<br />
  ethernet: Ethernet (wired LAN)<br />
  none: No connection<br />
  wifi: Wireless LAN<br />
  wimax: WiMAX<br />
  other: Other/unknown<br />
  unknown: Detection failed
- **Reference3**: A value indicating the maximum download speed of the connection. The unit is MBps. \[SSP 2.4.22\]
- **Reference4**: A value indicating the estimated effective download speed of the connection. The unit is MBps. \[SSP 2.5.26\]<br />
  This has the same value as Reference3 in environments where communication statistics cannot be obtained or are inaccurate.
- **Reference5**: Indicates whether the connection is metered. \[SSP 2.6.15\]<br />
  unknown: Not set/unknown<br />
  unrestricted: Unlimited data<br />
  fixed: Fixed plan with a data cap<br />
  variable: Metered<br />
  Setting "Metered connection" in Windows 10/11 results in fixed.

**対応:** SSP
