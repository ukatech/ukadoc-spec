# animation\*.option,exclusive

**カテゴリ:** surfaceブレス

アニメーションの排他的実行オプション。<br />
即ちexclusiveオプションが指定されたアニメーションが実行された時点で、他のすべてのアニメーションが停止し、またexclusiveオプションのアニメーションの終了まで、他のいかなるアニメーションも新たに開始されない。<br />
animationに続く\*の部分はanimationID（animation\*.intervalの\*と同一）。<br />
なおintervalがbindのアニメーションについてはこの指定は未定義である。<br />
SSPのみ、animation\*.option,exclusive,(1,3,5)のようにすると、指定IDのアニメーションに対してのみ限定的に排他制御することができる。<br />
[旧定義](caption_seriko-redefine.md)：\*option,exclusive

**既定値:** 挙動なし

**対応:** Materia / SSP / CROW
