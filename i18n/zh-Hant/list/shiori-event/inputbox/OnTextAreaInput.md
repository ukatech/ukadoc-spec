# OnTextAreaInput

**カテゴリ:** Input box events

Triggered when input is entered and confirmed in a [multiline input box (textareabox)](../../sakura-script/open/bang-open-textareabox-ID.md).<br />
If the ID begins with "On", an event named after the ID is triggered instead of this event, and the entered content is placed in Reference0 (subsequent references shift back by one). The same rules as for the [InputBox ID](../../sakura-script/open/bang-close-textareabox-ID.note-2.md) apply.

- **Reference0**: textareabox ID.
- **Reference1**: Entered content. Line breaks are separated by the character with byte value 1 (`\1`).
- **Reference2**: Empty (to align the Reference position with OnUserInput)
- **Reference3～**: Additional information specified by --reference=

**対応:** SSP 2.9.10
