# OnUpdateCheckComplete

**カテゴリ:** ネットワーク更新イベント

ネットワーク更新のチェックに成功した際に発生。

- **Reference0**: 更新ファイルがあった場合は、更新を行うファイルの総数（OnUpdateReady と異なり、1は引かれない）。<br />
  更新ファイルが無かった場合は none。
- **Reference1**: カンマでセパレートされた更新されたファイル名のリスト。
- **Reference3**: [※更新対象種別](caption_updatetype.md)
- **Reference4**: SSP 2.3：更新実行理由。scriptのみ。

**対応:** SSP
