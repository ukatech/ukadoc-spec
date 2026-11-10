# OnGetValues

**カテゴリ:** Generic inter-ghost event

Event to return in response to OnRequestValues.

- **Reference0**: Name of the sending ghost.
- **Reference1**: key=value (key is the variable name received in OnRequestValues, and value is its value). Reference2 and subsequent references follow the same format for as many requested variables as exist. Do not return variables that do not exist. The order in which they were sent in OnRequestValues does not matter.

**対応:** SSP
