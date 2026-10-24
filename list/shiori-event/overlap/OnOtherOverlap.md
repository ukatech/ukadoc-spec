# OnOtherOverlap

**カテゴリ:** 見切れ・重なりイベント

他も含めて全起動中のキャラクター（サーフェス）のウインドウが重なった時に発生。OnOverlapのグローバル版。<br />
重なり状態が変わった際に逐次通知されるので、「重ならなくなった」も工夫すれば検出できる。<br />
自分自身の情報も一緒に通知されるので注意。

- **Reference0**: Sakura名/ID-Sakura名/ID \[`\1`\] Sakura名/ID-Sakura名/ID \[`\1`\] Sakura名/ID-Sakura名/ID ...<br />
  \[`\1`\] はバイト値1<br />
  例：Emily/0-マリ/1 \[`\1`\] マリ/0-所長たん/1
- **Reference1**: Reference0と同じフォーマットで、状態が変わる前（＝1回前のイベント発生時のReference0）が通知される。

**対応:** SSP / Ninix
