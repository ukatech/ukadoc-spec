# OnGetValues

**カテゴリ:** Inter-ghost general event

Event to return upon receiving OnRequestValues.

- **Reference0**: Name of the sending ghost.
- **Reference1**: key=value (key is the variable name received in OnRequestValues, and value is its value). The same applies from Reference2 onward, for as many requested variables as exist. Variables that do not exist are not returned. The order in which they were sent in OnRequestValues does not matter.

**対応:** SSP
