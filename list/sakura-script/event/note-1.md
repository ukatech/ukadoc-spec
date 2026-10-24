# 補足

## 更新オプション指定

- **checkonly**: 普通の更新イベントの代わりに、SHIORIイベント[OnUpdateCheckComplete](../../shiori-event/network-update/OnUpdateCheckComplete.md)、失敗した場合は[OnUpdateCheckFailure](../../shiori-event/network-update/OnUpdateCheckFailure.md)が通知され、更新の有無を判定でき次第処理を中断する。<br />
  すべて更新が終わった後に、結果の総括として、updateotherの時は[OnUpdateCheckResultEx](../../shiori-event/network-update/OnUpdateCheckResultEx.md)、そのほかは[OnUpdateCheckResult](../../shiori-event/network-update/OnUpdateCheckResult.md)が発生する。
- **testonly**: 本番と同じように更新ファイルのダウンロードを行うが、実際のファイルの置き換えは行わない。<br />
  SSPでは開発用パレットから実行できる"Update Full Check"と同じ挙動。
- **recovery \[SSP 2.5.26～\]**: 修復モードで更新を実行する。SSPでは設定-ゴースト(1)-修復モードへの切り替えキー有効、で設定したキーを押しながら更新した際と同じ挙動。<br />
  ローカル側にある更新定義ファイルを全部無視し、ネットワーク上からダウンロードしてきた更新定義のみを採用した上で、ローカル側の全ファイルのハッシュ値と比較し、異なるものをダウンロードする。
