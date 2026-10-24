# OnTranslate

**カテゴリ:** その他イベント

SHIORIがMAKOTOのトランスレート機能を兼任するためのイベント。<br />
主に、GETコマンドのSHIORI Eventに対してベースウェアへスクリプトが返却された場合に、それに応じて発行される。<br />
OnTranslateの元となったSHIORI Eventに対して、SHIORI内部での操作を経てベースウェアへ返却されたスクリプトが、ベースウェアによる環境変数の展開などの後に再びSHIORIに送られる。SHIORIはこのスクリプトに対して再度何らかの処理を行ってベースウェアに最終的なスクリプトとして返却できる。<br />
なおOnTranslate自身では再度発生しない。

- **Reference0**: 元のスクリプト。
- **Reference1**: ※SSPのみ　コミュニケートの場合、communicate。<br />
  SSTP SENDの場合、sstp-send。<br />
  Owned SSTPの場合、owned。<br />
  非ローカルSSTPの場合、remote。<br />
  トランスレートしない指定の場合、notranslate。<br />
  プラグインからのスクリプトの場合、plugin-script<br />
  プラグインからのイベント反応の場合、plugin-event<br />
  該当するものがカンマ区切りで返る。※該当がない場合欠番となる。
- **Reference2**: ※SSPのみ　このスクリプトが発生したイベントID 。イベントが原因ではない場合欠番。
- **Reference3**: ※SSPのみ　バイト値1区切りの上記イベントのReference 。イベントが原因ではない場合欠番。

**対応:** Materia / SSP / CROW / Ninix
