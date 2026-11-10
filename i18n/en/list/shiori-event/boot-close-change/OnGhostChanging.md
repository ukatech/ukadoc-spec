# OnGhostChanging

**カテゴリ:** Startup, shutdown, and switching events

Occurs when a switch to another ghost is requested.<br />
In SSP, if no script is returned for this event (204), [OnClose](OnClose.md) occurs next.

- **Reference0**: The name of the baseware of the ghost being switched to.
- **Reference1**: If switched manually, manual<br />
  If switched by the system, automatic<br />
  is returned.
- **Reference2**: The name of the ghost being switched to.\[SSP only\]
- **Reference3**: The path of the ghost being switched to.\[SSP only\]

**対応:** Materia / SSP / CROW / Ninix
