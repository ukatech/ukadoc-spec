# OnBoot

**カテゴリ:** Boot, close, and change events

Occurs at startup.<br />
In SSP, if no script is returned for [OnGhostChanged](OnGhostChanged.md), [OnGhostCalled](OnGhostCalled.md), [OnFirstBoot](OnFirstBoot.md), or [OnVanished](../vanish/OnVanished.md) (204), this event occurs next.

- **Reference0**: Shell name at startup.
- **Reference6**: ※MATERIA and SSP only: halt if the previous process crashed.
- **Reference7**: ※MATERIA and SSP only: name of the ghost that crashed during the previous process.

**対応:** Materia / SSP / CROW / Ninix
