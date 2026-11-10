# OnGetValues

**カテゴリ:** General cross-ghost event

Event returned in response to OnRequestValues.

- **Reference0**: Name of the sending ghost.
- **Reference1**: key=value (key is the variable name received in OnRequestValues, and value is its value). Reference2 and subsequent references follow the same pattern for as many requested variables as exist. Variables that do not exist are not returned. The order in which they were sent in OnRequestValues does not matter.

**対応:** SSP
