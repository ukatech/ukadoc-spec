# OnGhostChanged

**カテゴリ:** 起動・終了・切り替えイベント

他のゴーストから自ゴーストに切り替えられた際に発生。<br />
SSPでは、このイベントにスクリプトが返されなかった（204）場合、続けて[OnBoot](OnBoot.md)が発生する。

- **Reference0**: 直前のゴーストの本体側の名前。
- **Reference1**: 直前のゴーストの切り替え時のスクリプト。
- **Reference2**: 直前のゴーストの名前。 \[SSPのみ\]
- **Reference3**: 直前のゴーストのパス（ファイルの場所）。 \[SSPのみ\]
- **Reference7**: *切り替わったゴーストの*シェル名。 \[SSPのみ\]

**対応:** Materia / SSP / CROW / Ninix
