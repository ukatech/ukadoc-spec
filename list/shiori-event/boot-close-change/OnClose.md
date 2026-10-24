# OnClose

**カテゴリ:** 起動・終了・切り替えイベント

終了が指示された際に発生。<br />
SSPでは、[OnGhostChanging](OnGhostChanging.md)、[OnCloseAll](OnCloseAll.md)に対してスクリプトが返されなかった（204）場合、続けてこのイベントが発生する。

- **Reference0**: ※SSPのみ　終了理由。<br />
  ユーザーが終了した場合、user<br />
  シャットダウンした場合、systemが返される。
- **Reference1**: ※SSPのみ　終了操作したメニューが属するキャラクターのスコープ番号。popupmenu.typeに影響される。(本体側0,相方1...)
- **Reference2**: ※SSPのみ　終了操作したウインドウのキャラクターのスコープ番号。popupmenu.typeに影響されない。(本体側0,相方1...)

**対応:** Materia / SSP / CROW / Ninix
