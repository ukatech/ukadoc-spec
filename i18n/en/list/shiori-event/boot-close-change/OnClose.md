# OnClose

**カテゴリ:** Boot, close, and change events

Occurs when a request to close is made.<br />
In SSP, if no script is returned for [OnGhostChanging](OnGhostChanging.md) or [OnCloseAll](OnCloseAll.md) (204), this event occurs next.

- **Reference0**: ※SSP only: reason for closing.<br />
  Returns user if the user closed it.<br />
  Returns system if the system is shutting down.
- **Reference1**: ※SSP only: scope number of the character associated with the menu used to close it. Affected by popupmenu.type. (main character 0, partner 1...)
- **Reference2**: ※SSP only: scope number of the character associated with the window used to close it. Not affected by popupmenu.type. (main character 0, partner 1...)

**対応:** Materia / SSP / CROW / Ninix
