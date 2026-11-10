# OnBIFFComplete

**カテゴリ:** Mail check event

Occurs when a mail check succeeds.

- **Reference0**: Number of messages in the spool, expressed as a 1-based count.
- **Reference1**: Number of bytes in the spool.
- **Reference2**: Name of the mail server being checked.
- **Reference3**: Difference in new mail.
- **Reference4**: TopResult for all mail. Full list of headers from POP communication. Headers are separated by byte value 1, and messages by byte value 2 (normally, the information in Reference7 should be used).
- **Reference5**: ListResult. IDs on the mail server. Equivalent to the result of the POP command "LIST".
- **Reference6**: UidlResult. IDs used to distinguish messages. Equivalent to the result of the POP command "UIDL".
- **Reference7**: Sender and subject, separated by byte value 1.

**対応:** Materia / SSP / CROW
