# OnUpdateProcessExec

**カテゴリ:** Network update event

Occurs when an instruction to run an update is issued from a menu or similar.<br />
Returning a script in response to this event allows the update process to be customized.<br />
If the event is ignored, the standard update process starts automatically.

- **Reference0**: manual: An update was initiated from the menu.<br />
  auto: The configured periodic automatic update process ran.<br />
  testonly: Update Full Check was run from the development palette.

**対応:** SSP 2.6.23
