# OnBIFFComplete

**カテゴリ:** Mail-check event

Occurs when a mail check succeeds.

- **Reference0**: Number of messages in the spool, expressed as a 1-based count.
- **Reference1**: Number of bytes of mail in the spool.
- **Reference2**: Name of the mail server to check.
- **Reference3**: Difference in new mail.
- **Reference4**: TopResult for all mail. Complete list of POP communication headers. Separated by byte value 2 for each message, with headers separated by byte value 1 (normally, use the information in Reference7).
- **Reference5**: ListResult. IDs on the mail server; equivalent to the result of the POP command "LIST".
- **Reference6**: UidlResult. IDs used to distinguish messages; equivalent to the result of the POP command "UIDL".
- **Reference7**: Sender and subject, separated by byte value 1.

**対応:** Materia / SSP / CROW
