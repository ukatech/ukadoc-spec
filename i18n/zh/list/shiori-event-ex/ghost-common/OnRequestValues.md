# OnRequestValues

**カテゴリ:** Inter-ghost general event

Occurs when another ghost sends this event at its discretion.<br />
When this event is sent, the OnGetValues event must be sent using \\\[raiseother\].

- **Reference0**: Name of the sending ghost.
- **Reference1**: Name of the requested variable (key). The same applies from Reference2 onward, for as many requested variables as exist.

**対応:** SSP
