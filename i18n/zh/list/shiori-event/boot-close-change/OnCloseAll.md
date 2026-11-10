# OnCloseAll

**カテゴリ:** Startup, shutdown, and switching event

Occurs when SSP itself shuts down.<br />
This occurs when "Exit all" is selected from the owner-draw menu, when "Exit" is selected for the only running ghost, and when SSP shuts down as part of an OS shutdown.

- **Reference0**: ※SSP only: reason for shutdown.<br />
  Returns user when the user shuts down<br />
  and system when the system shuts down.
- **Reference1**: ※SSP only: scope number of the character associated with the menu used to shut down. Affected by popupmenu.type (main character 0, partner 1...).
- **Reference2**: ※SSP only: scope number of the character in the window used to shut down. Not affected by popupmenu.type (main character 0, partner 1...).

**対応:** SSP / Ninix
