# Method: GIVE

*\[Deprecated specification\]* This method gives various types of data to a ghost for processing or response.<br />
This specification is very old, and there is no reason to use it today. Use NOTIFY or COMMUNICATE instead.

## request example

```
GIVE SSTP/1.1
Charset: UTF-8
Sender: SSTPクライアント
Document: まず水や。それから粉やな。
```

```
GIVE SSTP/1.1
Charset: UTF-8
Sender: SSTPクライアント
Song: 佐世保の時雨
```

## request-specific headers

- **Document**: Document (a general-purpose string)<br />
  In SHIORI/3.0, this is treated the same as user communication, and the OnCommunicate event is triggered.
- **Song**: Song name.<br />
  In SHIORI/3.0, the OnMusicPlay event is triggered, and Reference0 is set to the string specified in the Song header.
