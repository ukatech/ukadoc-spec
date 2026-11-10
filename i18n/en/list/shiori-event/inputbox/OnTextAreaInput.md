# OnTextAreaInput

**カテゴリ:** Input box event

Occurs when input is submitted in a [multiline input box (textareabox)](../../sakura-script/open/bang-open-textareabox-ID.md).<br />
If the ID begins with "On", an event named after the ID is raised instead of this event, and the input is placed in Reference0 (subsequent references each shift back by one). The same rule applies as for the [InputBox ID](../../sakura-script/open/bang-close-textareabox-ID.note-2.md).

- **Reference0**: textareabox ID.
- **Reference1**: Entered content. Newlines are separated by the character with byte value 1 (`\1`).
- **Reference2**: Empty (to align the Reference position with OnUserInput)
- **Reference3～**: Additional information specified by --reference=

**対応:** SSP 2.9.10
