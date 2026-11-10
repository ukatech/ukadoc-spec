# OnGhostChanged

**カテゴリ:** Startup, shutdown, and switching events

Occurs when switched from another ghost to this ghost.<br />
In SSP, if no script is returned for this event (204), [OnBoot](OnBoot.md) occurs immediately afterward.

- **Reference0**: Name of the previous ghost's main body.
- **Reference1**: Script used when switching from the previous ghost.
- **Reference2**: Name of the previous ghost. \[SSP only\]
- **Reference3**: Path of the previous ghost (file location). \[SSP only\]
- **Reference7**: *Shell name of the ghost switched to.* \[SSP only\]

**対応:** Materia / SSP / CROW / Ninix
