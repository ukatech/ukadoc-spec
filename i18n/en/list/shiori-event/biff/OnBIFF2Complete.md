# OnBIFF2Complete

**カテゴリ:** Mail check event

Occurs when the number of messages in the mail spool increases.<br />
In SSP, this occurs only if no script was returned for OnBIFFComplete.

- **Reference0**: Number of messages in the spool, expressed as a 1-based count.
- **Reference1**: Number of bytes in the spool.
- **Reference2**: Name of the mail server being checked; in SSP and CROW, this is the account name.
- **Reference3**: TopResult for all mail.

**対応:** Materia / SSP
