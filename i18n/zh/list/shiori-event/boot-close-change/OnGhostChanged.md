# OnGhostChanged

**カテゴリ:** Startup, shutdown, and switching events

Occurs when switched to this ghost from another ghost.<br />
In SSP, if no script is returned for this event (204), [OnBoot](OnBoot.md) occurs next.

- **Reference0**: Name of the previous ghost on the baseware side.
- **Reference1**: Script used when switching from the previous ghost.
- **Reference2**: Name of the previous ghost. \[SSP only\]
- **Reference3**: Path of the previous ghost (file location). \[SSP only\]
- **Reference7**: Shell name of the *ghost switched to*. \[SSP only\]

**対応:** Materia / SSP / CROW / Ninix
