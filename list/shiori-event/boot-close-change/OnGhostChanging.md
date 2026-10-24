# OnGhostChanging

**カテゴリ:** 起動・終了・切り替えイベント

他のゴーストへの切り替え指示があった際に発生。<br />
SSPでは、このイベントにスクリプトが返されなかった（204）場合、続けて[OnClose](OnClose.md)が発生する。

- **Reference0**: 切り替わるゴーストの本体側の名前。
- **Reference1**: 手動で切り替えた場合、manual<br />
  システムにより切り替えられた場合、automatic<br />
  が返される。
- **Reference2**: 切り替わるゴーストの名前。\[SSPのみ\]
- **Reference3**: 切り替わるゴーストのパス。\[SSPのみ\]

**対応:** Materia / SSP / CROW / Ninix
