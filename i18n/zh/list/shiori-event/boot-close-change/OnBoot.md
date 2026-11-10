# OnBoot

**カテゴリ:** Startup, shutdown, and switching event

Occurs at startup.<br />
In SSP, if no script is returned (204) for [OnGhostChanged](OnGhostChanged.md), [OnGhostCalled](OnGhostCalled.md), [OnFirstBoot](OnFirstBoot.md), or [OnVanished](../vanish/OnVanished.md), this event occurs next.

- **Reference0**: Shell name at startup.
- **Reference6**: ※MATERIA and SSP only: halt if the previous process crashed.
- **Reference7**: ※MATERIA and SSP only: name of the ghost that crashed during the previous process.

**対応:** Materia / SSP / CROW / Ninix
