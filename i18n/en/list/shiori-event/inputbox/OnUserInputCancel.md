# OnUserInputCancel

**カテゴリ:** Input box event

Occurs when InputBox is closed.<br />
If a timeout occurs and this event is not handled, OnUserInput Reference1=timeout is sent for compatibility.

- **Reference0**: Input event ID.
- **Reference1**: If timed out, timeout. If closed, close.
- **Reference2**: Additional input information (for sliderinput only, minimum,maximum; empty otherwise)
- **Reference3～**: Additional information specified by --reference=

**対応:** SSP / Ninix
