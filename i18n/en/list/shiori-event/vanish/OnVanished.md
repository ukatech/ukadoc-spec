# OnVanished

**カテゴリ:** Vanish event

Occurs when the ghost switches to this ghost because the previous ghost vanished.<br />
In SSP, if no script is returned for this event (204), [OnBoot](../boot-close-change/OnBoot.md) occurs immediately afterward.<br />
Also note that in SSP, this event occurs when another concurrently running ghost vanishes if no script is returned for OnOtherGhostVanished. In this case, there is no fallback to OnBoot.

- **Reference0**: The name of the vanished ghost on its main side.
- **Reference1**: ※SSP only　The script for the vanished ghost's OnVanishSelected event.
- **Reference2**: ※SSP only　The name of the vanished ghost.
- **Reference7**: ※SSP only　The shell name of *the ghost switched to*.

**対応:** Materia / SSP / CROW / Ninix
