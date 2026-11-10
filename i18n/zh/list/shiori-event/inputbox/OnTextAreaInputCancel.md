# OnTextAreaInputCancel

**カテゴリ:** Input box events

Occurs when a multiline input box (textareabox) is closed.<br />
This event occurs regardless of the ID. Unlike OnUserInputCancel, if a timeout occurs, the event is not redirected to the input submission event.

- **Reference0**: textareabox ID.
- **Reference1**: If timed out, timeout. If closed, close.
- **Reference2**: Content entered before closing. Line breaks are delimited by the character with byte value 1 (`\1`).
- **Reference3～**: Additional information specified with --reference=

**対応:** SSP 2.9.10
