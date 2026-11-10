# OnUserInputCancel

**カテゴリ:** Input box events

Occurs when InputBox is closed.<br />
If a timeout occurs and this event is not handled, OnUserInput Reference1=timeout is sent for compatibility.

- **Reference0**: Input event ID.
- **Reference1**: If timed out, timeout. If closed, close.
- **Reference2**: Input details (sliderinput only: minimum, maximum; empty otherwise)
- **Reference3～**: Additional information specified with --reference=

**対応:** SSP / Ninix
