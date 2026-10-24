# animation\*.option,オプション

**カテゴリ:** surfaceブレス

exclusive・background・shared-indexオプションは同時指定可能で、+区切りで複数オプション可。例：exclusive+background<br />
animationに続く\*の部分はanimationID（animation\*.intervalの\*と同一）。<br />
animation\*.option,exclusive+background,(1,3,5) のようにすると、*exclusiveのみ*影響を受ける。<br />
なおintervalがbindのアニメーションについてはexclusive指定はそもそも未定義である。

**既定値:** 挙動なし

**対応:** SSP
