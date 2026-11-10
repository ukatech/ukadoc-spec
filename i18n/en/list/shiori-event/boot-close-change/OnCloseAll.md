# OnCloseAll

**カテゴリ:** Boot, close, and change events

Occurs when SSP itself is shutting down.<br />
Occurs when "Exit All" is requested from the owner draw menu, when "Exit" is requested for the only running ghost, and when SSP shuts down as part of an OS shutdown.

- **Reference0**: ※SSP only: reason for closing.<br />
  Returns user if the user closed it.<br />
  Returns system if the system is shutting down.
- **Reference1**: ※SSP only: scope number of the character associated with the menu used to close it. Affected by popupmenu.type. (main character 0, partner 1...)
- **Reference2**: ※SSP only: scope number of the character associated with the window used to close it. Not affected by popupmenu.type. (main character 0, partner 1...)

**対応:** SSP / Ninix
