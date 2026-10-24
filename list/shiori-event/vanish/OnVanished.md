# OnVanished

**カテゴリ:** 消滅イベント

直前のゴーストの消滅により自分に切り替わった際に発生。<br />
SSPでは、このイベントにスクリプトが返されなかった（204）場合、続けて[OnBoot](../boot-close-change/OnBoot.md)が発生する。<br />
またSSPでは同時起動中の他のゴーストが消滅した際に、OnOtherGhostVanishedへスクリプトが返却されなかった際にも発生するため注意。この場合OnBootへのフォールバックはない。

- **Reference0**: 消滅したゴーストの本体側の名前。
- **Reference1**: ※SSPのみ　消滅したゴーストのOnVanishSelectedイベントのスクリプト。
- **Reference2**: ※SSPのみ　消滅したゴースト名。
- **Reference7**: ※SSPのみ　*切り替わったゴーストの*シェル名。

**対応:** Materia / SSP / CROW / Ninix
