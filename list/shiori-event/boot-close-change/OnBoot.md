# OnBoot

**カテゴリ:** 起動・終了・切り替えイベント

起動した際に発生。<br />
SSPでは、[OnGhostChanged](OnGhostChanged.md)、[OnGhostCalled](OnGhostCalled.md)、[OnFirstBoot](OnFirstBoot.md)、[OnVanished](../vanish/OnVanished.md)に対してスクリプトが返されなかった（204）場合、続けてこのイベントが発生する。

- **Reference0**: 起動時のシェル名。
- **Reference6**: ※MATERIA、SSPのみ　前回の処理中で落ちた時にhalt。
- **Reference7**: ※MATERIA、SSPのみ　前回の処理中で落ちたゴースト名 。

**対応:** Materia / SSP / CROW / Ninix
