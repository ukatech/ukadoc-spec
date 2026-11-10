# OnTextAreaInputCancel

**カテゴリ:** Input box events

Triggered when a multiline input box (textareabox) is closed.<br />
This event is triggered regardless of the ID. Unlike OnUserInputCancel, a timeout does not cause the event to be rerouted to the input confirmation event.

- **Reference0**: textareabox ID.
- **Reference1**: timeout if timed out; close if closed.
- **Reference2**: Content entered before closing. Line breaks are separated by the character with byte value 1 (`\1`).
- **Reference3～**: Additional information specified by --reference=

**対応:** SSP 2.9.10
