# OnUserInputCancel

**カテゴリ:** Input box events

Triggered when InputBox is closed.<br />
If it times out and this event is not handled, OnUserInput Reference1=timeout is sent for compatibility.

- **Reference0**: Input event ID.
- **Reference1**: timeout if timed out; close if closed.
- **Reference2**: Input details (sliderinput only: minimum, maximum; empty otherwise)
- **Reference3～**: Additional information specified by --reference=

**対応:** SSP / Ninix
