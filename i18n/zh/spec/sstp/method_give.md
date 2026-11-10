# Method: GIVE

*\[Legacy specification\]* This method gives various kinds of data to a ghost for processing or to trigger a reaction.<br />
This is a very old specification, and there is no reason to use it today. Use NOTIFY or COMMUNICATE instead.

## Request sample

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

## Request-specific headers

- **Document**: Document (a general-purpose string)<br />
  In SHIORI/3.0, this is treated the same as user communicate and triggers the OnCommunicate event.
- **Song**: Song name.<br />
  In SHIORI/3.0, the OnMusicPlay event is triggered, and Reference0 is set to the string specified in the Song header.
