# OnClose

**カテゴリ:** Startup, shutdown, and switching event

Occurs when shutdown is requested.<br />
In SSP, if no script is returned (204) for [OnGhostChanging](OnGhostChanging.md) or [OnCloseAll](OnCloseAll.md), this event occurs next.

- **Reference0**: ※SSP only: reason for shutdown.<br />
  Returns user when the user shuts down<br />
  and system when the system shuts down.
- **Reference1**: ※SSP only: scope number of the character associated with the menu used to shut down. Affected by popupmenu.type (main character 0, partner 1...).
- **Reference2**: ※SSP only: scope number of the character in the window used to shut down. Not affected by popupmenu.type (main character 0, partner 1...).

**対応:** Materia / SSP / CROW / Ninix
