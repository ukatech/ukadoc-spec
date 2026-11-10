# Method: GIVE

*\[Legacy specification\]* This method provides a ghost with various types of data for processing or to elicit a response.<br />
This is a very old specification, and there is no reason to use it now. Use NOTIFY or COMMUNICATE instead.

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

- **Document**: A document (a general-purpose string)<br />
  In SHIORI/3.0, this is treated the same as user communicate input, and an OnCommunicate event is raised.
- **Song**: The name of a song.<br />
  In SHIORI/3.0, an OnMusicPlay event is raised, and Reference0 is set to the string specified in the Song header.
