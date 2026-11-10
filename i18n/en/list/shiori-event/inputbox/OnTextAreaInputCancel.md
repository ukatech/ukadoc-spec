# OnTextAreaInputCancel

**カテゴリ:** Input box event

Occurs when a multiline input box (textareabox) is closed.<br />
This event occurs regardless of the ID. Unlike OnUserInputCancel, on timeout it does not redirect to the input submission event.

- **Reference0**: textareabox ID.
- **Reference1**: If timed out, timeout. If closed, close.
- **Reference2**: Content entered before closing. Newlines are separated by the character with byte value 1 (`\1`).
- **Reference3～**: Additional information specified by --reference=

**対応:** SSP 2.9.10
