# OnRequestValues

**カテゴリ:** Generic inter-ghost event

Occurs when another ghost sends this event at any time.<br />
When this event is sent, you must send an OnGetValues event using \\\[raiseother\].

- **Reference0**: Name of the sending ghost.
- **Reference1**: Name of the requested variable (key). Reference2 and subsequent references follow the same format for as many requested variables as exist.

**対応:** SSP
