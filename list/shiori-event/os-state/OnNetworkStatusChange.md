# OnNetworkStatusChange

**カテゴリ:** OS状態イベント

ネットワーク接続状態が変わった際に発生。<br />
起動直後のみNOTIFYで通知。

- **Reference0**: onlineまたはoffline。
- **Reference1**: 現在居るマシンに割り当てられているIPアドレスのバイト値1区切りリスト。
- **Reference2**: 接続の種類。 \[SSP 2.4.22\]<br />
  cellular : 携帯回線もしくは通常のPPP(PPPoE等除く)<br />
  ethernet : Ethernet (有線LAN)<br />
  none : 接続なし<br />
  wifi : 無線LAN<br />
  wimax : WiMAX<br />
  other : その他不明<br />
  unknown : 検出に失敗
- **Reference3**: 接続回線のダウンロード側の最大通信速度を示す数値。単位はMBps。 \[SSP 2.4.22\]
- **Reference4**: 接続回線のダウンロード側の推定有効通信速度を示す数値。単位はMBps。 \[SSP 2.5.26\]<br />
  通信統計が取得できない環境や、統計値が不正確な状態ではReference3と同じ値となる。
- **Reference5**: 接続回線が従量課金回線かどうかを通知する。 \[SSP 2.6.15\]<br />
  unknown : 未設定/不明<br />
  unrestricted : 完全使い放題<br />
  fixed : データ量の上限がある定額制<br />
  variable : 従量課金<br />
  Windwos 10/11で「従量制課金接続」を設定するとfixedになる。

**対応:** SSP
