# system.network.(キー)

**カテゴリ:** プロパティシステム

ネットワーク接続の状態。(キー)に入る文字列は以下の通り。

- **status**: ネットワーク接続状態。online（接続あり）またはoffline（接続なし）。
- **ipaddress**: ローカルIPアドレス。
- **type**: 接続の種類。bluetooth、cellular、ethernet、none、wifi、wimax、other、unknown のいずれか。
- **cost**: 接続のコスト区分。unknown（不明）、unrestricted（無制限）、fixed（定額）、variable（従量制）のいずれか。
- **downlink**: 下り方向の最大リンク速度（Mbps）。
- **downlink.estimate**: 下り方向の推定リンク速度（Mbps）。実測に基づき算出される、より控えめな見積もり値。

**対応:** SSP 2.8.17
