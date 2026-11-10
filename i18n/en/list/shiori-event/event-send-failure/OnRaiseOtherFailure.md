# OnRaiseOtherFailure

**カテゴリ:** Event send failure event

Occurs when `\![raiseother]` fails.

- **Reference0**: If not found, notfound.<br />
  If in `\t`, timecritical.<br />
  If in passive mode, passivemode.<br />
  If in induction mode, inductionmode.<br />
  If minimized, minimized.<br />
  Otherwise, the execution result, such as 204.<br />
  For cases such as \_\_SYSTEM_ALL_GHOST\_\_, a list delimited by byte value 1.
- **Reference1**: Ghost name or `\0` name.<br />
  For cases such as \_\_SYSTEM_ALL_GHOST\_\_, a list delimited by byte value 1.
- **Reference2**: Event ID that was to be executed.
- **Reference3～**: References for the event that was to be executed.

**対応:** SSP
